# -*- coding: utf-8 -*-
from odoo import models, fields , api

class pertronic_event_device(models.Model):
    _name='iot.device'
    _description = 'IOT Device'

    active = fields.Boolean(default=True)
    name = fields.Char("Name")
    device_id = fields.Integer()