# -- coding: utf-8 --
from odoo import models

class MrpWorkorder(models.Model):
    _inherit = 'mrp.workorder'


    #------------------
    #method declaration
    #------------------

    def start_timer(self):
        for record in self:
            if not record.is_user_working:
                record.button_start()

    def stop_timer(self):
        for record in self:
            if record.is_user_working:
                record.button_pending()

    def done_workorder(self):
        for record in self:
            if record.is_user_working:
                record.button_finish()

