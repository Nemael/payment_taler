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

    @http.route(_fulfillment_url, type='http', auth='public', methods=['GET'])
    def taler_return_from_checkout(self, **data):
        print("RETURNED FROM PAYMENT")


