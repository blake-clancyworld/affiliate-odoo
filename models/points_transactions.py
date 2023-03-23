from odoo import fields, models

class PointsTransaction(models.Model):
    _name = 'points.transaction'
    _description = 'Points Transactions'
    
    date = fields.Date(string='Date', default=fields.Date.today(), readonly=True)
    action_name = fields.Char(string='Action Name')
    points_awarded = fields.Float(string='Points Awarded')
    affiliate_id = fields.Many2one('affiliates.affiliate', string='Affiliate')
    parent_affiliate_id = fields.Many2one('res.partner', string='Parent Affiliate')
    sub_affiliate_ids = fields.Many2many('res.partner', string='Sub-Affiliates')
    website_guid = fields.Char(string='Website GUID')
