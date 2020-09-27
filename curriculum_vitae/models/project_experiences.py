from odoo import models, fields


class ProjectExperiences(models.Model):
    _name = 'project.experiences'

    image = fields.Binary(string="Image")
    name = fields.Char(string="Project Name")
    position = fields.Char(string="Position")
    responsibilities = fields.Char(string="Responsibilities")
    programming_languages = fields.Char(string="Programming Languages")
    period_from = fields.Date(string="Period From")
    period_to = fields.Date(string="Period To")
    description = fields.Text(string="Description")

    curriculum_vitae_id = fields.Many2one('curriculum.vitae')
