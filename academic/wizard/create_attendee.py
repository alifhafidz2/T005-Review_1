from odoo import models, fields, api, _

class CreateAttendeeWizard(models.TransientModel):
    _name = 'academic.create.attendee.wizard'

    session_id  = fields.Many2one(comodel_name='academic.session', string='Session')
    partner_ids = fields.Many2many(comodel_name='res.partner', string='Attendees to Add')

    session_ids = fields.Many2many(comodel_name='academic.session', string='Sessions')

    def action_add_attendee(self):
        self.ensure_one()
        session = self.session_id
        att_data = [{'partner_id': att.id} for att in self.partner_ids]
        for session in self.session_ids:
            session.attendee_ids = [(0,0,data) for data in att_data]
        return{'type': 'ir.actions.act_window_close'}