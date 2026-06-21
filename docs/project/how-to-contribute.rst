.. SPDX-FileCopyrightText: 2025 Mael Panouillot <panouillot.mael@gmail.com>
.. SPDX-License-Identifier: LGPL-3.0-or-later

How to Contribute
=================

.. contents:: On this page:
   :local:

How to contribute
-----------------

Contributions to the Taler payment integration are always welcome!

- To make a contribution:

  - Fork this repository (https://codeberg.org/Nemael/tops/)
  - Clone the fork on your local machine
  - Create a new branch
  - Make your changes in the code
  - Commit your changes
  - Push to your fork
  - Open a pull request on the original TOPS repository
    (https://codeberg.org/Nemael/tops/)

- Some features that need further development:

  - Add more translations to help make the add-on more accessible (see
    :ref:`here <how-to-add-a-translation>` for a guide on how to add a
    translation).
  - Implement partial refunds for customers.
  - Update the add-on for Odoo 19.
  - Maintain the add-on up to date for future Odoo releases (Odoo 20 is
    just around the corner).
  - Improve the README file.

    - Split it in multiple different file, for an easier navigation.

  - Translate the documentation + README in French

.. _how-to-add-a-translation:

How to add a translation
------------------------

- If you would like to add a translation to the module, the process is
  rather simple:

  - The file ``i18n/payment_taler.pot`` `available
    here <https://codeberg.org/Nemael/tops/src/branch/18.0/payment_taler/i18n/payment_taler.pot>`__
    is the base translation file, with all the strings of text stored in
    it.
  - Copy this file’s content in a new file ``{New language}.po``, such
    as ``fr.po``
  - In this new file, translate all the strings of text that you would
    like to translate. You can use ``fr.po`` `available
    here <https://codeberg.org/Nemael/tops/src/branch/18.0/payment_taler/i18n/fr.po>`__
    as a guide on how to format the translation.
  - Once complete, you can re-make your Odoo test database, and change
    your user’s language to the added translation’s language. The
    translation you made should appear on Odoo.
  - If you are encountering any issues, please open a thread in this
    forum category https://ich.taler.net/c/integrations/odoo/29 (You can
    ping me as well, @Nemael). Please specify that you are doing a new
    translation and for which language.
