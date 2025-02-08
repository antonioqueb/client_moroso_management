# -*- coding: utf-8 -*-
# client_moroso_management/models/res_partner.py

from odoo import api, fields, models, _

class ResPartner(models.Model):
    _inherit = 'res.partner'

    moroso = fields.Boolean(
        string='Moroso',
        help='Indica si el contacto está en condición de moroso.'
    )

    def action_mark_moroso(self):
        """
        Marca al partner como moroso y lo archiva.
        (Se elimina el message_post aquí para no duplicar chatter,
        pues write() lo controlará al modificar 'moroso'.)
        """
        for record in self:
            if not record.moroso:  # Evita registrar si ya está moroso
                record.moroso = True
                record.active = False
                # Se comenta/retira el message_post para evitar duplicación
                # record.message_post(
                #     body=_("El contacto ha sido marcado como moroso por %s el %s.") % 
                #          (self.env.user.name, fields.Datetime.now()),
                #     subtype_xmlid="mail.mt_note"
                # )

    def action_unmark_moroso(self):
        """
        Quita la marca de moroso, reactiva el partner.
        (Se elimina el message_post aquí para no duplicar chatter,
        pues write() lo controlará al modificar 'moroso'.)
        """
        for record in self:
            if record.moroso:  # Evita registrar si ya no es moroso
                record.moroso = False
                record.active = True
                # Se comenta/retira el message_post para evitar duplicación
                # record.message_post(
                #     body=_("La morosidad ha sido levantada por %s el %s.") % 
                #          (self.env.user.name, fields.Datetime.now()),
                #     subtype_xmlid="mail.mt_note"
                # )

    def write(self, vals):
        """
        Sobrescribimos write para que, si se modifica 'moroso' desde
        cualquier vista, se archive o reactive y se registre en el chatter
        un único mensaje.
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
