# -- coding: utf-8 --

from odoo import fields , models, api
from odoo.exceptions import UserError


class SaleOrder(models.Model):
    _inherit = 'sale.order'


    #---------------------------------------
    #field declaration
    #---------------------------------------

    zero_stock_approval = fields.Boolean(string = "Zero Stock Approval")
    compute_field = fields.Boolean(string="Zero Stock Approval", compute='set_readonly_approval')
    


    #---------------------------------------
    #method declaration
    #---------------------------------------

    def action_confirm(self):
     for record in self:
         if record.zero_stock_approval:
                return super(SaleOrder, self).action_confirm()
         else:
             raise UserError ("Please Check Zero Stock Approval field")

    @api.depends('zero_stock_approval')
    def set_readonly_approval(self):
        for record in self:
            record.compute_field = self.env.user.has_group('sales_team.group_sale_manager')

   
     

  
     
    
def action_confirm(self):
     for record in self:
         if record.zero_stock_approval:
            return super(SaleOrder, self).action_confirm()
            
         raise UserError ("Please Check Zero Stock Approval field")