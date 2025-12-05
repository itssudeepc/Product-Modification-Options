# In sales_order.py

import logging
from odoo import models, fields, api, _

_logger = logging.getLogger(__name__)

# Existing SaleOrderLine class (keep this)
class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    product_instructions_ids = fields.Many2many(
        'product.instructions',
        string="Custom Addons",
        compute='_compute_product_instructions',
        store=True,
        readonly=True,
    )
    selected_instruction_id = fields.Many2one(
        'product.instructions',
        string="Selected Addon",
        store=True,
    )

    @api.depends('product_id')
    def _compute_product_instructions(self):
        for line in self:
            if line.product_id:
                line.product_instructions_ids = line.product_id.product_tmpl_id.product_instructions.ids
            else:
                line.product_instructions_ids = False

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    def _website_product_id_change(self, order_id, product_id, qty=0):
        # 1. Call the super method to get the base values for the line
        line_values = super()._website_product_id_change(order_id, product_id, qty=qty)
        # 2. Get the selected_instruction_id from the context/request parameters
        selected_instruction_id = self.env.context.get('selected_instruction_id')
        
        # 3. If an ID is found, add it to the line_values dictionary
        if selected_instruction_id:
            # The value is passed as a string from the JS, ensure it's an integer ID
            try:
                line_values['selected_instruction_id'] = int(selected_instruction_id)
            except ValueError:
                _logger.warning("Invalid selected_instruction_id received: %s", selected_instruction_id)
                
        return line_values