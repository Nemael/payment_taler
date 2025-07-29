from odoo import models, fields
import requests
# from ..utils import *
from ..utils.utils import *

class Order(models.Model):
    _name = 'tops.order'
    _description = 'This is an order made with the Taler payment system, using the Taler-Odoo Payment System add-on.'
    _order = 'creation_time desc'

    taler_id = fields.Char(string="Order Id on Taler side", required=True)
    current_status = fields.Char(string="Current Order Status")
    summary = fields.Char(string="Order Summary", required=True)
    fulfilment_message = fields.Char(string="Order Fulfillment Message")
    amount = fields.Char(string="Order Amount", required=True)
    currency = fields.Char(string="Order Currency", required=True)
    creation_time = fields.Char(string="Order Creation Time", required=True)
    payment_time = fields.Char(string="Order Payment Time")
    merchant_server = fields.Char(string="Merchant Server the order was created on")
    url = fields.Char(string="Last Order URL", required=True)
    uri = fields.Char(string="Last Order URI")
    merchant_refund_window = fields.Char(string="Merchant Refund Window", required=True)


    # secret_token = fields.Char(string="Current Secret Token")
    # test_order_id = fields.Char(string="Test OrderID", default="2025.191-02D3GX2J9ME3M")
    # refund_time = fields.Char(string="Order Refund Time")
    # latest_order_id = fields.Char(string="Latest Order Id", default="1")
