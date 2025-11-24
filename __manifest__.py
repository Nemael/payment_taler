# SPDX-FileCopyrightText: 2025 Mael Panouillot <panouillot.mael@gmail.com>
#
# SPDX-License-Identifier: LGPL-3.0-or-later

{
    'name': 'Taler-Odoo Payment System',
    'version': '1.0',
    'author': 'Nemael',
    'category': 'Custom',
    'summary': 'Taler payment system for Odoo',
    'depends': ['base', 'payment', 'website', 'website_sale', 'account'], #website, website_sale and account might not be required, I have added them from another example, check later if they are required.
    'data': [
        'data/tops_welcome_data.xml',
        'data/taler_payment_provider_data.xml',
        'data/taler_payment_method_data.xml',
        'security/ir.model.access.csv',
        'views/welcome_view.xml',
        'views/order_view.xml',
        'views/res_config_settings_view.xml',
        'views/taler_payment_view.xml'
    ],
    'installable': True,
    'application': True,
}
