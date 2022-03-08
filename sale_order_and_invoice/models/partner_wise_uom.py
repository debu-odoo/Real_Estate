# -- coding: utf-8 --
from odoo import models , fields , api

class PartnerwiseUom(models.Model):
    _name = 'partner.wise.uom'
    _discription = 'Partner Wise Uom'


    #------------------------
    #Fields Declaration
    #------------------------

    partner_id = fields.Many2one('res.partner',string = "Partner Id")
    product_id = fields.Many2one('product.product',string = "Product Id" )
    uom_id = fields.Many2one('uom.uom',string = "Uom Id" , domain="[('category_id','=', uom_cat_id)]")
    uom_cat_id = fields.Many2one(related="product_id.uom_id.category_id")

   

    





    

  