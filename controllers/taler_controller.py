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
    _webhook_url = '/payment/taler/webhook'

    @http.route(_fulfillment_url + "/<string:recvd_order_id>/", type='http', auth='public', methods=['GET'])
    def taler_return_from_checkout(self, **data):
        print("RETURNED FROM PAYMENT")
        print(data)
        # print("LATEST ORDER ID 3: ", request.env['payment.transaction'].sudo().merchant_order_id)
        # print("LATEST ORDER ID 3: ", request.env['payment.transaction'])
        transaction = request.env['payment.transaction'].sudo().search([('reference', '=', data.get('recvd_order_id'))])
        received_merchant_order_id, merchant_orderStatus = transaction._get_orderid_status()
        if received_merchant_order_id != transaction.merchant_order_id:
            print("ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR the merchant order id and the odoo order id are different")
            return
        data = {'reference': data.get('recvd_order_id'),
                'merchantOrderId': transaction.merchant_order_id,
                # 'transactionId': data.get('transactionId'),
                'paymentStatus': merchant_orderStatus
        }
        transaction._handle_notification_data('taler', data)

        return request.redirect('/payment/status')




