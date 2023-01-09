# -*- coding: utf-8 -*-
from odoo import models, fields , api

class iot_event(models.Model):
    _name='iot.event'
    _description = 'IOT Event'

    active = fields.Boolean(default=True)
    device_id = fields.Many2one(comodel_name='iot.device', string='Device' , required = "1")
    data = fields.Text("Data" , help='Data associated with the event')
