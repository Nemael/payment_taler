# SPDX-FileCopyrightText: 2025 Mael Panouillot <panouillot.mael@gmail.com>
#
# SPDX-License-Identifier: LGPL-3.0-or-later

{
    'name': 'Taler-Odoo Payment System',
    'version': '1.0',
    'author': 'Nemael',
    'category': 'Custom',
    'summary': 'Taler payment system for Odoo',
    'depends': ['base', 'payment', 'website', 'website_sale', 'account', 'point_of_sale'], #website, website_sale and account might not be required, I have added them from another example, check later if they are required.
    'data': [
        'views/taler_payment_template.xml',
        'views/taler_provider_view.xml',
        'views/taler_invoice_view.xml',
        'data/taler_payment_method_data.xml',
        'data/taler_payment_provider_data.xml',
        'security/ir.model.access.csv'
    ],
    'installable': True,
    'application': True,
}
