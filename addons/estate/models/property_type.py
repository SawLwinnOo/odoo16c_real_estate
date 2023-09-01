from odoo import api, fields, models


class PropertyType(models.Model):
    _name = 'estate.property.type'
    _description = 'PropertyType'

    name = fields.Char(required=True)

    _sql_constraints = [
        ('unique_type_name', 'UNIQUE(name)', 'Type Name must be unique.'),
    ]


