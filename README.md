# TOPS: Taler-Odoo Payment System

TOPS is a currently in-development odoo add-on.

This Odoo add-on allows users to pay with Taler, akin to 18 other existing payment integrations in Odoo.
It is developed using the Odoo Framework, in Javascript and Python. The module integrates into and increase functionality of other existing Odoo modules (ticket sale, online shopping, invoices, etc.).

Installing the module allows merchants to offer their customers to use their Taler wallet to pay, allowing users to choose a payment system that respects their privacy.

Once finished, this add-on will be made available on the Odoo Apps store https://apps.odoo.com/apps

This work is published under license LGPL-3.0-or-later


How to install and use this add-on in your Odoo installation:
- Download this repository as .zip
- Extract the code
  - Preferably in {your odoo install}/custom_addons
    - Make sure that the "tops" directory in "custom_addons"
  - Note: the code can be extracted anywhere, but it's easier to have it within the Odoo folder
- 
- In the line you use to start Odoo, add the argument "--addons-path=./addons,./custom_addons"
  - Such as: ./odoo-bin --addons-path=./addons,./custom_addons -u tops -d odoo18_tops_0.1.1.1
- 
- In Odoo, go to the "Apps" section in the app switcher (top-left)
- Click "Update Apps List" on the top bar
- Search for the add-on "Taler-Odoo Payment System"
- Install it from there
- 
- Once installed, you just have to set the vendor url and the password
- (The following steps are subject to change, please reach out to me if they are innacurate)
- Go to the Taler-Odoo Payment System using the app switcher (top-left)
- Click "Configuration" on the top bar and then "Settings"
- In this settings page that opened, set the Taler Merchant URL you'd like to use, and the corresponding password
  - Default values for testing can be "https://backend.demo.taler.net/instances/sandbox" and "sandbox"
  - The "secret-token" section can be left blank
- 
- You are now finished with the installation and can start using the add-on
