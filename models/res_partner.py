from odoo import fields, models

class ResPartner(models.Model):
    _inherit = 'res.partner'

    affiliate_ids = fields.One2many('affiliates.affiliate', 'contact_id', string='Affiliates')
    affiliate_count = fields.Integer(string='Affiliate Count', compute='_compute_affiliate_count')
    affiliate_points_total = fields.Float(string='Affiliate Points Total', compute='_compute_affiliate_points_total')

    def _compute_affiliate_count(self):
        for partner in self:
            partner.affiliate_count = len(partner.affiliate_ids)

    def _compute_affiliate_points_total(self):
        for partner in self:
            partner.affiliate_points_total = sum(partner.affiliate_ids.mapped('points_total'))