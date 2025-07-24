from odoo import models, fields

class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    merchant_url = fields.Char(string="Taler Merchant URL", config_parameter='tops.merchant_url')
