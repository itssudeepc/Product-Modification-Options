odoo.define('product_instruction.product_instructions', function (require) {
    "use strict";

    const publicWidget = require('web.public.widget');

    publicWidget.registry.WebsiteSale.include({
        _onClickAdd: function (ev) {
            let $form = $(ev.currentTarget).closest('form');

            // Get only radios inside this product form
            const $selectedRadio = $form.find('input.product-instruction-radio:checked');
            const selectedInstruction = $selectedRadio.val();
            console.log(selectedInstruction);
            console.log($selectedRadio);
            console.log($form);
            // Remove old hidden input
            $form.find('input[name="selected_instruction_id"]').remove();

            if (selectedInstruction) {
                $("<input />").attr({
                    type: "hidden",
                    name: "selected_instruction_id",
                    value: selectedInstruction,
                }).appendTo($form);
            }

            return this._super.apply(this, arguments);
        },
    });
});
