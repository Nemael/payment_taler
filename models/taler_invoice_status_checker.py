from odoo import models, api
import requests
import logging

from odoo.addons.tops.controllers.taler_controller import TalerController

_logger = logging.getLogger(__name__)

class TalerInvoiceStatusChecker(models.Model):
    _name = "tops.invoice.status.checker"
    _description = "TOPS Invoice Status Checker"

    def check_payment_status(self):
        _logger.info("Running TOPS payment status check...")

        invoices = self.env['account.move'].search([
            ('move_type', '=', 'out_invoice'),
            #Maybe consider the in_invoice as well, I don't know the difference yet
            ('payment_state', '!=', 'paid'),
            # payment_state possible values:
                # ('not_paid', 'Not Paid'),
                # ('in_payment', 'In Payment'),
                # ('paid', 'Paid'),
                # ('partial', 'Partially Paid'),
                # ('reversed', 'Reversed'),
                # ('blocked', 'Blocked'),
                # ('invoicing_legacy', 'Invoicing App Legacy'),

            ('state', '=', 'posted'),
            # state possible values:
            #     ('draft', 'Draft'),
            #     ('posted', 'Posted'),
            #     ('cancel', 'Cancelled'),
        ])

        for invoice in invoices:
            print(invoice)
            if invoice.payment_method == "Taler2":
                if self.check_order_status(invoice):
                    self._register_invoice_payment(invoice)


    def _register_invoice_payment(self, invoice):
        payment_vals = {
            'payment_type': 'inbound',
            'partner_type': 'customer',
            'partner_id': invoice.partner_id.id,
            'amount': invoice.amount_residual,
            'currency_id': invoice.currency_id.id,
            'payment_date': api_data.get("paid_at"),
            'journal_id': self.env['account.journal'].search(
                [('type', '=', 'bank')], limit=1
            ).id,
            'ref': f"Taler API Payment for {invoice.name}",
        }

        payment = self.env['account.payment'].create(payment_vals)
        payment.action_post()

        # Reconcile automatically
        (payment.line_ids + invoice.line_ids).filtered(
            lambda l: l.account_id.internal_type == 'receivable'
        ).reconcile()

    def check_order_status(self, invoice):
        try:
            return(self._check_if_order_is_paid(invoice.taler_order_id))
        except Exception as e:
            _logger.error("Taler API order status check failed for %s: %s", invoice.name, e)

    def _requestGetToken(self):
        talog("Getting token")
        merchant_url = self.env['ir.config_parameter'].sudo().get_param('tops.merchant_url', default='')
        talog(merchant_url)
        url = merchant_url + "/private/token"
        payload = {"scope": "write"}
        headers = {
            "Content-Type": "application/json",
            "User-Agent": "TalerOdoo",
            "Authorization": "Bearer secret-token:" + self.env['ir.config_parameter'].sudo().get_param('tops.password', default='')
        }
        talog("Headers: ", headers)
        talog("Payload: ", payload)
        response = requests.request("POST", url, json=payload, headers=headers)
        talog("Response received")
        talog(response.text)
        if response.status_code != 200:
            talog("Error getting token, bad response: ", response.text)
            return
        if "token" not in response.json():
            talog("Error getting new token: ", response.text)
            return
        self.env['ir.config_parameter'].sudo().set_param('tops.secret_token', response.json()["token"])
        talog(self.env['ir.config_parameter'].sudo().get_param('tops.secret_token'))


    def _check_if_order_is_paid(self, merchant_order_id):
        print("CHECK IF ORDER IS PAID")
        print("LATEST ORDER ID 2: ", merchant_order_id)
        response = self.requestGetOrderFromId(merchant_order_id)
        print(response.json()["order_status"])
        return response.json()["order_status"] == "paid"

    def requestGetOrderFromId(self, merchant_order_id):
        print(merchant_order_id)
        merchant_url = self.env['ir.config_parameter'].sudo().get_param('tops.merchant_url', default='')
        print(merchant_url)
        url = merchant_url + "/private/orders/" + merchant_order_id
        payload = ""
        headers = {
            "User-Agent": "TalerOdoo",
            "Authorization": "Bearer " + self.env['ir.config_parameter'].sudo().get_param('tops.secret_token')
        }
        talog("Headers: ", headers)
        talog("Payload: ", payload)
        response = requests.request("GET", url, data=payload, headers=headers)
        talog("Response received")
        # talog(response.text)
        if response.status_code != 200:
            talog("Error getting order from id, bad response: ", response.text)
            return
        return(response)
