import uuid
from odoo import fields, models, api


class Affiliate(models.Model):
    _name = 'affiliates.affiliate'
    _description = 'Affiliates'

    name = fields.Char(string='Affiliate User name', invisible=1, required=0)
    contact_id = fields.Many2one('res.partner', string='Affiliate User', required=True, onchange="_onchange_contact_id")
    affiliate_group_id = fields.Many2one('affiliates.group', string='Affiliate Group Name', required=True)
    approved = fields.Boolean(string='Approved')
    website_guid = fields.Char(string='Website GUID', required=True, readonly=True, default=lambda self: str(uuid.uuid4()))
    parent_affiliate_id = fields.Many2one('res.partner', string='Parent Affiliate')
    sub_affiliate_ids = fields.Many2many('res.partner', string='Sub-Affiliates')
    points_transaction_ids = fields.One2many('points.transaction', 'affiliate_id', string='Points Transactions')

    points_total = fields.Float(string='Points Total', compute='_compute_points_total')

    @api.depends('points_transaction_ids.points_awarded')
    def _compute_points_total(self):
        for record in self:
            record.points_total = sum(record.points_transaction_ids.mapped('points_awarded'))

    @api.onchange('contact_id')
    def _onchange_contact_id(self):
        if self.contact_id:
            self.name = self.contact_id.email