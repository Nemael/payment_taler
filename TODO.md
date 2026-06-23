<!--
SPDX-FileCopyrightText: 2025 Mael Panouillot <panouillot.mael@gmail.com>

SPDX-License-Identifier: LGPL-3.0-or-later
-->

- Remove this TODO when I finish the work on this MoU

- Update the add-on for Odoo 19

- Translate the README + documentation in French
  - Redo the tutorial pictures in French as well

- Improve the taler_api_methods file to make it a mixin
  - For help making it work, ask the OCA

- When the add-on is updated for Odoo 19, change the last line in `TOPS:` section (in the readme probably?)

- Add instructions in the documentation on how to build the docs
  - Explain how to add to the docs, edit the docs, and build the docs
  - Use this command to build the documentation: sphinx-build -M html sourcedir outputdir
    - Or `make html`

- Add instructions in the documentation on how to update the docs and the translation:
  - Rebuild the .pot files: sphinx-build -b gettext . _build/gettext
  - Remake the language-specific .po files: sphinx-intl update -p _build/gettext -l fr
  - And to rebuild the docs:
    - sphinx-build -D language=en -b html . _build/html/en
    - sphinx-build -D language=fr -b html . _build/html/fr



- In the documentation, add a section "How to update translation after a change in documentation"
  - That explains how to re-generate the .po files, and tells you what you should translate again
  - This is the same thing that I will have to do when I update documentation after I add the partial refund feature, and I update my addon for Odoo 19.

- Remove the UI-Explanation.md file once the new documentation is complete

- Add link to french documentation in section "Project/Translation Status/Translation & available languages"

- Remove what steps were completed from "Project/How to contribute/How to contribute"

- Edit the "this page is also available in French here" from the documentation, to say "this documentation is also available in French here"

- Add the link to the new documentation in the README file.

- Add the link to the new documentation page about making contributions in the README file.

- Check if I can fix why the repository is non-compliant with REUSE (See licensing section at end of README)

- When I update the add-on to Odoo 19, check all the flows individually if they are working fine

- Add in the partial refunds documentation that you can do multiple partial refunds if needed, and the customer will receive multiple emails with QR Codes
  - Verify this in my own flow as well.

- Update the unit tests for the partial refunds

- Run the unit tests after the Odoo 19 upgrades

- Make sure that the error message "Refund amount exceeds original payment." is translated

- Make French version of the pictures for UI-Explanation documentation

- When the documentation is uploaded to ReadTheDocs, add the links that are needed in the README.md

- Make a new release when the MoU is finished and I did my last commit for now

- When translation is finished, complete the translation of the readme.md

- See why woodpecker does not do the pipeline checks

- Odoo 19 issues:
  - The yellow text in the payment provider is not displaying properly. Same for the test mode yellow text
  - Fix the unit tests

- Make the github mirror

- Upload docs to ReadTheDocs
