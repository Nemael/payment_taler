from odoo import models, fields
import hashlib
import base64
import random
import string
import json
import logging

#Payment Provider code: https://github.com/odoo/odoo/blob/18.0/addons/payment/models/payment_provider.py#L14

SUPPORTED_CURRENCIES = [
    'AED',
    'AUD',
    'BGN',
    'BRL',
    'CAD',
    'CHF',
    'CZK',
    'DKK',
    'EUR',
    'GBP',
    'HKD',
    'HRK',
    'HUF',
    'ILS',
    'ISK',
    'JPY',
    'MXN',
    'MYR',
    'NOK',
    'NZD',
    'PHP',
    'PLN',
    'RON',
    'RUB',
    'SEK',
    'SGD',
    'THB',
    'TWD',
    'USD',
    'ZAR'
]


class TalerPayment(models.Model):
    _inherit = "payment.provider"

    print("adding code")
    code = fields.Selection(selection_add=[("taler", "Taler")], ondelete={"taler": "set default"})
    print("code added")
    taler_api_key = fields.Char(string="taler_api_key")

    def _get_supported_currencies(self):
        """ Override of `payment` to return the supported currencies. """
        supported_currencies = super()._get_supported_currencies()
        if self.code == 'taler':
            supported_currencies = supported_currencies.filtered(
                lambda c: c.name in SUPPORTED_CURRENCIES
            )
        return supported_currencies


    CONTINUER D'IMPLEMENTER TOUTES LES METHODES QUI SONT DANS LES FICHIERS DU MODULE MOLLIE D'ODOO, POUR CONTINUER A IMPLEMENTER MON PAYMENT PROVIDER

    def _mollie_make_request(self, endpoint, data=None, method='POST'):
        pass

    def _get_default_payment_method_codes(self):
        pass

    # provider = fields.Selection(selection_add = [("taler", "Taler")])
    # provider = fields.Selection(
    #     selection_add=[('taler', "Taler")],
    #     ondelete={'taler': 'set default'}
    # )



    # #@api.model
    # def _get_payment_method_information(self):
    #     """Override to add createtest payment method information to the
    #     existing methods.
    #     """
    #     res = super()._get_payment_method_information()
    #     res['createtest'] = {'mode': 'unique', 'domain': [('type', '=', 'bank')]}
    #     return res

    # taler_order_status_url = fields.Char(string="Taler Order Status URL")
    # taler_order_id = fields.Char(string="Taler Order ID")
    # taler_fulfillment_url = fields.Char(string="Taler Fulfillment URL")
    #
    # name = fields.Char(string="name")
    # company_id = fields.Char(string="company_id")
    # state = fields.Char(string="state")
    # view_template_id = fields.Char(string="view_template_id")
    # pre_msg = fields.Char(string="pre_msg")
    # post_msg = fields.Char(string="post_msg")


    # def newprovider_form_generate_values(selfself, values):
    #     pass
    #
    # def newprovider_get_form_action_url(self):
    #     pass
