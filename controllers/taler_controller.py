# Part of Odoo. See LICENSE file for full copyright and licensing details.

import hmac
import logging
import pprint
import hashlib
import hmac
import requests
from werkzeug.exceptions import Forbidden

from odoo import http
from odoo.exceptions import ValidationError
from odoo.http import request

_logger = logging.getLogger(__name__)


class TalerController(http.Controller):
    _fulfillment_url = '/payment/taler/return'
    #Can delete this one
    _webhook_url = '/payment/taler/webhook'

    @http.route(_fulfillment_url + "/<string:recvd_order_id>/", type='http', auth='public', methods=['GET'])
    def taler_return_from_checkout(self, **data):
        print("RETURNED FROM PAYMENT")
        print(data)
        # print("LATEST ORDER ID 3: ", request.env['payment.transaction'].sudo().merchant_order_id)
        # print("LATEST ORDER ID 3: ", request.env['payment.transaction'])
        transaction = request.env['payment.transaction'].sudo().search([('reference', '=', data.get('recvd_order_id'))])
        if not transaction:
            print("No transaction found for reference: ", data.get('recvd_order_id'))
            return
        received_taler_order_id, taler_orderStatus = transaction._get_orderid_status()
        if received_taler_order_id != transaction.taler_order_id:
            return
        data = {'reference': data.get('recvd_order_id'),
                'merchantOrderId': transaction.taler_order_id,
                # 'transactionId': data.get('transactionId'),
                'paymentStatus': taler_orderStatus
        }
        transaction._handle_notification_data('taler', data)

        return request.redirect('/payment/status')



    # @http.route(_fulfillment_url + "/<string:invoice_check>/<string:invoice_year>/<string:invoice_number>", type='http', auth='public', methods=['GET'])
    # @http.route(_fulfillment_url + "/<path:reference>", type='http', auth='public')
    @http.route(_fulfillment_url + "/<string:prefix>/<int:year>/<string:number>", type='http', auth='public')
    def taler_return_from_invoice(self, **data):
        # pass
        #We need to do invoice reconciliation when a payment leads to this page
        print("TALER RETURNED FROM INVOICE PAYMENT")
        reference = data.get('prefix') + "/" + str(data.get('year')) + "/" + data.get('number')
        print(reference)
        invoice = request.env['account.move'].sudo().search([('name', '=', reference)])
        if not invoice:
            return "Invoice not found"
        transaction = request.env['payment.transaction'].sudo().search([('reference', '=', reference)], limit=1)
        if not transaction:
            return "Transaction not found"

        print("Invoice and transaction found")
        print(invoice)
        print(transaction)

        if transaction.currency_id != invoice.currency_id:
            return "Currency mismatch"


        print("Invoice amount residual: ", invoice.amount_residual)
        if transaction.amount != invoice.amount_residual:
            return "Amount mismatch"


        print("Curency and amount match")

        received_taler_order_id, taler_orderStatus = transaction._get_orderid_status()

        data = {'reference': data.get('recvd_order_id'),
                'merchantOrderId': transaction.taler_order_id,
                # 'transactionId': data.get('transactionId'),
                'paymentStatus': taler_orderStatus
        }

        transaction._handle_notification_data('taler', data)


        print("transactions has been handled")
        print(transaction.state)
        print(transaction.payment_id.journal_id.default_account_id.name)
        print(transaction.payment_id.journal_id.default_account_id.code)
        print("!")
        if transaction.state == 'done':
            print("Transaction has been paid")
            invoice.js_assign_outstanding_line(transaction.id)
        print("ready to return")
        #return request.redirect('/payment/status')





        # print(invoice)
        # print("----------------------------------------------------")
        # print(invoice.taler_order_id)
        # print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        # for payment in invoice.matched_payment_ids:
        #     print(payment.payment_transaction_id)
        #     print(payment.payment_transaction_id.taler_order_id)
        # print("??????????????????????")
        # print(invoice.origin_payment_id)
        # print(invoice.origin_payment_id.taler_order_id)
        # print(",,,,,,,,,,,,,,,,,,,,,,,,,")
        # print(invoice.matched_payment_ids)
        # for payment in invoice.matched_payment_ids:
        #     print(payment.taler_order_id)
