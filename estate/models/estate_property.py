from odoo import fields, models


class Property(models.Model):
    _name = "estate.property"
    _description = "Properties of an estate"
    name = fields.Char(string="Title", required=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(string="Available From", copy=False, default=fields.Date.add(fields.Date.today(), months=3))
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True, copy=False)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer(string="Living Area (sqm)")
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        selection = [("north", "North"),("west", "West"),("east","East"),("south","South")]
    )
    active = fields.Boolean(default=True)
    state = fields.Selection(
        selection = [("new","New"), ("offer_received","Offer Received"), ("offer_cccepted","Offer Accepted"), ("sold","Sold"), ("canceled","Canceled")],
        required = True,
        default = "new",
        copy = False,
    )
    # Exercise of Ch.6-1 is done in Ch.2

