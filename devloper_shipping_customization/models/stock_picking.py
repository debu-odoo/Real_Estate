# -- coding: utf-8 --

from odoo import api, models , fields
from datetime import timedelta



class StockPicking(models.Model):
    _inherit = 'stock.picking'

    #------------------------------------------------
    #fields declaration
    #------------------------------------------------

    appointment_date = fields.Datetime(string = 'Appointment Date')
    scheduled_date = fields.Datetime('Scheduled Date' , copy = False , readonly = False )

    
    #---------------------------------------
    #method declaration
    #---------------------------------------

    @api.onchange('appointment_date')
    def _onchange_scheduled_date(self):
        for record in self:
             if record.appointment_date and record.partner_id.days_to_deliver > 0:
                 record.scheduled_date = record.appointment_date - timedelta(days=record.partner_id.days_to_deliver)



    #---------------------------------------
    #method declaration
    #---------------------------------------

    # @api.depends('appointment_date')
    # def _compute_scheduled_date(self):
    #     for record in self:
    #         if record.appointment_date and record.partner_id.days_to_deliver > 0:
    #             record.scheduled_date = record.appointment_date - timedelta(days=record.partner_id.days_to_deliver)

