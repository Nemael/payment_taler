from odoo import models, fields

class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    merchant_url = fields.Char(string="Merchant URL", related="company_id.merchant_url")


class ResCompany(models.Model):
    _inherit = "res.company"

    merchant_url = fields.Char(string="Merchant URL")
