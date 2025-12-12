from odoo import fields, models

class TalerPosOrder(models.Model):
    _inherit = "pos.order"

    # allow_taler_qr = fields.Boolean("Enable Taler QR Payment")

class TalesPosPaymentMethod(models.Model):
    _inherit = "pos.payment.method"

    provider = fields.Selection(
        selection_add=[('taler', "Taler QR Code")],
        ondelete={'taler': 'set default'}
    )

    def get_and_set_online_payments_data(self, next_online_payment_amount=False):
        res = super().get_and_set_online_payments_data(next_online_payment_amount)
        print("TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT")
        print(res)
        return res

