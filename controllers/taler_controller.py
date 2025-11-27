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
        print("LATEST ORDER ID 3: ", request.env['payment.transaction'].sudo().test_latest_order_id)
        print("LATEST ORDER ID 3: ", request.env['payment.transaction'])
        transaction = request.env['payment.transaction'].sudo().search([('reference', '=', data['recvd_order_id'])])
        transaction._check_if_order_is_paid()


