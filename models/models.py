from odoo import models, fields

class MyModel(models.Model):
    _name = 'my.model'
    _description = 'My Custom Model'
    name = fields.Char(string="Name")
    description = fields.Text(string="Description")
