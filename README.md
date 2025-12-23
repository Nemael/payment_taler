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

## Tutorials

### Installation steps on an already-existing Odoo installation

- Clone this repository
  - Preferably in {your Odoo install}/custom_addons
    - Make sure that the "tops" directory in "custom_addons"
  - Note: the code can be extracted anywhere, but it's easier to have it in the Odoo folder
- In the command line you use to start Odoo, add the argument `--addons-path=./addons,./custom_addons`
  - Such as: `./odoo-bin --addons-path=./addons,./custom_addons -u tops -d odoo18_tops_0.1.1.1`
- In Odoo, go to the `Apps` section in the app switcher (top-left button)
- Click `Update Apps List` on the top bar
- Search for the add-on `Taler-Odoo Payment System`
- Install it from there
- Once installed, you have to set the Taler Merchant url and the password
- (The following steps are subject to change, please reach out to me if you find them inaccurate)
- Go to `Taler-Odoo Payment System` using the app switcher (top-left button)
- Click `Configuration` on the top bar and then `Settings`
- In this settings page that opened, set the Taler Merchant URL you'd like to use, and the corresponding password
  - Default values for testing purposes can be `https://backend.demo.taler.net/instances/sandbox` and `sandbox`
  - The `secret-token` section can be left blank
- You are now finished with the installation and can start using the add-on
- Note: to update the add-on, you can pull from the repository you cloned earlier


### How to setup the Taler payment provider
- Once the addon is installed from the Apps:
  - Go to the payment providers menu. It can be accessed in multiple ways:
    - Website -> Configuration -> eCommerce -> Payment Providers
    - Invoicing -> Configuration -> Online Payments -> Payment Providers
  - Either way you land here, this is the list of your currently available payment providers.
  - You will see a new payment provider in this list, "Taler", which is set as disabled for now
  - Click on the Taler payment provider
  - Click the "Enabled" radio button
  - In the "Credentials" tab, set the Taler Merchant URL you plan to use
    - After setting the URL, you can click the "Confirm the url validity" button to check if the entered URL is reaching a valid Taler Merchant, and that this merchant's accepted currencies are compatible with you TOPS available currencies
  - Then set your Taler Merchant Password, which will be used for API calls to the merchant
  - You can change the Taler fulfillment message, which will be shown on created Taler transactions, only on Taler side, not on Odoo side.
    - If you'd like to change the Odoo messages shown to the user after a payment using Taler, you can do so in the "Messages" tab on the same page
  - The default values are for the sandbox merchant server
    - URL: https://backend.demo.taler.net/instances/sandbox
    - Password: sandbox
- The initial setup is now complete and Taler payment will be available in all eCommerce and Invoicing apps.
![img.png](README_Pictures/Taler_provider_setting_complete.png)


---
## Flow examples and walkthrough

### Completes an eCommerce payment
- Once you have completed the Taler initial setup, customers can pay on your website
- To do so, they will open the shop and add any items in their cart
- During the checkout, they can now choose the "Taler" payment method
![img.png](README_Pictures/Taler_ecommerce_checkout.png)
- After clicking "Pay now", a new Taler order will be created on the merchant side, and the customer will be redirected to the Taler order, from which they can pay with any Taler wallet on their phone or web browser
![img.png](README_Pictures/Taler_ecommerce_wallet.png)
- Upon completion of the payment using their wallet, the customer will be redirected back to the Odoo instance, where it will show a confirmation that the payment was successfully processed
![img.png](README_Pictures/Taler_ecommerce_payment_processed.png)

### Creating an invoice that can be paid with Taler (TODO)
- Talk about the QR Code

### Paying an invoice online with Taler (TODO)
- This process is unrelated to the invoices created with Taler in the previous step
  - Any invoices can be paid online using Taler

### Tickets (TODO)
- Talk about the addon I have to install to make tickets available

### How to setup POS payment provider
- Preliminary steps
  - Only do this step if you have [setup Taler as a payment provider](#how-to-setup-the-Taler-payment-provider) first
  - Install the "Point of sale" Odoo addon
- Create the Point of Sale payment method
  - On the top bar, press Configuration -> Payment Methods
  - Create a new Payment Method
  - Call it "Taler" (You can call it anything but Taler is easier to remember)
  - Check "Online Payment"
  - Select "Taler" in the "Allowed Providers" field.
- Adding Taler to the point of sale (Make sure that the point of sale register is closed for this step)
  - On the top bar, press Configuration -> Point of Sale list
  - Select the point of sale you'd like to add Taler payment to (for test data, Clothes Shop is a good candidate)
  - Click on "More settings: Configurations > Settings", which will lead you to the point of sale's settings page
    - You can also access this page by going to Settings through the app switcher on the top right, then going to "Point of Sale" section, and selecting the point of sale that you would like to modify
  - In Payment -> Payment Methods, add the payment method you just created. It can be named "Taler", or any other custom name you chose
- You are now good to go, and can select your new payment provider when customer pay for an order.



### Paying on a Point of Sale (TODO)

### Going through the refund process
This flow is not implemented yet

---

### Change settings using CLI
- Run the Odoo CLI shell by adding `shell` to your original command line to start Odoo
  - Such as `./odoo-bin shell --addons-path=./addons,/media/sf_VMSharedFolders/custom_addons -u tops -d odoo18_tops_0.1.1.1`
- Run these commands to edit the setting you want to set. You can use `get_params` to print the current value, and `set_params` to set a new value.
  - `env['ir.config_parameter'].set_param('tops.merchant_url', 'https://backend.demo.taler.net/instances/sandbox/')`
  - `env['ir.config_parameter'].set_param('tops.password', 'https://backend.demo.taler.net/instances/sandbox/')`
- ![#f03c15](https://placehold.co/15x15/f03c15/f03c15.png) `#f03c15`IMPORTANT: Commit the changes to the database before closing the shell instance and restarting Odoo
  - `env.cr.commit()`
  - `exit()`

---

### Editing rights to the payment provider settings
- As with other payment providers, not all Odoo users on an instance can modify the Taler payment provider settings
- Only user that belong in the `base.group_system` user group will be able to access and modify the Taler payment provider settings.


---

### Uninstall the addon
- To uninstall the addon, you have to go to the `Apps` app on Odoo
- In there, search for and go to the `Taler-Odoo Payment System` addon
- Click `Uninstall`, the addon should be uninstalled
- You can reinstall the addon at a later time

---

## Folder structure

This add-on uses a quite standard folder structure
- `controllers` contains the controllers for the mvc structure of this project
- `data` contains setup data that is processed when someone installs the add-on.
- `Devlog` is a text compendium of the posts I am making on the ICH forum
- `LICENSES` contains the text of the licenses used in this project
- `models` contains my Odoo models. There are:
  - `taler_api_method`, which contains the methods used to communicate to the Taler merchant API
  - `taler_invoicing`, which contains the methods used when creating invoices with Taler
  - `taler_provider`, which contains the methods used by the Taler payment provider
  - `taler_transaction`, which contains the methods used to complete a transaction with Taler
- `README_Pictures`, which contains all the pictures shown in this README
- `static` contains logo data and other image assets for the addon
- `tests` contains unit tests for this project
- `utils` contains utility methods (such as logging)
- `views` contains a view for each of my models.

---

## Running unit tests
- To run unit tests on a new db, use this command
  - `./odoo-bin --addons-path=./addons,/media/sf_VMSharedFolders/custom_addons --test-enable -d test_db_2 -i tops --stop-after-init --test-tags taler`
  - The db name after -d is arbitrary and can be replaced by any other names
- In the results, you should expect to see `odoo.tests.result: 0 failed, 0 error(s) of 9 tests when loading database`

---

Note: if any of these tutorials seem inaccurate, please reach out for clarifications or changes.

---

## Funding

This project is funded through [NGI TALER Fund](https://nlnet.nl/taler), a fund established by [NLnet](https://nlnet.nl) with financial support from the European Commission's [Next Generation Internet](https://ngi.eu) program. Learn more at the [NLnet project page](https://nlnet.nl/project/TALER-Odoo-module).

[<img src="https://nlnet.nl/logo/banner.png" alt="NLnet foundation logo" width="20%" />](https://nlnet.nl) 

---

## Licensing

This work is published under license LGPL-3.0-or-later
