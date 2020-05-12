from odoo import models, fields, api

class Tripulantes(models.Model):
    _name = 'sistema_vuelo.tripulantes'
    _description = 'sistema_vuelo.tripulantes'

    name = fields.Char(string="Nombre de Tripulante", 
    required=True
    )
   
    dato = fields.Char(
       string='dato Tripulante',
    )
    