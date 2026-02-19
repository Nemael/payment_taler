<!--
SPDX-FileCopyrightText: 2025 Mael Panouillot <panouillot.mael@gmail.com>

SPDX-License-Identifier: LGPL-3.0-or-later
-->

- Update the add-on for Odoo 19

- See if my add-on has "iframe support", such as what is shown in the features for this repo https://github.com/Kashier-payments/Kashier-Odoo-Payment-Add-on

- Translate the README in French
  - Redo the tutorial pictures in French as well

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

- Translation:
  - Do an overhaul of the README.md file before handing it to my translator
  - Edit the pictures of the README file, to make the foundation for the README_FR file

- UI explanation goals:
  - Take screenshots of all the pages that I modified
  - Add red squares on each relevant UI element
  - Assign a number to each square
  - Below the picture, explain for each square what UI element it is

- Automated release goals:
  - Zip file available
  - Auto version bumping
  - Auto creation of artifact (zip file)
  - Auto tagging in git

- Security report goal:
  - List all the outgoing request
    - Parameters, payloads, headers, response, return values
  - Explain how I use tokens to send payloads

- When the tutorial for the test mode is finished being translated, Check that the link in the test mode warning does point to the tutorial in French, and does not lead to a 404.

- For the Odoo store publishing:
  - Add a folder payment_taler to the root of my repository
  - Guidelines are here: https://apps.odoo.com/apps/vendor-guidelines
  - See if I can easily setup the `live_test_url` field in the manifest
  - Add the `support` field in the manifest, with my support URL

- Change the installation instructions to fit the new directory payment_taler


- Re-read the README file and make it better, and make sure all the links and screenshots are correct.

- Make a post on the ICH to thank Jans for the QA and the info on how to standardize my code

- When the addon is online on both odoo and oca shops, add the links to section `TOPS:` in the README
  - And add in the installation instructions how to install them from these respective websites, in `Install the add-on` section

- Remove `current status` section

- When the add-on is updated for Odoo 19, change the last line in `TOPS:` section

- When I do the 1.0 release, make sure that the add-on manifest.py version is also `18.1.0.0`
