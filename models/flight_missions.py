from odoo.exceptions import ValidationError
import logging
_logger = logging.getLogger(__name__)
from odoo import models, fields, api
from string import ascii_letters, digits
import string 

class Mission(models.Model):
   _name = 'flight.mission'
   _description = 'flight.mission'

   name = fields.Char(string="Código de la Misión", 
   required=True, size=20
   )
   
    
   mission_type_id = fields.Many2one(
        string='Tipo de Misión',
        comodel_name='flight.mission.class',
        ondelete='restrict',
   )

   attachment_ids = fields.Many2many(
        comodel_name='ir.attachment',
        relation='attachments_rel',
        column1='mission_id',
        column2='attachment_id',
        string='Archivo Adjunto'
   )

   
   @api.onchange('name')
   def _name_validation(self):                
      if set(str(self.name)).difference(ascii_letters + digits + '-'):                   
         self.name=""
            
   @api.onchange('attachment_ids')
   def _archive(self):      
      if(len(self.attachment_ids)>1): 
         self.attachment_ids.unlink(self.id)          
      text=str(self.attachment_ids.name)
      if self.attachment_ids.name:
         if not text.endswith(".pdf"): 
            self.attachment_ids.unlink()             
         else:
            if(text.find(" ")<0):
               if set(text).difference(ascii_letters + digits + '-' + '.'):                                
                  self.attachment_ids.unlink()                     
            else:
               self.attachment_ids.unlink() 
      

      
         
    
               
               
         
               
            
      
     
    