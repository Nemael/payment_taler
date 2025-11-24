from odoo import models, fields
from odoo.addons.tops import const
import hashlib
import base64
import random
import string
import json
import logging

#Payment Provider code: https://github.com/odoo/odoo/blob/18.0/addons/payment/models/payment_provider.py#L14



class TalerPaymentMethod(models.Model):
    _name = 'tops.method'
    _inherit = "payment.method"
    name = fields.Char(string="Taleneioteinpfneiwftr", required=True, translate=True)
    code = fields.Char(
        string="taleriiiii", help="The technical code of this payment method.", required=True
    )
    sequence = fields.Integer(string="Sequence", default=1)
    primary_payment_method_id = fields.Many2one(
        string="Talerlllllll",
        help="The primary payment method of the current payment method, if the latter is a brand."
             "\nFor example, \"Card\" is the primary payment method of the card brand \"VISA\".",
        comodel_name='payment.method',
    )
    brand_ids = fields.One2many(
        string="Talerdddddddd",
        help="The brands of the payment methods that will be displayed on the payment form.",
        comodel_name='payment.method',
        inverse_name='primary_payment_method_id',
    )
    provider_ids = fields.Many2many(
        string="talerfffff",
        help="The list of providers supporting this payment method.",
        comodel_name='payment.provider',
    )
    active = fields.Boolean(string="Active", default=True)
    image = fields.Image(
        string="Image",
        help="The base image used for this payment method; in a 64x64 px format.",
        max_width=64,
        max_height=64,
        required=True,
    )
    image_payment_form = fields.Image(
        string="The resized image displayed on the payment form.",
        related='image',
        store=True,
        max_width=45,
        max_height=30,
    )
    # # Feature support fields.
    # support_tokenization = fields.Boolean(
    #     string="Tokenization",
    #     help="Tokenization is the process of saving the payment details as a token that can later"
    #          " be reused without having to enter the payment details again.",
    # )
    # support_express_checkout = fields.Boolean(
    #     string="Express Checkout",
    #     help="Express checkout allows customers to pay faster by using a payment method that"
    #          " provides all required billing and shipping information, thus allowing to skip the"
    #          " checkout process.",
    # )
    # support_refund = fields.Selection(
    #     string="Refund",
    #     help="Refund is a feature allowing to refund customers directly from the payment in Odoo.",
    #     selection=[
    #         ('none', "Unsupported"),
    #         ('full_only', "Full Only"),
    #         ('partial', "Full & Partial"),
    #     ],
    #     required=True,
    #     default='none',
    # )
    # supported_country_ids = fields.Many2many(
    #     string="Countries",
    #     comodel_name='res.country',
    #     help="The list of countries in which this payment method can be used (if the provider"
    #          " allows it). In other countries, this payment method is not available to customers."
    # )
    # supported_currency_ids = fields.Many2many(
    #     string="Currencies",
    #     comodel_name='res.currency',
    #     help="The list of currencies for that are supported by this payment method (if the provider"
    #          " allows it). When paying with another currency, this payment method is not available "
    #          "to customers.",
    #     context={'active_test': False},
    # )

