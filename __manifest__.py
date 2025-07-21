{
    'name': 'Taler-Odoo Payment System',
    'version': '1.0',
    'author': 'Nemael',
    'category': 'Custom',
    'summary': 'Taler payment system for Odoo',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/student_view.xml',
        'views/res_config_settings.xml'
        ],
    'installable': True,
}
