# SPDX-FileCopyrightText: 2025 Mael Panouillot <panouillot.mael@gmail.com>
#
# SPDX-License-Identifier: LGPL-3.0-or-later

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
        'views/res_config_settings.xml'
        ],
    'installable': True,
    'application': True,
}
