from odoo import fields, models

class PointsAction(models.Model):
    _name = 'points.action'
    _description = 'Points Action'
    
    name = fields.Char(string='Points Action name', required=True)
    action_type = fields.Selection([('new_user_signup', 'New User Sign Up'),
                                    ('any_product_sale', 'Any Product Sale'),
                                    ('specific_product_sale', 'Specific Product Sale'),
                                    ('affiliate_signup', 'Affiliate Signup'),
                                    ('sale_from_sub_affiliate', 'Sale from Sub-affiliate')],
                                   string='Points Action', required=True)
    product_ids = fields.Many2many('product.product', string='Products')
    points = fields.Float(string='Points')
