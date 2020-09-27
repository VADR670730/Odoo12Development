from odoo import models, fields


class EducationBackground(models.Model):
    _name = 'education.background'

    image = fields.Binary(string="Image")
    name = fields.Char(string="Name")

    country = fields.Char(string="Country")
    certification = fields.Char(string="Certification")
    description = fields.Char(string="Description")
    period_from = fields.Date(string="Period From")
    period_to = fields.Date(string="Period To")

    curriculum_vitae_id = fields.Many2one('curriculum.vitae')
