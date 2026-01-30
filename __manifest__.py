# SPDX-FileCopyrightText: 2025 Mael Panouillot <panouillot.mael@gmail.com>
#
# SPDX-License-Identifier: LGPL-3.0-or-later

{
    'name': 'Taler-Odoo Payment System',
    'version': '1.0',
    'author': 'Nemael',
    'category': 'Accounting/Payment Providers',
    'summary': 'Free Open-Source Software - Integration of the Taler payment system in Odoo. Works for Invoicing, ECommerce online payments and Point-of-sale. See https://codeberg.org/Nemael/tops for the code repository',
    'depends': ['base', 'payment', 'website', 'website_sale', 'account', 'point_of_sale'],
    'data': [
        'views/taler_payment_template.xml',
        'views/taler_provider_view.xml',
        'views/taler_invoice_view.xml',
        'data/taler_payment_method_data.xml',
        'data/taler_payment_provider_data.xml',
        'data/email_refund_template_data.xml',
        'security/ir.model.access.csv' #The ir security file is not actually needed for now, but it stays included in case it is needed later.
    ],
    'post_init_hook': 'post_init_hook',
    'uninstall_hook': 'uninstall_hook',
    'installable': True,
    'application': True,
    'license': 'LGPL-3' #Complete license is "LGPL-3.0-or-later", see on top of any files in the module.
}
