<!--
SPDX-FileCopyrightText: 2025 Mael Panouillot <panouillot.mael@gmail.com>

SPDX-License-Identifier: LGPL-3.0-or-later
-->

- Make a dedicated email address for support on this add-on, to put on the addon shops' webpage, to receive emails for support and such

- In the readme, explain which version of Odoo the addon is confirmed to be working for, and it was tested for

- See if my add-on has "iframe support", such as what is shown in the features for this repo https://github.com/Kashier-payments/Kashier-Odoo-Payment-Add-on

- When I do translation, don't forget to do translation of the .xml files
  - And the readme files as well

- For the refund system integration, use the field "refund_delay?: RelativeTime;" in the order creation payload
  - See https://docs.taler.net/core/api-merchant.html#creating-orders

- Translate the README in French
  - Redo the tutorial pictures in French as well


- Merchant test mode tasks:
  - For the payment "Test Mode", there is a radio button in Odoo's interface to activate "Test Mode" for the payment method
    - Credentials are integrated as well
    - It will take a lot of work to make the existing system work, but this is a great base to start
  - Make it so that the test mode make an order with kudos
  - Complete the order
  - Check that everything is ok
