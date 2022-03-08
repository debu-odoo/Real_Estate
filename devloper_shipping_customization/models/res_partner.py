# -- coding: utf-8 --

from odoo import fields , models

class ResPartner(models.Model):
    _inherit = 'res.partner'


    #------------------------------------------------
    #fields declaration
    #------------------------------------------------
    days_to_deliver = fields.Integer(string = "Days to Deliver")
