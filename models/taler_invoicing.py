from odoo import models, fields
from odoo.addons.tops.utils.utils import generate_qr
from odoo.addons.tops.models.taler_api_methods import requestGetToken, postPlaceOrderWithFulfillmentMessage

class TalerInvoicing(models.Model):
    _inherit = 'account.move'

    is_taler_invoice = fields.Boolean(default=False)
    taler_fulfillment_message = fields.Char(string="Fulfillment message", default="")
    taler_currency = fields.Char(string="Test Order Currency", default="KUDOS")
    taler_summary = fields.Char(string="Test Order Summary", default="Test order")
    taler_amount = fields.Char(string="Test Order Amount", default="0.01")
    taler_order_id = fields.Char(string="Taler Order ID", default="")
    taler_order_url = fields.Char(string="Taler Order URL", default="")
    taler_order_uri = fields.Char(string="Taler Order URI", default="")
    taler_qr = fields.Char(string="Taler QR")


    #I maybe can remove this provider_id field, it was for invoices. To test
    provider_id = fields.Many2one(
        "payment.provider",
        string="Taler Provider",
        default=lambda self: self.env["payment.provider"].search([("code", "=", "taler")], limit=1).id,
    )

    def action_post(self):
        res = super().action_post()
        print("move confirm")
        for move in self:
            print("CHECKING MOVE")
            print(move.preferred_payment_method_line_id.name)
            if move.move_type in ('out_invoice', 'in_invoice') and move.preferred_payment_method_line_id.code == "taler":  # only invoices/bills
                #I should probably make this "if" only for either 'out' or 'in' invoices
                self.is_taler_invoice = True
                move._taler_invoice_create()
        return res

    def _taler_invoice_create(self):
        print("My custom invoice creation")
        # self.provider_id = self.env['payment.provider'].search([('code', '=', 'taler')], limit=1)
        #Delete this one
        order_summary = "Odoo reference " + self.name + " for " + str(self.amount_total) + str(self.currency_id.symbol) + " " + self.currency_id.name
        requestGetToken(self)
        self.taler_order_id, self.taler_order_url, self.taler_order_uri = postPlaceOrderWithFulfillmentMessage(self,
                                                                                                               # self.currency_id.name,
                                                                                                               "KUDOS", # testing value, remove for release and uncomment line above
                                                                                                               # self.amount_total,
                                                                                                               "0.02", # testing value, remove for release and uncomment line above
                                                                                                               order_summary,
                                                                                                               self.provider_id.fulfillment_message)
        self.taler_qr = generate_qr(self.taler_order_uri)
