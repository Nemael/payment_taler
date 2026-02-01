# SPDX-FileCopyrightText: 2025 Mael Panouillot <panouillot.mael@gmail.com>
#
# SPDX-License-Identifier: LGPL-3.0-or-later

from odoo import models, fields
from odoo.addons.tops import const
from odoo.exceptions import ValidationError
from odoo.addons.tops.models.taler_api_methods import getMerchantConfiguration


class TalerProvider(models.Model):
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
                                      help="""Fulfillment message shown to the user on the Taler merchant ordes after paying for the order. Note: This message does not show on Odoo itself, see the "Messages" tab for this purpose.""",
                                      default="Thank you for your payment with Taler")

    def is_in_test_mode(self):
        provider_state = self.state # Possible values: disabled, enabled, test
        return provider_state == 'test'

    def _compute_feature_support_fields(self):
        super()._compute_feature_support_fields()
        for provider in self:
            self.filtered(lambda p: p.code == 'taler').update({
                'support_refund': 'full_only'
            })

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

    def merchant_url_check_button(self):
        """ Checks the validity of the Taler merchant URL set by the user. """
        response = getMerchantConfiguration(self.taler_merchant_url)
        if not response["name"] or not response["name"] == "taler-merchant" or not response["version"] or not response["currencies"]:
            raise ValidationError("The Taler Merchant URL is invalid")

        # Checks if the currencies used by Odoo are all included in the supported currencies by the Taler Merchant
        merchant_currencies = []
        for currency in response["currencies"].keys():
            merchant_currencies.append(currency)

        odoo_currencies_missing_in_merchant = []
        for odoo_currency in self.available_currency_ids:
            if odoo_currency.name not in merchant_currencies:
                odoo_currencies_missing_in_merchant.append(odoo_currency.name)
        if len(odoo_currencies_missing_in_merchant) > 0:
            raise ValidationError("The Taler Merchant URL is invalid.\nCurrencies supported on Odoo side: " + str(odoo_currencies_missing_in_merchant) + ".\nCurrencies supported on Taler merchant side: " + str(merchant_currencies) + ".\nDiscrepancy: " + str(odoo_currencies_missing_in_merchant))

        # If everything is ok, create an "ok" popup for the user
        confirmation_string_for_user = "The Taler Merchant URL is valid and the currencies are compatible. "
        confirmation_string_for_user += "Merchant name: " + response["name"]
        confirmation_string_for_user += ". Merchant version: " + response["version"]
        confirmation_string_for_user += ". Currencies: "
        for currency in response["currencies"].keys():
            confirmation_string_for_user += currency + ", "
        confirmation_string_for_user = confirmation_string_for_user[:-2] # Remove the last two characters, which will be ", "

        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': 'Info',
                'message': confirmation_string_for_user,
                'type': 'success',
                'sticky': False,
            }
        }
