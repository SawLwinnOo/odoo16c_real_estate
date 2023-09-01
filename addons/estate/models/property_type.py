from odoo import api, fields, models


class PropertyType(models.Model):
    _name = 'estate.property.type'
    _description = 'PropertyType'

    name = fields.Char(required=True)


