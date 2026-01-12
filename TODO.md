<!--
SPDX-FileCopyrightText: 2025 Mael Panouillot <panouillot.mael@gmail.com>

SPDX-License-Identifier: LGPL-3.0-or-later
-->

- Make a dedicated email address for support on this add-on, to put on the addon shops' webpage, to receive emails for support and such

- In the readme, explain which version of Odoo the addon is confirmed to be working for, and it was tested for 
  - Test the addon in Odoo 19, and version 17, which are all the currently supported versions


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
  - Add some text when "test mode" is selected
    - A yellow square
    - Text saying "Test mode is selected, this mode allows you to test if the payment process with Taler and the currently chosen Merchant completes correctly. On the Odoo UI, all the payment UI will show the relevant payment information (amount, currency, etc), but the currency will automatically be swapped to "Kudos" right before sending the order to the Taler merchant. Kudos is the Taler testing currency, and is a currency that can be used for test transactions with your order wallet. See "LINK TO THE KUDOS DOCUMENTATION" for more information about Kudos. Add a link to the tutorial for merchant test mode on the codeberg repository as well. "WARNING TRIANGLE" Do not use this mode in production or with published items for sale"
  - Complete the order
  - Check that everything is ok

- Add more tutorials
  - One for the merchant test mode
    - Show the steps for a regular transaction, and then show "Website -> Reporting -> Online sales -> Bottom right month" to show the exchange that was confirmed
  - One for the refund system

- Edit the two links in the test mode tooltip
  - Make sure to add the link to the merchat test mode tutorial
  - section that says "which is very likely" in the text, check if all Taler merchants will accept Kudos, if it is mandatory or optional, and add a link if relevant.
