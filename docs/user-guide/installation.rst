.. SPDX-FileCopyrightText: 2025 Mael Panouillot <panouillot.mael@gmail.com>
.. SPDX-License-Identifier: LGPL-3.0-or-later

Installation
=============

.. contents:: On this page:
   :local:

Install or update the add-on on an already-existing Odoo installation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- There are multiple options to install this add-on

  - Install from the Odoo Apps store

    - Navigate to `the module’s apps.odoo.com
      page <https://apps.odoo.com/apps/modules/18.0/payment_taler>`__
    - Click on ``Deploy on Odoo.sh``
    - The add-on should be now installed on your Odoo.sh instance

  - Manually add the code yourself in your Odoo install (Multiple
    options)

    - First, download the add-on code with either of these 3 methods

      - Download the latest version from the releases
        (https://codeberg.org/Nemael/tops/releases)

        - Downloading the latest release provides the most stable and
          tested code

      - Download the add-on from `the apps.odoo.com
        page <https://apps.odoo.com/apps/modules/18.0/payment_taler>`__
      - Clone this repository (git clone
        https://codeberg.org/Nemael/tops.git)

        - Preferably clone it in ``{your Odoo install}/custom_addons``

          - Ensure that the ``tops`` directory is in ``custom_addons``
          - Cloning the repository provides the most up-to-date code,
            and you can simply use ``git pull`` to obtain the latest
            updates. However, the code obtained this way might be
            unstable

    - Then move the files to your Odoo folder

      - Extract the zip file to ``{your Odoo install}/custom_addons``
      - Ensure that the ``tops`` or ``payment_taler`` directory is in
        ``custom_addons``

.. note::
   Note: the add-on code can be stored anywhere, but it’s easier store it within the Odoo folder

- In the command line you used to start Odoo, specify the path to this
  add-on by adding the argument
  ``--addons-path=./addons,./custom_addons/tops``

  - Such as:
    ``./odoo-bin --addons-path=./addons,./custom_addons/tops -u tops -d odoo18_tops_0.1.1.1``

- In Odoo, go to the ``Apps`` section in the app switcher (top-left
  button)
- Click ``Update Apps List`` on the top bar
- Search for the add-on ``Taler-Odoo Payment System``
- Click on the add-on, and press ``Activate`` or ``Install`` to complete
  this step

.. note::

   To update the add-on, first update the code using the same way that
   you first downloaded it, then restart the server and finally click
   ``Upgrade`` on the add-on page


Uninstall the add-on
~~~~~~~~~~~~~~~~~~~~

- To uninstall the add-on, you have to go to the ``Apps`` app on Odoo.
- Search for, and go to the ``Taler-Odoo Payment System`` add-on.
- Click ``Uninstall``, the add-on should be uninstalled.

.. note::
  If you have made any transactions using Taler with this add-on, you will not be able to uninstall it.

- You can reinstall the add-on at a later time.
- If you added a payment method record for the point of sale app (:ref:`see the related section for more information <point-of-sale-payment-configuration>`), complete the following steps as well:

  - Go to the ``Point of Sale`` app, and navigate to
    ``Configuration/Payment Methods``.
  - Click on the ``Taler`` record you created when setting up the point
    of sale payment system, it should be highlighted in red because the
    payment provider is not available anymore.
  - Click on the gear at the top, and then either ``Archive`` (better
    for data conservation) or ``Delete`` (more risky because you might
    lose track of some payments)
  - On the top bar, go to ``Configuration -> Point of Sales``.
  - Select a point of sale that you made Taler payments available for.
  - Click on ``More settings: Configurations > Settings``, which will
    lead you to the point of sale’s settings page.
  - In Payment -> Payment Methods, remove the Taler payment method.

    - Do this step for every point of sale you made Taler payments
      available for.
