.. SPDX-FileCopyrightText: 2025 Mael Panouillot <panouillot.mael@gmail.com>
.. SPDX-License-Identifier: LGPL-3.0-or-later

How to Contribute
=================

.. contents:: On this page:
   :local:

How to contribute
-----------------

Contributions to the Taler payment integration are always welcome!

- To make a contribution:

  - Fork this repository (https://codeberg.org/Nemael/tops/),
  - Clone the fork on your local machine,
  - Create a new branch,
  - Make your changes in the code,
  - Commit your changes,
  - Push to your fork,
  - Open a pull request on the original TOPS repository
    (https://codeberg.org/Nemael/tops/).

- Some features that may need further work:

  - Add more translations to help make the add-on more accessible (see
    :ref:`here <how-to-add-a-translation>` for a guide on how to add a
    translation).
  - Maintain the add-on up to date for future Odoo releases (Odoo 20 is
    just around the corner).

.. _how-to-add-a-translation:

How to add a translation to the Odoo module
-------------------------------------------

- If you would like to add a translation to the module, the process is
  rather simple:

  - The file ``i18n/payment_taler.pot`` `available
    here <https://codeberg.org/Nemael/tops/src/branch/18.0/payment_taler/i18n/payment_taler.pot>`__
    is the base translation file, with all the strings of text stored in
    it.
  - Copy this file’s content in a new file ``{New language}.po``, such
    as ``fr.po``.
  - In this new file, translate all the strings of text that you would
    like to translate. You can use ``fr.po`` `available
    here <https://codeberg.org/Nemael/tops/src/branch/18.0/payment_taler/i18n/fr.po>`__
    as a guide on how to format the translation.
  - Once complete, you can re-make your Odoo test database, and change
    your user’s language to the added translation’s language. The
    translation you made should appear on Odoo.
  - If you are encountering any issues, please open a thread in this
    forum category https://ich.taler.net/c/integrations/odoo/29 (You can
    ping me as well, @Nemael). Please specify that you are doing a new
    translation and for which language.

How to update and build the documentation
------------------------------------------

- The documentation is made in ``.rst`` format, and built using Sphinx. You can follow the Sphinx guides or other ``.rst`` guides to improve the documentation.
- To add information to the documentation, you need to edit the files in ``docs/``.

  - There are three directories corresponding to each documentation section (``user-guide``, ``project``, ``ui-explanation``).

- After making your changes, you need to rebuild the documentation, to obtain the updated html files.

  - You need to build the documentation for a specific language:

    - ``sphinx-build -D language=en -b html . _build/html/en`` will build in English.
    - ``sphinx-build -D language=fr -b html . _build/html/fr`` will build in French.
    - If the above do not work for any reason, you can use ``make html`` to build a barebone version of the documentation.

- When the documentation is built, you can find the resulting files in ``docs/_build/html/{2-letters target language}``.

  - You can open the root index.html in your browser to view the documentation.

How to update the translation of the documentation
--------------------------------------------------

- The translation of the documentation is based on ``.pot`` files, which are extracted from the existing ``.rst`` files, converted into a language's ``.po`` files, translated and then compiled.
- This is a standard process, you can find online guides on how to work with ``.po`` files.

  - After editing the ``.rst`` files, you have extract the ``.pot`` files for them to contain the changes you made: ``sphinx-build -b gettext . _build/gettext``.

  - Once you have the new ``.pot`` files, you have to re-make the language-specific ``.po`` files.
  - One ``.pot`` file will be created for each ``.rst`` file.

    - ``sphinx-intl update -p _build/gettext -l {2-letters target language}``.
    - Example: ``sphinx-intl update -p _build/gettext -l fr``.

  - Once you have the ``.po`` files, you can translate line-per-line the content of each ``mgsid`` in the ``.po`` files.
  - When this is complete, you can build the documentation for the chosen language.

    - ``sphinx-build -D language={2-letters target language} -b html . _build/html/{2-letters target language}``.
    - Example: ``sphinx-build -D language=fr -b html . _build/html/fr``.

  - The resulting files can be found in directory ``docs/_build/html/{2-letters target language}``.
  - To update the documentation on ReadTheDocs, push the documentation changes on the main branch of the repository (branch ``19.0``).
