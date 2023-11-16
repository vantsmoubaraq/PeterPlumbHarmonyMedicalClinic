from odoo import models, fields

class Estate(models.Model):
    """Class implements estate"""
    _name = "estate.property"
    _description = "Lists property details"


    name = fields.Char("Property name")
    description = fields.Text("Description")
    postcode = fields.Char("Postcode")
    date_availability = fields.Date(string="Availability Date")
    expected_price = fields.Float("Expected_price")
    selling_price = fields.Float("Selling_price")
    bedrooms = fields.Integer("Number of bedrooms")
    living_area = fields.Integer("Living areas")
    facades = fields.Integer("Facades")
    garage = fields.Boolean("Garage")
    garden = fields.Boolean("Garden")
    garden_area = fields.Integer("Garden Area")
    garden_orientation = fields.Selection([("landscape", "landscape"), ("potrait", "potrait")], string="Garden orentation")



