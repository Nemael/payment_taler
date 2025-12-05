from odoo import models, fields
from odoo.addons.tops.utils.utils import generate_qr
from odoo.addons.tops.models.taler_api_methods import requestGetToken, postPlaceOrderWithFulfillmentMessage

class TalerInvoicing(models.Model):
    _inherit = ['account.move']
    # _inherit = 'account.move'

    taler_notice = fields.Char(string="Taler notice", default="") #can remove from here and xml file
    taler_fulfillment_message = fields.Char(string="Fulfillment message", default="")
    taler_currency = fields.Char(string="Test Order Currency", default="KUDOS")
    taler_summary = fields.Char(string="Test Order Summary", default="Test order")
    taler_amount = fields.Char(string="Test Order Amount", default="0.01")
    taler_order_id = fields.Char(string="Taler Order ID", default="")
    taler_order_url = fields.Char(string="Taler Order URL", default="")
    taler_order_uri = fields.Char(string="Taler Order URI", default="")
    taler_qr = fields.Char(string="Taler QR")

    def action_post(self):
        res = super().action_post()
        print("move confirm")
        for move in self:
            print("CHECKING MOVE")
            print(move.preferred_payment_method_line_id.name)
            if move.move_type in ('out_invoice', 'in_invoice') and move.preferred_payment_method_line_id.name == "Taler2":  # only invoices/bills
                #I should probably make this if only for either out or in invoices
                move._taler_invoice_create()
        return res

    def _taler_invoice_create(self):
        print("My custom invoice creation")
        self.taler_notice = "My custom post creation"
        requestGetToken(self)
        self.taler_order_id, self.taler_order_url, self.taler_order_uri = postPlaceOrder(self, self.taler_currency, self.taler_amount, self.taler_order_id, self.taler_order_url)
        self.taler_notice = self.taler_order_id
        self.taler_qr = generate_qr(self.taler_order_uri)
