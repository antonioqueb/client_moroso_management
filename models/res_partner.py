# -*- coding: utf-8 -*-
from odoo import api, fields, models, _

class ResPartner(models.Model):
    _inherit = 'res.partner'

    moroso = fields.Boolean(
        string='Moroso',
        help='Indica si el contacto está en condición de moroso.'
    )

    def action_mark_moroso(self):
        """
        Marca al partner como moroso y lo archiva (active=False).
        Solo debe ejecutarse si el usuario tiene el grupo apropiado.
        """
        for record in self:
            record.moroso = True
            record.active = False

    def action_unmark_moroso(self):
        """
        Quita la marca de moroso y reactiva (active=True) al partner.
        """
        for record in self:
            record.moroso = False
            record.active = True

    def write(self, vals):
        """
        Sobrescribimos write para que, si se modifica 'moroso' desde
        la vista en árbol, se archive o reactive automáticamente.
        """
        res = super(ResPartner, self).write(vals)
        if 'moroso' in vals:
            for rec in self:
                if rec.moroso:
                    rec.active = False
                else:
                    rec.active = True
        return res
