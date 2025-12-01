from odoo import models, fields, api
from odoo.addons.tops.utils.utils import *
import requests
import base64
import qrcode
from io import BytesIO

class AccountMove(models.Model):
    _inherit = 'account.move'
    taler_notice = fields.Char(string="Taler notice", default="")
    taler_fulfillment_message = fields.Char(string="Fulfillment message", default="")
    taler_currency = fields.Char(string="Test Order Currency", default="KUDOS")
    taler_summary = fields.Char(string="Test Order Summary", default="Test order")
    taler_amount = fields.Char(string="Test Order Amount", default="0.01")
    taler_order_id = fields.Char(string="Taler Order ID", default="")
    taler_order_url = fields.Char(string="Taler Order URL", default="")
    taler_order_uri = fields.Char(string="Taler Order URI", default="")
    taler_qr_image = fields.Char(string="Taler QR")

    def _get_taler_notice(self):
        print("getting taler notice")
        # Compute or fetch your custom value here
        return self.taler_notice

    def _get_report_base_filename(self):
        #probably can remove this
        print("getting report base filename")
        return super()._get_report_base_filename()

    # Inject variable for the PDF report
    def _get_invoice_report_values(self):
        print("getting invoice report values")
        res = super()._get_invoice_report_values()

        # for move in self:
        #     res[move.id]["taler_notice"] = move._get_taler_notice()

        return res

    # @api.model_create_multi
    # def write(self, vals_list):
    #     # Call the original create method first
    #     records = super().write(vals_list)
    #
    #     # Now your custom code runs after creation
    #     for record in records:
    #         print("CHECKING RECORD")
    #         print(record.preferred_payment_method_line_id.name)
    #         #IN THE IF, REMOVE EITHER THE OUT OR THE IN-INVOICE
    #         if record.move_type in ('out_invoice', 'in_invoice') and record.preferred_payment_method_line_id.name == "Taler2":
    #             record._my_custom_post_creation()
    #
    #     return records

    def action_post(self):
        res = super().action_post()
        print("move confirm")
        for move in self:
            print("CHECKING MOVE")
            print(move.preferred_payment_method_line_id.name)
            if move.move_type in ('out_invoice', 'in_invoice') and move.preferred_payment_method_line_id.name == "Taler2":  # only invoices/bills
                move._my_custom_post_creation()

        return res


    def _my_custom_post_creation(self):
        print("My custom post creation")
        self.taler_notice = "My custom post creation"
        self._requestGetToken()
        self._postPlaceOrder()
        self.taler_qr_image = self._generate_qr(self.taler_order_uri)
        print(self.taler_qr_image)

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

    def _getOrderTalerUri(self, order_id):
        merchant_url = self.env['ir.config_parameter'].sudo().get_param('tops.merchant_url', default='')
        url = merchant_url + "/private/orders/" + order_id

        payload = ""
        headers = {
            "User-Agent": "TalerOdoo/insomnia/11.3.0",
            "Authorization": "Bearer " + self.env['ir.config_parameter'].sudo().get_param('tops.secret_token')
        }
        talog("Headers: ", headers)
        talog("Payload: ", payload)
        response = requests.request("GET", url, data=payload, headers=headers)
        talog("Response received")
        if response.status_code != 200:
            talog("Error getting order taler payment URI, bad response: ", response.text)
            return ''
        if "taler_pay_uri" not in response.json():
            talog("Error getting taler_pay_uri field: ", response.text)
            return ''
        return response.json()["taler_pay_uri"]

    def _postPlaceOrder(self):
        merchant_url = self.env['ir.config_parameter'].sudo().get_param('tops.merchant_url', default='')
        url = merchant_url + "/private/orders"
        payload = {
            "order": {
                "amount": self.taler_currency + ":" + self.taler_amount,
                "summary": self.taler_summary,
                "fulfillment_message": self.taler_fulfillment_message,
            },
            "create_token": False
        }
        talog(self.env['ir.config_parameter'].sudo().get_param('tops.secret_token'))
        headers = {
            "Content-Type": "application/json",
            "User-Agent": "TalerOdoo/insomnia/11.3.0",
            "Authorization": "Bearer " + self.env['ir.config_parameter'].sudo().get_param('tops.secret_token')
        }
        talog("Headers: ", headers)
        talog("Payload: ", payload)
        response = requests.request("POST", url, json=payload, headers=headers)
        talog("Response received")
        talog(response.text)
        if response.status_code != 200:
            talog("Error placing order, bad response: ", response.text)
            return
        if "order_id" not in response.json():
            talog("Error getting new order_id: ", response.text)
            return
        order_id = response.json()["order_id"]
        order_url = merchant_url + "/orders/" + order_id
        order_uri = self._getOrderTalerUri(order_id)
        print("??????????????????", order_uri)
        talog("order_id: ", order_id)

        self.taler_order_id = order_id
        self.taler_order_url = order_url
        self.taler_order_uri = order_uri
        print("??????????????????", self.taler_order_uri)
        self.taler_notice = self.taler_order_id
        print("LATEST ORDER ID 1: ", self.taler_order_id)



    #THIS METHOD SHOULD MAYBE BE IN THE UTILS FOLDER
    def _generate_qr(self, url):
        print("????? Generating QR code")
        qr = qrcode.QRCode(box_size=10, border=2)
        qr.add_data(url)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")

        buf = BytesIO()
        img.save(buf, format='PNG')
        qr_bytes = buf.getvalue()
        print("{{{{{{{{{{{{{{", base64.b64encode(qr_bytes).decode("utf-8"))

        return base64.b64encode(qr_bytes).decode("utf-8")
