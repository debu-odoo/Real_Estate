# -- coding: utf-8 --
from odoo import models , api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    #-------------------
    #method declaration
    #-------------------
    @api.model
    def create(self, vals):
        res = super(ProductTemplate, self).create(vals)
        if res.categ_id and res.categ_id.assign_sequence:
            res.default_code = self.env['ir.sequence'].next_by_code('product.template')
        elif res.categ_id.parent_id:
            approval_list = []
            approval_list = self.find_parent_category_sequence(res.categ_id.parent_id,approval_list)
            if approval_list:
                res.default_code = self.env['ir.sequence'].next_by_code('product.template')
        return res

    def find_parent_category_sequence(self, parent_category, approval_list):
        parent_parent_category = parent_category.parent_id
        if parent_category.assign_sequence:
            approval_list.append(True)
        else:
            self.find_parent_category_sequence(parent_parent_category,approval_list)
        return approval_list



    

   