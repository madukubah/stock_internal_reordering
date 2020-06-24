 # -*- coding: utf-8 -*-
from odoo import api, fields, models, _

class QaqcCoa(models.Model):
	_name = "qaqc.coa"

	name = fields.Char(string="Name", size=100 , required=True)
	ni_spec = fields.Float( string="Ni Specification (%)", required=True, default=0, digits=0 )
	fe_spec = fields.Float( string="Fe Specification (%)", required=True, default=0, digits=0 )
	moisture_spec = fields.Float( string="Moisture Specification (%)", required=True, default=0, digits=0 )
	mineral_spec = fields.Float( string="SiO2/MgO Specification", required=True, default=0, digits=0 )