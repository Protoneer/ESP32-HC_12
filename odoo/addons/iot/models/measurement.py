# -*- coding: utf-8 -*-
from odoo import models, fields , api

class measurement(models.Model):
    _name='iot.measurement'
    _description = 'Measurement'

    device_id = fields.Many2one(comodel_name='iot.device', string='Device' , required = "1")
    type = fields.Many2one(comodel_name='iot.measurement_type', string='Device' , required = "1")

    value_char = fields.Char()
    value_number = fields.Float()




    def process_event(self,event):  
        def decode_message(message):
            result = {
                'from_adr' : ord(message[1]),
                'to_adr' : ord(message[2]),
                'function' : ord(message[3]),
                'size' : ord(message[4]),
                'body' : message[5:5+ord(message[4])],
                'crc' : ord(message[5+ord(message[4])]),
                
                }
            return result

        decoded = decode_message(event.data)

        if decoded['from_adr'] == 2 and decoded['function'] == 5:          
            self.env['iot.measurement'].create({
                "device_id" : 4,
                "type" : 1,
                "value_number" : decoded['body'].split(',')[0]
            })

            self.env['iot.measurement'].create({
                "device_id" : 4,
                "type" : 2,
                "value_number" : decoded['body'].split(',')[2]
            })


class measurement_types(models.Model):
    _name='iot.measurement_type'
    _description = 'Measurement Type'

    name = fields.Char()