from odoo.exceptions import ValidationError
import logging
_logger = logging.getLogger(__name__)
from odoo import models, fields, api
from string import ascii_letters, digits
import string 

class Aircraft(models.Model):
    _name = 'flight.aircraft'
    _description = 'flight.aircraft'
    

    name = fields.Char(string="Numero de Matrícula", 
        required=True, size=10    )

    aircraft_type_id = fields.Many2one(
        string='Tipo de aeronave', comodel_name='flight.items', ondelete='restrict',
        domain="[('catalogue_id', '=', 1)]", required=True)

    model_id = fields.Many2one(
        string='Modelo', comodel_name='flight.items', ondelete='restrict',
        domain="[('catalogue_id', '=', 2)]", required=True)

    squadron_id = fields.Many2one(
        string='Escuadrón Asignado', comodel_name='flight.items',
        ondelete='restrict', domain="[('catalogue_id', '=', 3)]", required=True)

    acquisition_date = fields.Date(
        string='Fecha de Adquisición', required=True)

    airworthiness_center = fields.Char(
        string='Certificado de Aeronavegabilidad', size=70)

    maker = fields.Char(string="Fabricante", size=70)

    making_year = fields.Char(
        string='Año de Fabricación', required=True, size=4)

    wingspan = fields.Integer(string='Envergadura',)

    turbine_type_id = fields.Many2one(
        string='Tipo de Turbina', comodel_name='flight.items',
        ondelete='restrict', domain="[('catalogue_id', '=', 4)]", required=True)

    
    power = fields.Float(
        string='Potencia', required=True)    

    engine_type_id = fields.Many2one(
        string='Tipo de Motor', comodel_name='flight.items', ondelete='restrict',
        domain="[('catalogue_id', '=', 5)]", required=True)

    maneuver_speed = fields.Float(
        string='Velocidad de Maniobra', required=True)  

    length_dimension = fields.Float(
        string='Longitug', required=True)
    
    height_dimension = fields.Float(
        string='Altura', required=True)  

    economic_speed = fields.Float(
        string='Velocidad Económica', required=True)

    fast_speed= fields.Float(
        string='Velocidad de Crucero Rápido', required=True)

    slow_speed = fields.Float(
        string='Velocidad de Crucero Lento', required=True)

    max_height = fields.Float(
        string='Altura Máxima de Vuelo', required=True)

    mission_class_ids = fields.Many2many(
        string='Clase de Mision', comodel_name='flight.mission.class',
        relation='flight_mission_aircraft_rel', column1='mission_id',
        column2='aircraft_id',required=True)

    navigation_equipment_id = fields.Many2one(
        string='Equipos de Navegación', comodel_name='flight.items',ondelete='restrict',
        domain="[('catalogue_id', '=', 6)]", required=True)

    communication_id = fields.Many2one(
        string='Equipos de Comunicación', comodel_name='flight.items', ondelete='restrict',
        domain="[('catalogue_id', '=', 7)]", required=True)

    detection_id = fields.Many2one(
        string='Equipos de Detección', comodel_name='flight.items', ondelete='restrict',
        domain="[('catalogue_id', '=', 8)]", required=True )

    max_passenger = fields.Integer(
        string='Número Máximo Permitido de Pasajeros', required=True )
    
    load_number = fields.Float(string='Número Máximo Permitido de Carga', )

    max_weight = fields.Float(string='Peso Máximo Permitido por Pasajero', required=True)

    fuel_weight = fields.Float(string='Peso total de combustible',required=True)

    take_off_weight = fields.Float(string='Peso máximo de despegue',required=True)  

    security_type_id = fields.Many2one(
        string='Tipo de Seguro', comodel_name='flight.items', ondelete='restrict',
        domain="[('catalogue_id', '=', 10)]", required=True)

    change_radiogram= fields.Char(
        string="Radiograma de Cambio de Seguro", required=True, size=70)

    security_observation= fields.Text(
        string="Observaciones del seguro", required=True, size=250)  

    status_id = fields.Many2one(
        string='Estado', comodel_name='flight.items', ondelete='restrict',
        domain="[('catalogue_id', '=', 9)]", required=True)

    additional_ids = fields.Many2many(
        string='Equipos Adicionales', comodel_name='flight.addtional.equipment',
        relation='flight_additional_aircraft_rel', column1='additional_id', column2='aircraft_id',)
   
   
   
    security_type_id = fields.Many2one(
        string='Tipo de Seguro', comodel_name='flight.items', ondelete='restrict',
        domain="[('catalogue_id', '=', 10)]" )

    
    #Ingreso del historico
    @api.model
    def create(self, values):  
        result = super(Aircraft, self).create(values)        
        vals={
            'history_security_type_id':values['security_type_id'],
            'history_change_radiogram':values['change_radiogram'],
            'history_security_observation':values['security_observation'],
            'aircraft_id':result.id,
        } 
        self.env['flight.aircraft.history'].create(vals)              
        return result    

   
    @api.onchange('aircraft_type_id','model_id', 'squadron_id','turbine_type_id','engine_type_id',
    'navigation_equipment_id','communication_id', 'detection_id','status_id','security_type_id')
    def _onchange_field(self):
        if(int(self.aircraft_type_id.catalogue_id)!=1):         self.aircraft_type_id=""
        if(int(self.model_id.catalogue_id)!=2):                 self.model_id=""
        if(int(self.squadron_id.catalogue_id)!=3):              self.squadron_id=""
        if(int(self.turbine_type_id.catalogue_id)!=4):          self.turbine_type_id=""        
        if(int(self.engine_type_id.catalogue_id)!=5):           self.engine_type_id=""        
        if(int(self.navigation_equipment_id.catalogue_id)!=6):  self.navigation_equipment_id=""
        if(int(self.communication_id.catalogue_id)!=7):         self.communication_id=""
        if(int(self.detection_id.catalogue_id)!=8):             self.detection_id=""
        if(int(self.status_id.catalogue_id)!=9):                self.status_id=""
        if(int(self.security_type_id.catalogue_id)!=10):        self.security_type_id=""


    warning = {'title': 'Advertancia!', 'message' : 'Your message.' }
   
    @api.onchange('name','maker','making_year','change_radiogram')
    def _name_validation_name(self):
        flag=False
        if set(str(self.name)).difference(ascii_letters + digits + '-'):
            self.warning['message'] ="Caracteres Invalidos en campo NÚMERO DE MATRÍCULA"  
            flag=True 
            self.name=""                            
        if set(str(self.maker)).difference(ascii_letters + digits + '-'):  
            self.warning['message'] ="Caracteres Invalidos en campo FABRICANTE"   
            flag=True
            self.maker=""
        if self.making_year:
            if ((not str(self.making_year).isdigit()) or len(str(self.making_year))!=4):
                self.warning['message'] ="AÑO DE FABRICACIÓN debe tener 4 dígitos"  
                flag=True  
                self.making_year=""          
        if set(str(self.change_radiogram)).difference(ascii_letters + digits + '-'):
            self.warning['message'] ="Caracteres Invalidos en campo RADIOGRAMA DE CAMBIO DE SEGURO"      
            flag=True
            self.change_radiogram=""   
        if flag:                                 
            return {'warning': self.warning}

    
    @api.onchange('take_off_weight')
    def _take_off_weight_validate(self):
        if self.take_off_weight < (self.max_passenger*self.max_weight)+self.fuel_weight:
            self.take_off_weight=""
            self.warning['message'] = "El peso máximo de despegue no puede ser menor\n(Número Máximo Permitido de Pasajeros * Peso Máximo Permitido por Pasajero)+ Peso total de combustible)"
            return {'warning': self.warning}   
    
  
class AircraftHistory(models.Model):
    _name = 'flight.aircraft.history'
    _description = 'flight.aircraft.history'

    history_security_type_id = fields.Many2one(string='Tipo de Seguro', comodel_name='flight.items',
        ondelete='restrict', domain="[('catalogue_id', '=', 10)]", required=True)

    history_change_radiogram= fields.Char(string="Radiograma de Cambio de Seguro", required=True,size=70)

    history_security_observation= fields.Text(string="Observaciones del seguro",  required=True, size=250 )
    
    aircraft_id = fields.Many2one(string='Aeronave', comodel_name='flight.aircraft', ondelete='restrict',)
    

    warning = { 'title': 'Advertancia!', 'message' : 'Your message.' }


    @api.onchange('history_change_radiogram','history_security_observation')
    def _name_validation(self):
        flag=False
        if set(str(self.history_change_radiogram)).difference(ascii_letters + digits + '-'):
            self.warning['message'] ="Caracteres Invalidos en campo RADIOGRAMA DE CAMBIO DE SEGURO"      
            flag=True
            self.history_change_radiogram="" 
        if set(str(self.history_security_observation)).difference(ascii_letters + digits + '-'):
            self.warning['message'] ="Caracteres Invalidos en campo OBSERVACIONES DEL SEGURO"      
            flag=True
            self.history_security_observation="" 
        if flag:                                 
            return {'warning': self.warning} 

    @api.onchange('history_security_type_id')
    def _onchange_field(self):       
        if(int(self.history_security_type_id.catalogue_id)!=10):
            self.history_security_type_id=""    
