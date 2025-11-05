from odoo import fields, models, api
from datetime import timedelta


class PropertyOffer(models.Model):
    _name = 'estate.property.offer'
    _description = 'Real Estate Property Offers'

    price=fields.Float(string="Price")
    status=fields.Selection(
        [
            ('accepted', 'Accepted'),
            ('refused', 'Refused')
        ],
        string="Status"
    )
    partner_id = fields.Many2one('res.partner', string="Partner", domain=[('company_id','=',1)])
    complete_name = fields.Char(related="partner_id.complete_name", string="Partner complete_name")
    property_id=fields.Many2one('estate.property', string="Property")
    validity=fields.Integer(string="Validity")
    deadline= fields.Date(string="Deadline", compute="_compute_deadline")
    creation_date= fields.Date(string="Create Date")


    @api.depends('validity','creation_date')
    def _compute_deadline(self):
        for res in self:
            if res.creation_date and res.validity:
                res.deadline=res.creation_date + timedelta(days=res.validity)
            else:
                res.deadline=False
