# -- coding: utf-8 --
from odoo import models , fields , api


class ProductCategory(models.Model):
    _inherit = 'product.category'

    #-----------------
    #field declaration
    #-----------------
    assign_sequence = fields.Boolean(string = "Assign sequence")
    



  