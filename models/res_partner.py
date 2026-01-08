from odoo import api, fields, models, _

class ResPartner(models.Model):
    _inherit = 'res.partner'

    moroso = fields.Boolean(
        string='Moroso',
        help='Indica si el contacto está en condición de moroso.'
    )

    def action_mark_moroso(self):
        for record in self:
            if not record.moroso:
                record.moroso = True

    def action_unmark_moroso(self):
        for record in self:
            if record.moroso:
                record.moroso = False

    def write(self, vals):
        res = super().write(vals)
        if 'moroso' in vals:
            for rec in self:
                if rec.moroso:
                    rec.message_post(
                        body=_("El contacto ha sido marcado como moroso por %s.") % self.env.user.name,
                        subtype_xmlid="mail.mt_note"
                    )
                else:
                    rec.message_post(
                        body=_("La morosidad ha sido levantada por %s.") % self.env.user.name,
                        subtype_xmlid="mail.mt_note"
                    )
        return res