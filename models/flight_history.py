from odoo import models, fields, api

class HistorySecurityType(models.Model):
    _name = 'flight.aircraft.history.securitytype'
    _description = 'flight.aircraft.history.securitytype'

    history_security_type_id = fields.Many2one(string='Tipo de Seguro', comodel_name='flight.items',
        ondelete='restrict', domain="[('catalogue_id', '=', 10)]",)

    history_change_radiogram= fields.Char(string="Radiograma de Cambio de Seguro" ,size=70)

    history_security_observation= fields.Text(string="Observaciones del seguro" , size=250 )

    history_additional_equipment= fields.Text(string="Equipamento Adicional" , size=250 )
    
    aircraft_id = fields.Many2one(string='Aeronave', comodel_name='flight.aircraft', ondelete='cascade',)
    

    warning = { 'title': 'Advertencia!', 'message' : 'Your message.' }


class HistoryEquipment(models.Model):
    _name = 'flight.aircraft.history.equipment'
    _description = 'flight.aircraft.history.equipment'    

    history_additional_equipment= fields.Text(string="Equipamento Adicional" , size=250 )
    aircraft_id = fields.Many2one(string='Aeronave', comodel_name='flight.aircraft', ondelete='cascade',)
    
    
    



    