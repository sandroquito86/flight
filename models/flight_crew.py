from odoo.exceptions import ValidationError
import logging
_logger = logging.getLogger(__name__)
from odoo import models, fields, api
from string import ascii_letters, digits

class Tripulantes(models.Model):    
    _inherit = ['hr.employee']


    document_id = fields.Char(
      string='Cédula de Identidad',    
      required=True,
      size=10    )     

    crew_degree = fields.Char(
      string='Grado del Tripulante',    
      required=True    )
 
    medical_record_ids = fields.One2many(
       string='Registro Medico',
       comodel_name='flight.medical.record',
       inverse_name='hr_employee_id',
       limit=2,
        )

   
    apto = fields.Char(
       string='Apto',
    )
   
   



class MedicalRecord(models.Model):
    _name = 'flight.medical.record'
    _description = 'flight.medical.record'
    _order="date_report desc" 

   
    result = fields.Char(
       string='Resultado',
    )

    date_report = fields.Date(
       string='Fecha de Informe',
     )

    referent_document = fields.Char(
       string='Documento de Referencia',
    )

    observation = fields.Char(
       string='Observaciones',
    )
   
    hr_employee_id = fields.Many2one(
       string='Tripulantes',
       comodel_name='hr.employee',
       ondelete='restrict',
    )

   
    @api.model
    def create(self, values):         
        record= self.env['hr.employee'].browse(values['hr_employee_id'])
        record.apto=values['result']     
        result = super(MedicalRecord, self).create(values)   
        return result


   
   


   


   






    
    