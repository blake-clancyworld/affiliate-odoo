from odoo import fields, models

class AffiliateGroup(models.Model):
    _name = 'affiliates.group'
    _description = 'Affiliate Group'
    
    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    affiliate_ids = fields.One2many('affiliates.affiliate', 'affiliate_group_id', string='Affiliate Members')
    point_action_ids = fields.Many2many('points.action', string='Points List Matrix')
