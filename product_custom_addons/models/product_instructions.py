from odoo import models, fields, _


class ProductInstructions(models.Model):
    _name = "product.instructions"
    _description = "Product Custom Addon"
    _rec_name = 'product_instructions'
    _order = 'id desc'

    product_instructions = fields.Char(
        string="Custom Addon",
        required=True,
        translate=True,
        help="Custom addon instruction for the product"
    ) 

    product_tmpl_id = fields.Many2one(
        'product.template',
        string='Product Template',
        ondelete='cascade'
    )

    def name_get(self):
        result = []
        for record in self:
            name = record.product_instructions or str(record.id)
            result.append((record.id, name))
        return result
