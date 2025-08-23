{
    'name': 'Taler-Odoo Payment System',
    'version': '1.0',
    'author': 'Nemael',
    'category': 'Custom',
    'summary': 'Taler payment system for Odoo',
    'depends': ['base'],
    'data': [
        'data/tops_welcome_data.xml',
        'security/ir.model.access.csv',
        'views/welcome_view.xml',
        'views/order_view.xml',
        'views/res_config_settings_view.xml'
        ],
    'installable': True,
    'application': True,
}
