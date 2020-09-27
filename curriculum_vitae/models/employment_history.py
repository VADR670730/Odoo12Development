from odoo import models, fields


class EmploymentHistory(models.Model):
    _name = 'employment.history'

    image = fields.Binary(string="Image")
    name = fields.Char(string="Company Name", required=True)
    position = fields.Char(string="Position")
    responsibilities = fields.Char(string="Responsibilities")
    period_from = fields.Date(string="Period From")
    period_to = fields.Date(string="Period To")
    description = fields.Text(string="Description")

    curriculum_vitae_id = fields.Many2one('curriculum.vitae')
