# -- coding: utf-8 --

from odoo import models, fields, api
from datetime import timedelta

class SaleOrder(models.Model):
    _inherit='sale.order'

    #---------------------------------------
    #fied declaration
    #---------------------------------------

    appointment_date = fields.Datetime(string="Appointment Date")
    commitment_date = fields.Datetime('Delivery Date', copy=False,compute='_compute_delivery_date', readonly=False)
                    
                                     

    #---------------------------------------
    #method declaration
    #---------------------------------------

    # @api.onchange('appointment_date')
    # def _onchange(self):
    #     for record in self:
    #         if record.appointment_date and record.partner_id.days_to_deliver > 0:
    #             record.commitment_date = record.appointment_date - timedelta(days=record.partner_id.days_to_deliver)


    #---------------------------------------
    #method declaration
    #---------------------------------------

    @api.depends('appointment_date')
    def _compute_delivery_date(self):
        for record in self:
            if record.appointment_date and record.partner_id.days_to_deliver > 0:
                record.commitment_date = record.appointment_date - timedelta(days=record.partner_id.days_to_deliver)




    #---------------------------------------
    #method declaration
    #---------------------------------------

    # def action_confirm(self):
    #  res = super(SaleOrder, self).action_confirm()
    #  for record in self.picking_ids :
    #       record.appointment_date = self.appointment_date
    #  return res