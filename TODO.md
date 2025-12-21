<!--
SPDX-FileCopyrightText: 2025 Mael Panouillot <panouillot.mael@gmail.com>

SPDX-License-Identifier: LGPL-3.0-or-later
-->

- Make a dedicated email address for this add-on, to put on the addon shops' webpage, to receive emails for support and such

- In the readme, tell which version of Odoo the addon is working for, and it was tested for

- For the payment "Test Mode", there is a radio button in Odoo's interface to activate "Test Mode" for the payment method
  - Credentials are integrated as well
  - It will take a lot of work to make the existing sysem work, but this is a great base to start

- Add to the readme that users are advised to create a "Taler" payment journal to record taler payments

- See if my add-on has "iframe support", such as what is shown in the features for this repo https://github.com/Kashier-payments/Kashier-Odoo-Payment-Add-on

- Write in the README that, to sell tickets, you have to install the "event" module, and then go to the settings for events, and check the "online ticketing", and maybe the pos side as well
  - Note, to have the proper ticketing system, you might need to install the python module pycairo:
    - 1. sudo apt install libcairo2-dev
    - 2. pip install rlPyCairo

- Add in the thanks section in the README
  - OCA with all their repositories
  - GNU Taler
  - Petites Singularite for the support on the ICH forum, where I could share my progress and discussions when making this software
  - The Kashier and Sadad as examples on github (add a link to their)

- When I do translation, don't forget to do translation of the .xml files
  - And the readme files as well

- For the refund system integration, use the field "refund_delay?: RelativeTime;" in the order creation payload
  - See https://docs.taler.net/core/api-merchant.html#creating-orders

- Add to the README file that, if there is an issue, they can open an issue on the git repository [repository_url]

- Add "How to remove the addon" in the guides
  - Show how to proceed with the removal on the app portal
  - Show, for pos, how to remove the record manually added
  - Show, for pos, if needed, how to remove the added payment option from the setting of a pos store

- Translate the README in French
  - Redo the tutorial pictures in French as well

- After all the code cleanup is finished, and the only todos left are the ones to do at later steps of the project, then I should make picture tutorials in the readme for
  - Activation of taler payment provider after installation
    - Including explanation on what to put in the fields such as merchant_url, password, etc
  - online ecommerce transaction completion
  - invoice creation focused on the qr code on invoice
    - plus maybe invoice reconciliation after payment through qr code? In that case I'll have to read the qr code using the addon
  - invoice creation + payment on the online portal
  - ticket sale process, with the info from the readme or TODO on how to install the ticket addon
  - pos setup for the online payment provider
  - pos payment process with qr code for the user

