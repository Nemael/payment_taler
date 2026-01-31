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

- Translate the README in French
  - Redo the tutorial pictures in French as well

- Edit the two links in the test mode tooltip
  - Make sure to add the link to the merchant test mode tutorial
  - section that says "which is very likely" in the text, check if all Taler merchants will accept Kudos, if it is mandatory or optional, and add a link if relevant.


- Find a solution to this predicament:
  - The milestone i18n depends on the documentation
  - The milestone documentation depends on the addon being on a storefront (OCA + Odoo)
  - The milestone of the addon being on a storefront depends on the i18n being completed
  - Solution:
    - Do every documentation needed except the "install from an online shop"
    - Do the translation for it all
    - Submit the add-ons for publication on =

- Improve the taler_api_methods file to make it a mixin
  - For help making it work, ask the OCA

- See if there is a way to reduce the image size in the README
