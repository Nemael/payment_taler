.. SPDX-FileCopyrightText: 2025 Mael Panouillot <panouillot.mael@gmail.com>
.. SPDX-License-Identifier: LGPL-3.0-or-later

Technical Information
=====================

.. contents:: On this page:
   :local:

Change settings using CLI
-------------------------

- To change Odoo settings using CLI, run the Odoo CLI shell by adding
  ``shell`` to your original command line to start Odoo.

  - Such as
    ``./odoo-bin shell --addons-path=./addons,{custom_addons_path}/tops -u payment_taler -d odoo18_tops_0.1.1.1``

- Run these commands to edit the settings. You can use ``get_params`` to
  print the current value, and ``set_params`` to set a new value:

  - ``env['ir.config_parameter'].set_param('payment_taler.taler_merchant_url', 'https://backend.demo.taler.net/instances/sandbox/')``
  - ``env['ir.config_parameter'].set_param('payment_taler.taler_merchant_password', 'sandbox')``


.. warning::
   You need to commit the changes to the database before closing the shell instance and restarting Odoo:

  - ``env.cr.commit()``
  - ``exit()``


Editing rights to the payment provider settings
-----------------------------------------------

- As with other payment providers, Odoo users will have limited access to the Taler payment provider settings.
- Only user that belong in the ``base.group_system`` user group will be able to access and modify the Taler payment provider settings.


Run unit tests
--------------

- To run unit tests on a new db, use this command:

  - ``./odoo-bin --addons-path=./addons,{custom_addons_path}/tops --test-enable -d test_db_2 -i payment_taler --stop-after-init --test-tags taler``

    - The db name after -d is arbitrary and can be replaced by any other
      names.

- In the results logs, you should expect to see
  ``odoo.tests.result: 0 failed, 0 error(s) of x tests when loading database``.

  - x is the number of unit tests, currently 11.


Folder structure
----------------

This add-on uses a standard folder structure:

- ``controllers`` contains the controllers used by the add-on.
- ``data`` contains setup data that is processed when someone installs the add-on, as well as email templates.
- ``i18n`` contains the data for localization and translation.
- ``models`` contains the Odoo models. There are 4 models:

  - ``taler_api_method``, which contains the methods used to communicate to the Taler merchant API.
  - ``taler_invoicing``, which contains the methods used when creating invoices with Taler.
  - ``taler_provider``, which contains the methods used by the Taler payment provider.
  - ``taler_transaction``, which contains the methods used to complete a transaction with Taler.

- ``security`` contains the (unused) ``ir.moder.access.csv`` file to manage access rights.
- ``static`` contains logo data and other image assets for the add-on.
- ``tests`` contains unit tests for this project.
- ``utils`` contains utility methods (such as logging).
- ``views`` contains the views used for the models.

