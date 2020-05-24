from odoo.exceptions import ValidationError
import logging
_logger = logging.getLogger(__name__)
from odoo import models, fields, api
from string import ascii_letters, digits
import string 

class GestionPlanSemanal(models.Model):
    _name = 'flight.gestion.plan.semanal'
    _description = 'flight.gestion.plan.semanal'

    

    descripcion = fields.Char(
        string='Descripción',size=80,required=True)

    semana_plan_vuelo = fields.Date(
        string='Semana del plan de vuelo',size=80,required=True)



    estado = fields.Selection(
        string='Estado',
        selection=[('activo', 'activo'), ('planificado', 'planificado'),('aprobado director reparto', 'aprobado director reparto')
            , ('aprobado operaciones COAVNA', 'aprobado operaciones COAVNA'),('aprobado director COAVNA', 'aprobado director COAVNA')
            , ('rechazado', 'rechazado'), ('desactivado', 'desactivado')]
    )
    
    planificacion_culminada = fields.Boolean(
        string='Planificación culminada', 
        default=False
        
    )

class VuelosPlanificados(models.Model):
    _name = 'flight.vuelos.planificados'
    _description = 'flight.vuelos.planificados'

    tipo_vuelo_id = fields.Many2one(
        string='Tipo de vuelo', comodel_name='flight.items', ondelete='restrict',
        domain="[('catalogue_id', '=', 13)]", required=True)
    
    aeronave_id = fields.Many2one(
        string='Aeronaves',comodel_name='flight.aircraft',ondelete='restrict',required=True)

    matricula = fields.Char(
        string='matricula',related='aeronave_id.name',readonly=True)  
   
    mission_class_ids = fields.Many2many(
    related='aeronave_id.mission_class_ids', readonly=True,)    
    
    fecha_vuelo = fields.Date(
        string='Fecha de vuelo',default=fields.Date.context_today,        
        domain=[('fecha_vuelo','>=',fields.Date.context_today)])
    
    hora = fields.Date( string='Hora',default=fields.Date.context_today,)

    piloto_id = fields.Many2one(
        string='Piloto', comodel_name='flight.qualification', ondelete='restrict', required=True)

    copiloto_id = fields.Many2one(
        string='Piloto', comodel_name='flight.qualification', ondelete='restrict')

    
    mecanico_ids = fields.Many2many(
        string='Mecánico', comodel_name='flight.qualification', relation='mecanico_vuelos_planificado_rel',
        column1='vuelo_planificado_id',column2='tripulante_mecanico_id', required=True )

    ingeniero_vuelo_id = fields.Many2one(
        string='Ingeniero de vuelo', comodel_name='flight.qualification', ondelete='restrict')
    
    radarista_id = fields.Many2one(
        string='Radarista', comodel_name='flight.qualification', ondelete='restrict')

    operador_electro_id = fields.Many2one(
        string='Operador Electro/óptico', comodel_name='flight.qualification', ondelete='restrict')

    taco_id = fields.Many2one(
        string='Taco', comodel_name='flight.qualification', ondelete='restrict')

    ruta_salida_id = fields.Many2one(
        string='Ruta de salida', comodel_name='res.country.state', ondelete='restrict', 
       
        )

    operacion_id = fields.Many2one(
        string='Operación o Destino', comodel_name='res.country.state', ondelete='restrict', 
        
        )

    ruta_retorno_id = fields.Many2one(
        string='Ruta de retorno', comodel_name='res.country.state', ondelete='restrict', 
        
        )

    

    
    
    

    

    
    

    

    
    

    

    
    




    



