from odoo.exceptions import ValidationError
import logging
_logger = logging.getLogger(__name__)
from odoo import models, fields, api
from string import ascii_letters, digits
import string 

class GestionPlanSemanal(models.Model):
    _name = 'flight.gestion.plan.semanal'
    _description = 'flight.gestion.plan.semanal'    

    descripcion = fields.Char(string='Descripción',size=80,required=True)

    semana_plan_vuelo = fields.Date( string='Semana del plan de vuelo',size=80,required=True)    
    
    planificacion_culminada = fields.Boolean(string='Planificación culminada', default=False )
    
    state = fields.Selection([
        ('activo', 'activo'),
        ('planificado', 'planificado'),
        ('sale', 'Sales Order'),
        ('done', 'Locked'),
        ('cancel', 'Cancelled'),
        ], string='Status', readonly=True, copy=False, index=True, tracking=3, default='activo')    
    
    observacion_reparto = fields.Text(
        string='Observaciones Director Reparto:',
    )
    
    observacion_coavna = fields.Text(
        string='Observaciones Director COAVNA',
    )      

class VuelosPlanificados(models.Model):
    _name = 'flight.vuelos.planificados'
    _description = 'flight.vuelos.planificados'

    tipo_vuelo_id = fields.Many2one(
        string='Tipo de vuelo', comodel_name='flight.items', ondelete='restrict', domain="[('catalogo_id', '=', 12)]",)
    
    aeronave_id = fields.Many2one(
        string='Aeronaves',comodel_name='flight.aircraft',ondelete='restrict',required=True)

    matricula = fields.Char(
        string='matricula',related='aeronave_id.name',store=True )   
    
    
    
    mision_planvuelo_ids = fields.Many2many(
        string='Misiones Plan de Vuelo',
        comodel_name='flight.mision.planvuelo',
        relation='plavuelo_misionplanvuelo_rel',
        column1='vueloplanificado_id',
        column2='misionvueloplanificado_id', 
        domain="[('aeronave_id', '=', aeronave_id)]"
     )
     
     
     
    
    
   
    
       
    
    fecha_vuelo = fields.Date(
        string='Fecha de vuelo',default=fields.Date.context_today,        
        domain=[('fecha_vuelo','>=',fields.Date.context_today)])
    
    hora = fields.Date( string='Hora',default=fields.Date.context_today,)

    piloto_id = fields.Many2one(
        string='Piloto', comodel_name='flight.qualification', ondelete='restrict', )    
    
    copiloto_id = fields.Many2one(
        string='Copiloto', comodel_name='flight.qualification',ondelete='restrict')    
    
    ingeniero_vuelo_id = fields.Many2one(
        string='Ingeniero de vuelo', comodel_name='flight.qualification', ondelete='restrict')
    
    operador_electro_id = fields.Many2one(
        string='Operador Electro/óptico', comodel_name='flight.qualification', ondelete='restrict')
    
    radarista_id = fields.Many2one(
        string='Radarista', comodel_name='flight.qualification', ondelete='restrict', )    

    taco_id = fields.Many2one(
        string='Taco', comodel_name='flight.qualification', ondelete='restrict')
    
    ruta_salida_id = fields.Many2one(
        string='Ruta de salida', comodel_name='res.country.state', ondelete='restrict', )

    operacion_id = fields.Many2one(
        string='Operación o Destino', comodel_name='res.country.state', ondelete='restrict',)

    ruta_retorno_id = fields.Many2one(
        string='Ruta de retorno', comodel_name='res.country.state', ondelete='restrict',)
    
    
    mecanico_ids = fields.One2many(
        string='Mecánico', comodel_name='flight.qualification', inverse_name='habilitacion_id', ) 
    
    
    """
    @api.onchange('aeronave_id')
    def _onchange_field(self):             
        domain=[('aeronave_id','=',int(self.aeronave_id))]        
        record=self.env['flight.mision.planvuelo'].search(domain)
        #raise ValidationError("llego {}".format(record)  
        self.mision_planvuelo_ids=record
    """
    
    
    
    
    

    

    
    

    

    
    

    

    
    




    



