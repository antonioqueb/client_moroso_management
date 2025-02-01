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
        Marca al partner como moroso, lo archiva y deja un mensaje en el chatter.
        """
        for record in self:
            if not record.moroso:  # Evita registrar si ya está moroso
                record.moroso = True
                record.active = False
                record.message_post(
                    body=_("El contacto ha sido marcado como moroso por %s el %s.") % 
                         (self.env.user.name, fields.Datetime.now()),
                    subtype_xmlid="mail.mt_note"
                )

    def action_unmark_moroso(self):
        """
        Quita la marca de moroso, reactiva el partner y deja un mensaje en el chatter.
        """
        for record in self:
            if record.moroso:  # Evita registrar si ya no es moroso
                record.moroso = False
                record.active = True
                record.message_post(
                    body=_("La morosidad ha sido levantada por %s el %s.") % 
                         (self.env.user.name, fields.Datetime.now()),
                    subtype_xmlid="mail.mt_note"
                )

    def write(self, vals):
        """
        Sobrescribimos write para que, si se modifica 'moroso' desde
        la vista en árbol, se archive o reactive automáticamente
        y se registre en el chatter.
        """
        res = super(ResPartner, self).write(vals)
        if 'moroso' in vals:
            for rec in self:
                if rec.moroso:
                    rec.active = False
                    rec.message_post(
                        body=_("El contacto ha sido marcado como moroso por %s el %s.") % 
                             (self.env.user.name, fields.Datetime.now()),
                        subtype_xmlid="mail.mt_note"
                    )
                else:
                    rec.active = True
                    rec.message_post(
                        body=_("La morosidad ha sido levantada por %s el %s.") % 
                             (self.env.user.name, fields.Datetime.now()),
                        subtype_xmlid="mail.mt_note"
                    )
        return res
