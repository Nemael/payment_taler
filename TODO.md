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

- For the translations, add _() to all the strings, to make sure that all the strings are in the .po file, for example the error messages are not there.

- Translation: edit the pictures of the README file, to make the foundation for the README_FR file

- Make a translation for the email template and email description and email subject

- Add to the bottom of the readme page, an email address for support (see what I can do to create this email address)

- Shorten the time that a token is valid, for security reasons

- Automated release goals:
  - Zip file available
  - Auto version bumping
  - Auto creation of artifact (zip file)
  - Auto tagging in git

- Security report goals:
  - List all the outgoing request
    - Parameters, payloads, headers, response, return values
  - Explain the use of tokens to send payloads

- Security checks:
  - Talk about the meetings I had with cybersecurity professionals

- For the translation milestone, see if I can delete the field "SUPPORTED_LOCALES" from the file const.py.
  - I think it is not used





- Add the devlog link to the readme.md

- Check that there are dots at the end of every sentence in the README
