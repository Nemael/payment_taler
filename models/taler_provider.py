from odoo import models, fields
from odoo.addons.tops import const
import hashlib
import base64
import random
import string
import json
import logging

class TalerPayment(models.Model):
    _inherit = "payment.provider"
    # Because this model inherits, and does not have its own name, there is no need for it to appear in ir.model.access.csv
    # It will inherit the ir security settings from the account.move model

    # This code = 'taler' is a check to recognize that this provider is for Taler
    code = fields.Selection(selection_add=[("taler", "Taler")], ondelete={"taler": "set default"})


    taler_merchant_url = fields.Char(string="Taler Merchant URL",
                                     help="URL to the Taler merchant instance you'd like to use",
                                     default="https://backend.demo.taler.net/instances/sandbox", # this default value is the url to the Taler merchant sandbox environment
                                     groups='base.group_system') # Limits access to this field to admin users (system group)

    taler_merchant_password = fields.Char(string="Taler Merchant Password",
                                          help="Password to the Taler merchant instance you'd like to use",
                                          default="sandbox", # sandbox is the password to the Taler merchant sandbox environment
                                          groups='base.group_system') # Limits access to this field to admin users (system group)

    taler_token = fields.Char(string="Taler Merchant Token, you should not be able to see this parameter",
                              groups='base.group_system') # Limits access to this field to admin users (system group)

    fulfillment_message = fields.Char(string="Taler fulfillment message",
                                      help="Fulfillment message shown to the user after paying for the order",
                                      default="Thank you for your payment with Taler")


    def _get_supported_currencies(self):
        """ Override of payment to return the supported currencies. """
        supported_currencies = super()._get_supported_currencies()
        if self.code == 'taler':
            supported_currencies = supported_currencies.filtered(
                lambda c: c.name in const.SUPPORTED_CURRENCIES
            )
        return supported_currencies

    def _get_default_payment_method_codes(self):
        """ Override of payment to return the default payment method codes. """
        default_codes = super()._get_default_payment_method_codes()
        if self.code != 'taler':
            return default_codes
        return const.DEFAULT_PAYMENT_METHOD_CODES
