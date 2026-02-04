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

- Add a tutorial on how to translate in the README
  - It should be short, explain that you should copy the .pot file in the i18n folder, and rename it to the language they want to translate to + ".po", and then translate each line
  - Explain that they can use the "fr.po" file as example

- For the verification of milestone accessibility, if that makes sense and is easily comprehensible, I could make a video recording of a screen reader reading my add-on

- Check if the accessibility itself is translated (see if aria-label are translated)


Translation issues:
- Invoice the txt above QR Code is in english
- Invoice preview is in english
- Test mode warning is in english
- Copy all the original lines from fr.po to tops.pot, to make sure the two files are in sync

- Add more tests, for the refunds for example

- For the translations, add _() to all the strings, to make sure that all the strings are in the .po file, for example the error messages are not there.

- Translation:
  - Do an overhaul of the README.md file before handing it to my translator
  - Edit the pictures of the README file, to make the foundation for the README_FR file

- UI explanation:
  - Take screenshots of all the pages that I modified
  - Add red squares on each relevant UI element
  - Assign a number to each square
  - Below the picture, explain for each square what UI element it is

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

- Implement the proposed changes of repository folders, move every directory file currently in the root, into a "payment_taler" folder, to change the add-on name.
  - I will need to change the installation instructions if I go through this change
    - Maybe the installation with `git clone` will not be working anymore
  - Also double-check that the uninstallation goes smoothly

- Instead of using a "main" branch
  - Use an "18.0" branch (double-check the branch name on the OCA modules)
  - This will be useful when 18.0 is fully released, and I can make a "19.0" branch, with 19.0-specific fixes, for the update compatibility.

- Next steps:
  - Once the whole software is ready for the translation and sent over, merge the code right away
  - Implement the rolling releases, it will be useful for the proposed directory changes, and other small fixes.
    - For auto releases, Codeberg implements auto zipping, I believe:
      - https://docs.codeberg.org/git/using-tags/#creating-tags-and-releases

- Before finishing the translation milestone, do a runaround of all the features
  - First in English
  - Then in French

- When the tutorial for the test mode is finished being translated, Check that the link in the test mode warning does point to the tutorial in French, and does not lead to a 404.

- When I finish the software translation, merge it to the main branch already, and make a tag "software_translation"

- Next steps:
  - Finish software translation
  - Check the upload requirements on the OCA and Odoo appstore
  - See if I can send my add-on for approval, and if I want to do it already
    - Before sending it, see if I can implement the changes from issue#18

- For the Odoo store publishing:
  - Add a folder payment_taler to the root of my repository
  - Guidelines are here: https://apps.odoo.com/apps/vendor-guidelines
  - See if I can easily setup the `live_test_url` field in the manifest
  - Add the `support` field in the manifest, with my support URL 
