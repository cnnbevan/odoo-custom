from odoo import models, fields

class MyModel(models.Model):
    _name = 'my.module'
    _description = 'My Model'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
{
    'name': 'My Module',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'A simple example module for Odoo',
    'author': 'Your Name',
    'website': 'https://www.example.com',
    'depends': ['base'],
    'data': ['views/my_model_view.xml'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
