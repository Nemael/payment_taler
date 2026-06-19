<!--
SPDX-FileCopyrightText: 2025 Mael Panouillot <panouillot.mael@gmail.com>

SPDX-License-Identifier: LGPL-3.0-or-later
-->

- Update the add-on for Odoo 19

- Translate the README + documentation in French
  - Redo the tutorial pictures in French as well

- Improve the taler_api_methods file to make it a mixin
  - For help making it work, ask the OCA

- When the add-on is updated for Odoo 19, change the last line in `TOPS:` section (in the readme probably?)

- Make instructions in the documentation on how to build the docs
  - Explain how to add to the docs, edit the docs, and build the docs
  - Use this command to build the documentation: sphinx-build -M html sourcedir outputdir
    - Or `make html`

- In the documentation, add a section "How to update translation after a change in documentation"
  - That explains how to re-generate the .po files, and tells you what you should translate again
  - This is the same thing that I will have to do when I update documentation after I add the partial refund feature, and I update my addon for Odoo 19.

- Remove the UI-Explanation.md file once the new documentation is complete

- Add link to french documentation in section "Project/Translation Status/Translation & available languages"

- Remove what steps were completed from "Project/How to contribute/How to contribute"

- Edit the "this page is also available in French here" from the documentation, to say "this documentation is also available in french here"

- Add the link to the new documentation in the README file.
- 
- Add the link to the new documentation page about making contributions in the README file.
