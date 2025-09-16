<!--
SPDX-FileCopyrightText: 2025 Mael Panouillot <panouillot.mael@gmail.com>

SPDX-License-Identifier: LGPL-3.0-or-later
-->

# TOPS: Taler-Odoo Payment System

TOPS is a currently in-development add-on for Odoo.

This Odoo add-on allows users to pay with Taler, similar to other existing payment integrations in Odoo.
It is developed using the Odoo Framework, in Javascript and Python. The module integrates into and increase functionality of other existing Odoo modules (ticket sale, online shopping, invoices, etc.).

Installing this module allows merchants to offer their customers to use their Taler wallet to pay, allowing users to choose a payment system that respects their privacy.

Once finished, it will be made available on the Odoo Apps store https://apps.odoo.com/apps

---

## Installation steps on an already-existing Odoo installation

- Clone this repository
  - Preferably in {your Odoo install}/custom_addons
    - Make sure that the "tops" directory in "custom_addons"
  - Note: the code can be extracted anywhere, but it's easier to have it in the Odoo folder
- In the command line you use to start Odoo, add the argument `--addons-path=./addons,./custom_addons`
  - Such as: `./odoo-bin --addons-path=./addons,./custom_addons -u tops -d odoo18_tops_0.1.1.1`
- In Odoo, go to the `Apps` section in the app switcher (top-left button)
- Click `Update Apps List` on the top bar
- Search for the add-on Taler-Odoo Payment System`
- Install it from there
- Once installed, you just have to set the vendor url and the password
- (The following steps are subject to change, please reach out to me if you find them inaccurate)
- Go to `Taler-Odoo Payment System` using the app switcher (top-left button)
- Click `Configuration` on the top bar and then `Settings`
- In this settings page that opened, set the Taler Merchant URL you'd like to use, and the corresponding password
  - Default values for testing purposes can be `https://backend.demo.taler.net/instances/sandbox` and `sandbox`
  - The `secret-token` section can be left blank
- You are now finished with the installation and can start using the add-on
- Note: to update the add-on, you can pull from the repository you cloned earlier

---

## Change settings using CLI
- Run the Odoo CLI shell by adding `shell` to your original command line to start Odoo
  - Such as `./odoo-bin shell --addons-path=/addons/media/sf_VMSharedFolders/custom_addons -u tops -d odoo18_tops_0.1.1.1`
- Run these commands to edit the setting you want to set. You can use `get_params` to print the current value, and `set_params` to set a new value.
  - `env['ir.config_parameter'].set_param('tops.merchant_url', 'https://backend.demo.taler.net/instances/sandbox/')`
  - `env['ir.config_parameter'].set_param('tops.password', 'https://backend.demo.taler.net/instances/sandbox/')`
- ![#f03c15](https://placehold.co/15x15/f03c15/f03c15.png) `#f03c15`IMPORTANT: Commit the changes to the database before closing the shell instance and restarting Odoo
  - `env.cr.commit()`
  - `exit()`

---

## Folder structure

This add-on uses a quite standard folder structure
- `data` contains the setup data that is processed when someone installs the add-on.

- `Devlog` is a text compendium of the posts I am making on the ICH forum

- `models` contains my Odoo models. There are:
  - `Welcome` model (which contains method to interact with Taler)
  - `Order` model (which allows for the storing an management of orders)
  - `res_config_settings` model (which allows to store and edit settings for the add-on, and is currently used to set up Taler connection data)

- `static` contains logo data and other assets I would need to use in the future

- `test` is for unit testing, is currently unused

- `utils` contains utility methods (such as logging)

- `views` contains a view for each of my models.

---

## Funding

This project is funded through [NGI TALER Fund](https://nlnet.nl/taler), a fund established by [NLnet](https://nlnet.nl) with financial support from the European Commission's [Next Generation Internet](https://ngi.eu) program. Learn more at the [NLnet project page](https://nlnet.nl/project/TALER-Odoo-module).

[<img src="https://nlnet.nl/logo/banner.png" alt="NLnet foundation logo" width="20%" />](https://nlnet.nl) 

---

## Licensing

This work is published under license LGPL-3.0-or-later
