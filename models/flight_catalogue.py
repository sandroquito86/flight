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

    sub_catalogue_ids = fields.One2many(
        string='Catalogo',
        comodel_name='flight.items',
        inverse_name='catalogue_id',
    )


class Items(models.Model):
    _name = 'flight.items'
    _description = 'flight.items'

    name = fields.Char(string="Item", 
    help='Escriba el nombre del item asociado a su catálogo',
    required=True
    )    

    description = fields.Char(string="Descripcion", 
    required=True
    )

    
    catalogue_id = fields.Many2one(
        string='Catalogo',
        comodel_name='flight.catalogue',
        ondelete='restrict',
    )

    _sql_constraints = [
        ('name_unique',
         'UNIQUE(catalogue_id,name)',
         "Items debe ser único dentro de cada catálogo"),
    ]
    

    @api.constrains('name')
    def _check_name_insensitive(self):
        model_ids = self.search(['&',('id', '!=',self.id),('catalogue_id', '=', int(self.catalogue_id))])        
        list_names = [x.name.upper() for x in model_ids if x.name]        
        if self.name.upper() in list_names:
            raise ValidationError("Ya existe un registro con el nombre: %s " % (self.name.upper()))
            
            

 
class MisionClass(models.Model):
   _name = 'flight.mission.class'
   _description = 'flight.mission.class'
   name = fields.Char(string="Clase de Misión", 
    required=True
    )

class AdditionalEquipment(models.Model):
   _name = 'flight.addtional.equipment'
   _description = 'flight.addtional.equipment'
   name = fields.Char(string="Equipo Adicional", 
    required=True
    )

