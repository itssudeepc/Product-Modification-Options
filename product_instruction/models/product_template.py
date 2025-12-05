from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = "product.template"

    product_instructions = fields.One2many(
        "product.instructions",
        "product_tmpl_id",
        string="Custom Addons",
    )
