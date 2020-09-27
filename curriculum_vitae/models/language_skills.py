from odoo import models, fields


class LanguageSkills(models.Model):
    _name = 'language.skills'

    name = fields.Char(string="Language", required=True)
    level = fields.Char(string="Level")
    education_center = fields.Char(string="Education Center")
    description = fields.Text(string="Description")

    curriculum_vitae_id = fields.Many2one('curriculum.vitae')
