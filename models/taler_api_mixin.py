from odoo import models, fields, api

class TalerMixin(models.AbstractModel):
    _name = "taler.api.mixin"
    _description = "Taler Mixin to connect to Taler Merchant API"

    def printA(self):
        print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
