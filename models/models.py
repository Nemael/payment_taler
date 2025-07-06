from odoo import models, fields

class Student(models.Model):
    _name = 'wb.student'
    _description = 'This is student profile.'
    name = fields.Char(string="Name")
    description = fields.Text(string="Description")


    name1 = fields.Char(string="Name1")
    name2 = fields.Char(string="Name2")
    name3 = fields.Char(string="Name3")
    name4 = fields.Char(string="Name4")
