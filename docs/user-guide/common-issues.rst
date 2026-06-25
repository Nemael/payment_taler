.. SPDX-FileCopyrightText: 2025 Mael Panouillot <panouillot.mael@gmail.com>
.. SPDX-License-Identifier: LGPL-3.0-or-later

Common issues
=============

.. contents:: On this page:
   :local:

Tech support
~~~~~~~~~~~~

If you are encountering any issues with the add-on, please don’t
hesitate to either:

- Open a thread in this forum category https://ich.taler.net/c/integrations/odoo/29 (You can ping me as well, @Nemael). Please explain your issue in detail.
- Open an issue on the Codeberg repository https://codeberg.org/Nemael/tops/issue. Please explain in details the issue you are encountering.



The ``Check URL validity`` button is showing an error
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- This button checks that the chosen Taler merchant is valid and
  supports the same currencies that you are using. If your Taler
  provider accepts a currency not supported by the Taler merchant, an
  error will be raised.

  - The error message will show any discrepancies, and the accepted
    currencies on both sides.

- To change the currencies you’d like to support with Taler, go to the
  ``Configuration`` tab in the payment provider, and navigate to
  ``Availability -> Currencies``.

  - This change will be overwritten when you restart the Odoo server.
  - For a more permanent change, you can edit the ``const.py`` file at
    the root of this add-on, and comment/uncomment the currencies that
    you want to set as Taler configuration.
  - ``const.py`` is loaded at server start.

.. note::
   Because KUDOS is an imaginary currency, you will not find it in Odoo's currency list.
