from odoo.exceptions import ValidationError
import logging
_logger = logging.getLogger(__name__)
from odoo import models, fields, api



class Catalogue(models.Model):
    _name = 'flight.catalogue'
    _description = 'flight.catalogue'

    name = fields.Char(string="Nombre del Catalogo", 
    required=True
    )

    items_ids = fields.One2many(
        string='Catalogo',
        comodel_name='flight.items',
        inverse_name='catalogo_id',
    )
    
    


class Items(models.Model):
    _name = 'flight.items'
    _description = 'flight.items'

    name = fields.Char(string="Item", 
    help='Escriba el nombre del item asociado a su catálogo',
    required=True
    )    

    descripcion = fields.Char(string="Descripcion", 
    required=True
    )
    
    catalogo_id = fields.Many2one(
        string='Catalogo',
        comodel_name='flight.catalogue',
        ondelete='restrict',
    )

    _sql_constraints = [
        ('name_unique',
         'UNIQUE(catalogo_id,name)',
         "Items debe ser único dentro de cada catálogo"),
    ]    
    
  
    @api.constrains('name')
    def _check_name_insensitive(self):
        model_ids = self.search(['&',('id', '!=',self.id),('catalogo_id', '=', int(self.catalogo_id))])        
        list_names = [x.name.upper() for x in model_ids if x.name]        
        if self.name.upper() in list_names:
            raise ValidationError("Ya existe un registro con el nombre: %s " % (self.name.upper()))
          
           

 
class MisionClass(models.Model):
   _name = 'flight.mission.class'
   _description = 'flight.mission.class'
   
   name = fields.Char(string="Clase de Misión", 
    required=True )
   
   
   mision_ids = fields.One2many(
       string='Misiones',
       comodel_name='flight.mision.planvuelo',
       inverse_name='mision_id',       
       ondelete='restrict'
       
   )
   
 
class AdditionalEquipment(models.Model):
    _name = 'flight.addtional.equipment'
    _description = 'flight.addtional.equipment'
    _rec_name= "name"

    name = fields.Char(string="Equipo Adicional", 
    required=True )
    
    
   
class Habilitaciones (models.Model):
    _name = 'flight.habilitaciones'
    _description = 'flight.habilitaciones'    
    
    name = fields.Char(
        string='Nombre',
    )
    
class MisionPlanVuelo(models.Model):
    _name = 'flight.mision.planvuelo'
    _description = 'flight.mision.planvuelo'
    _rec_name = 'mision_id'    
    
    mision_id = fields.Many2one(
        string='Mision',
        comodel_name='flight.mission.class',
        ondelete='restrict',
    )   
    
    aeronave_id = fields.Many2one(
        string='Aeronave',
        comodel_name='flight.aircraft',
        ondelete='restrict',
    )
    
    
class Escuadron(models.Model):
    _name = 'flight.escuadron'
    _description = 'flight.escuadron'   
    
    name = fields.Char(string='Nombre',)    
    
    siglas = fields.Char(string='Siglas',)    
    
    ciudad_id = fields.Many2one(string='Ciudad',comodel_name='flight.ciudad',
        ondelete='restrict',)
    


class Ciudad(models.Model):
    _name = 'flight.ciudad'
    _description = 'flight.ciudad'   
    
    name = fields.Char(string='Ciudad',)     
    

class TiposMotores(models.Model):
    _name = 'flight.tipos.motores'
    _description = 'flight.tipos.motores'    
    
    name = fields.Char(string='Nombre',)
    modelo = fields.Char(string='Modelo',)
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
   
   
    

