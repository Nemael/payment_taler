<!--
SPDX-FileCopyrightText: 2025 Mael Panouillot <panouillot.mael@gmail.com>

SPDX-License-Identifier: LGPL-3.0-or-later
-->

_This page is also available in French (here)[link to lisezmoi_fr.md] LISEZMOI_FR.md

_Cette page est également disponible en Français (ici)[lien vers lisezmoi_fr.md] LISEZMOI_FR.md_

---

# TOPS: Taler-Odoo Payment System

TOPS is an add-on for Odoo. It allows users to pay with Taler, similar to other existing payment integrations in Odoo.
The module integrates into and increase functionality of other existing Odoo modules (eCommerce, invoices, ticket sales, online payment, etc.). It also implements refunds to customers that used Taler to pay.

Installing this module enables merchants to accept payments from customers using their Taler Wallet, giving them the option to choose a payment system that respects their privacy.

It is available on the Odoo Apps store (https://apps.odoo.com/apps) PENDING LINK, as well as on the OCA community shop (https://odoo-community.org/shop) PENDING LINK

It has been built for Odoo 18, and will be updated to Odoo 19 once milestone 1.0 is reached.

---

## Tutorials and flow walkthrough

### Install or update the add-on on an already-existing Odoo installation

- There are multiple ways to install this add-on
  - Install from the OCA community shop
    - PENDING
  - Install from the Odoo Apps store
    - PENDING
  - Add the code yourself in your Odoo install (by cloning or downloading the release)
    - Clone this repository (git clone https://codeberg.org/Nemael/tops.git)
      - Preferably clone it in `{your Odoo install}/custom_addons`
        - Ensure that the `tops` directory is in `custom_addons`
    - Download the latest version from the releases (https://codeberg.org/Nemael/tops/releases)
      - Extract the zip file to `{your Odoo install}/custom_addons`
      - Ensure that the `tops` directory is in `custom_addons`
    - Note: the code can be stored anywhere, but it's easier store it within the Odoo folder
- In the command line you used to start Odoo, specify the path to this add-on by adding the argument `--addons-path=./addons,./custom_addons/tops`
  - Such as: `./odoo-bin --addons-path=./addons,./custom_addons/tops -u tops -d odoo18_tops_0.1.1.1`
- In Odoo, go to the `Apps` section in the app switcher (top-left button)
- Click `Update Apps List` on the top bar
- Search for the add-on `Taler-Odoo Payment System`
- Click on the add-on, and press `Activate` or `Install` to complete this step 

> To update the add-on, first update the code using the same way that you first downloaded it, then restart the server and finally click `Upgrade` on the add-on page


### How to setup the Taler payment provider

- Once the addon is installed from the Apps:
  - Go to the payment providers menu. It can be accessed in multiple ways:
    - `Website -> Configuration -> eCommerce -> Payment Providers`.
    - `Invoicing -> Configuration -> Online Payments -> Payment Provider`s.
  - Either way you land here, this is the list of your currently available payment providers.
  - A new `Taler` payment provider will be in this list, set as disabled for now.
  - Click on the Taler payment provider.
  - In the `Credentials` tab, set the Taler merchant URL.
    - By default, the demobank's credentials are used. You can access the demobank [here](https://backend.demo.taler.net/instances/sandbox/)
    - After setting the URL, you can click the `Check URL validity` button to check if the entered URL is reaching a valid Taler merchant, and that this merchant's accepted currencies are compatible with you Taler available currencies.
      - You can find the accepted currencies in the `Configuration` tab.
  - Then set the Taler Merchant Password. It will be used for API calls to the merchant.
  - You may want change the Taler fulfillment message as well. It will be shown on created Taler transactions
    - This change is only for the Taler order, there will be no change in Odoo.
    - If you'd like to change the Odoo fulfillment messages shown to the customers after a payment using Taler, you can do so in the `Messages` tab.
  - The default values are connecting to the sandbox Taler merchant:
    - URL: https://backend.demo.taler.net/instances/sandbox
    - Password: sandbox
  - It is advised, but completely optional, to create a Taler-specific Journal (this can be set in the Configuration tab).
    - This will help during the Accounting process.
  - Click the `Enabled` radio button.
- The initial setup is now complete and Taler payment will be available in all eCommerce, online payments and Invoicing apps.

<img src="payment_taler/README_Pictures/EN/Taler_provider_setting_complete.png" alt="Taler providers settings" width="700px">

### Complete an eCommerce payment

- Once you have completed the Taler initial setup, customers can pay on your website.
- To do so, they will open the shop and add any items to their cart.
- During the checkout, they can now select the `Taler` payment provider.

<img src="payment_taler/README_Pictures/EN/Taler_ecommerce_checkout.png" alt="Taler eCommerce checkout" width="700px">

- After clicking `Pay now`, a new Taler order will be created on the merchant side, and the customer will be redirected to the Taler order, from which they can pay with any Taler wallet on their phone or web browser.

<img src="payment_taler/README_Pictures/EN/Taler_ecommerce_wallet.png" alt="Taler eCommerce wallet" width="300px">

- On completion of the payment using their wallet, the customer will be redirected back to your Odoo website, which will show a successful payment confirmation.

<img src="payment_taler/README_Pictures/EN/Taler_ecommerce_payment_processed.png" alt="Taler eCommerce payment processor" width="700px">

### Create an invoice that can be paid with Taler

- It is possible to create an invoice that includes a Taler QR Code to pay it.
  - Go to the Invoicing app and create a new invoice.
  - Fill any data relevant to the invoice that you are creating.
  - Important step: In the `Other Info` tab, set the Payment Method to `Taler` (see below). Otherwise, the QR Code will not be generated.
  
<img src="payment_taler/README_Pictures/EN/Taler_invoices_payment_method.png" alt="Taler invoices payment method" width="700px">

- When you are done, click `Confirm` at the top, you will be led to the invoice page.
  - You can now click `Preview` to see the Invoice that will be sent to your customer.
  - The invoice's PDF will include a Taler payment QR Code, as well as some Taler order information.

<img src="payment_taler/README_Pictures/EN/Taler_invoices_taler_qr_code.png" alt="Taler invoices taler qr code" width="700px">

- If a customer pays for the invoice using the QR Code present in the PDF, you will have to do a manual payment reconciliation.
  - To do this, once you confirm that you received the payment, go to the Invoices' app page.
  - Click on `Pay`.
  - Confirm the data shown in the opened window, it is recommended to add the Taler OrderID shown on the invoice, to the `Memo` field, to keep track of the payment more easily.
  - Press `Create Payment`.


### Online invoice payment using Taler

> This process is unrelated to the invoices created with Taler in the previous step\
> Any invoice can be paid online using Taler

- Go to the Invoicing app and create a new invoice.
- Once created, you can press `Preview` to see the page that the customer will see.
- On this page, the user will be able to click `Pay Now`, and choose Taler as a payment option.

<img src="payment_taler/README_Pictures/EN/Taler_invoices_online_payment.png" alt="Taler invoices online payment" width="700px">

- Once they click `Pay`, they will be redirected to the Taler order page, where they can pay with a Taler wallet on their phone or web browser (in the same way as for an eCommerce payment).
- When the payment is complete, the customer will be sent back to the invoice page, with a notice saying that the payment is successful.

<img src="payment_taler/README_Pictures/EN/Taler_invoices_paid_online.png" alt="Taler invoices paid online" width="700px">

### Purchase an Event ticket online using Taler

> Note: to have a fully working ticketing system, you might need to install the python module pycairo:\
> `sudo apt install libcairo2-dev`\
> `pip install rlPyCairo`

- How to make event tickets available for customers to pay for using Taler.
  - Add the "Events" add-on on your Odoo instance.
  - Go to the settings app, and navigate to the "Events" settings.
  - Tick the "Online Ticketing" and save the changes.

<img src="payment_taler/README_Pictures/EN/Taler_ticketing_settings.png" alt="Taler ticketing settings" width="700px">

  - Tickets are now available to buy using Online payments providers, including the Taler payment provider!
  - Customers can now navigate the "Events" tab on your website, and choose any event they'd like to purchase a ticket to.

<img src="payment_taler/README_Pictures/EN/Taler_ticketing_events_list.png" alt="Taler ticketing event list" width="700px">

  - When they click an event, they can register in it, which will prompt them to give some information, and then lead them to a payment page
  - On this payment page, the customer can select Taler as a payment provider.
  - They will be redirected to a Taler order page, where they can pay with their wallet or web browser.
  - Once payment is finished, the customer will land back on the odoo page, with their payment successfully processed, and a .pdf of the event tickets available.

<img src="payment_taler/README_Pictures/EN/Taler_ticketing_event_payment_confirmation.png" alt="Taler ticketing event payment confirmation" width="700px">

### How to setup POS payment provider

- Allowing Taler payment on the point-of-sale app requires a few more steps than online payments aboves.
- Preliminary steps.
  - Only do this step if you have previously [setup Taler as a payment provider](#how-to-setup-the-Taler-payment-provider).
  - Install the "Point of sale" Odoo addon.
- Create the Point of Sale payment method.
  - On the top bar, press Configuration -> Payment Methods.
  - Create a new Payment Method.
  - Call it "Taler" (You can call it anything but Taler is easier to remember).
  - Check "Online Payment".
  - Select "Taler" in the "Allowed Providers" field.
- Adding Taler to the point of sale (Make sure that the point of sale register is closed for this step).
  - On the top bar, press Configuration -> Point of Sale list.
  - Select the point of sale you'd like to add Taler payment to (for test data, Clothes Shop is a good candidate).
  - Click on "More settings: Configurations > Settings", which will lead you to the point of sale's settings page.
    - Alternatively, you can access this page by going to Settings through the app switcher on the top right, then going to "Point of Sale" section, and selecting the point of sale that you would like to modify.
  - In Payment -> Payment Methods, add the payment method you just created. It can be named "Taler", or any other custom name you chose.
- The setup is now complete, and you can select your new payment provider when a customer pay for an order on the Point of sale that you added the payment method to.

### Payment on a Point of Sale

- Open a register on one of the Points of Sale for which you activated the Taler payment method in the previous step.
- Put any items in the order, and once done, click "Payment" at the bottom of the page.
- The "Taler" payment method, that you added earlier, should now be available in the payment options.

<img src="payment_taler/README_Pictures/EN/Taler_pos_taler_payment.png" alt="Taler pos taler payment" width="700px">

- Clicking on the option and validating it will prompt the customer with a QR Code.
- Scanning this QR Code will redirect to an Odoo page, where they will be able to choose to pay with Taler.
- This will bring the customer to a Taler order page, and they will be able to pay using their Taler wallet or web browser.
- Upon the payment completion, the customer will be redirected to Odoo, with a confirmation of payment (first picture), and the order on the point of sale's side will show a successful payment, and produce the receipt (second picture).

<img src="payment_taler/README_Pictures/EN/Taler_pos_payment_complete.png" alt="Taler pos payment complete" width="700px">

<img src="payment_taler/README_Pictures/EN/Taler_pos_receipt.png" alt="Taler pos receipt" width="700px">

### Refunding an online payment

- To make a refund, you first have to find the payment you wish to refund.
- In the `website` or `invoicing` add-on, navigate to `Configuration -> Payment Transactions` on the top bar.
  - This page will show you all the transactions that have been completed.
- Click the transaction that you would like to refund.
  - In the picture, the transaction to refund is `S00060`.

<img src="payment_taler/README_Pictures/EN/Taler_refund_list_of_transactions.png" alt="Taler list of transactions" width="700px">

- On the transaction page, click on the linked payment.
  - In the picture, the linked payment is `PBNK1/2026/00029`.

<img src="payment_taler/README_Pictures/EN/Taler_refund_transaction.png" alt="Taler transaction page" width="700px">

- On the payment page, click `Refund` in the action button section and confirm the refund.

<img src="payment_taler/README_Pictures/EN/Taler_refund_payment.png" alt="Taler payment page" width="700px">

- Confirming the refund will create a new transaction, that you can view in the list of transactions, with the name `R-{Odoo reference number}`.
  - An email containing a QR Code for the customer will also be sent to the customer's email address.
    - You can find the list of emails in `Settings -> Technical -> Emails`
  - To receive the refund, the customer will have to scan the QR Code with their Taler wallet.

<img src="payment_taler/README_Pictures/EN/Taler_refund_email.png" alt="Taler refund email to customer" width="700px">

_Notes:_
  - _You need a functional email address for this feature to work properly._
    - _Without an email address, the email will be generated and can be read, but it will not be sent._ 
  - _You can only do full refunds using Taler. Partial refunds are not implemented, but Taler does allow for partial refunds, so it could be a supplementary feature._

### Merchant test mode

- The merchant test mode allows you to test the installation of the Taler-Odoo Payment System, and confirm that the module and the selected merchant are working properly.
- In the Odoo UI, all the payment information will be shown with actual values (amount, currency, etc), but the currency will automatically be swapped to "Kudos" right before sending the order to the Taler merchant.
- <strong>Warning:</strong> Do not use this mode in production or with published items for sale.
- Here is an example of the flow for this feature:
- _Note: The test mode makes the payment provider "unpublished", which means that only administrator users will be able to see the payment provider in this state. To go through this flow, I usually use the "Mitchell Admin" user available from Odoo's demo data._
- On the payment provider's page, check the "Test Mode" radio button.

<img src="payment_taler/README_Pictures/EN/Taler_test_mode_radio_button.png" alt="Taler test mode radio button selected" width="700px">

- Then start the process for any online payment, I will show the process for an eCommerce payment.
- Navigate to the shop page.
- Select any product that you'd like to buy as a test, go to your cart and start the checkout process.
- Once you confirm your order, the Taler payment method will appear, with two icons.

<img src="payment_taler/README_Pictures/EN/Taler_test_mode_payment_method_with_icons.png" alt="Taler test mode payment method with two icons, striked-through eye and yellow warning sign" width="700px">

- Symbols:
  - The red striked-through eye means "Unpublished". It is there to let you know that this payment method is not visible to visitors, only users that have access rights to the shop, will be able to see the test mode Taler payment provider.
  - The yellow warning sign means "Test mode". It is there to warn you that the test mode is activated for this payment method.
- Go ahead and pay the order. A corresponding order will be created on the Taler merchant, with a currency change.
  - The currency is getting swapped with "Kudos".
    - Kudos is an imaginary currency created for Taler. It can be used for free to test transactions with your order wallet.
- A Taler order will be created, with the currency replaced by Kudos, that you can open and pay with your wallet.

<img src="payment_taler/README_Pictures/EN/Taler_test_mode_taler_order_payment.png" alt="Taler test mode payment on Taler, showing kudos currency" width="700px">

- Once the order is paid using the imaginary currency, you will be sent back to the completed Odoo order.

<img src="payment_taler/README_Pictures/EN/Taler_test_mode_taler_payment_completed.png" alt="Taler test mode payment shown as completed on Odoo website" width="700px">

- If you reach this step in a similar manner with no raised issues, the test is complete, the add-on works and the Taler merchant endpoint can receive your orders for compatible currencies.

---

### Change settings using CLI

- Run the Odoo CLI shell by adding `shell` to your original command line to start Odoo.
  - Such as `./odoo-bin shell --addons-path=./addons,{custom_addons_path} -u tops -d odoo18_tops_0.1.1.1`
- Run these commands to edit the setting you want to set. You can use `get_params` to print the current value, and `set_params` to set a new value:
  - `env['ir.config_parameter'].set_param('tops.merchant_url', 'https://backend.demo.taler.net/instances/sandbox/')`
  - `env['ir.config_parameter'].set_param('tops.password', 'https://backend.demo.taler.net/instances/sandbox/')`
- <strong>IMPORTANT:</strong> Commit the changes to the database before closing the shell instance and restarting Odoo:
  - `env.cr.commit()`
  - `exit()`

---

### Editing rights to the payment provider settings

- As with other payment providers, not all Odoo users on an instance can modify the Taler payment provider settings.
- Only user that belong in the `base.group_system` user group will be able to access and modify the Taler payment provider settings.


---

### Uninstall the addon

- To uninstall the addon, you have to go to the `Apps` app on Odoo.
- In there, search for and go to the `Taler-Odoo Payment System` addon.
- Click `Uninstall`, the addon should be uninstalled.
- You can reinstall the addon at a later time.
- If you added a payment method record for the point of sale app:
  - Go to the Point of Sale app, and navigate to `Configuration/Payment Methods`.
  - Click on the "Taler" record you created when setting up the point of sale payment system, it should be highlighted in red because the payment provider is not available anymore.
  - Click on the gear at the top, and then either "Archive" (better) or "Delete" (more risky because you might lose track of some payments)
  - On the top bar, press Configuration -> Point of Sale list.
  - Select a point of sale that you made Taler payments available for.
  - Click on "More settings: Configurations > Settings", which will lead you to the point of sale's settings page.
  - In Payment -> Payment Methods, remove the Taler payment method. It can be named "Taler", or any other custom name you chose when first setting it up.
  - Do this for every point of sale you made Taler payments available for.

---

## Folder structure

This add-on uses a quite standard folder structure:
- `controllers` contains the controllers used by the addon.
- `data` contains setup data that is processed when someone installs the add-on, as well as email templates.
- `Devlog` is a text compendium of the posts I am making on the ICH forum
- `LICENSES` contains the text of the licenses used in this project.
- `models` contains the Odoo models. There are:
  - `taler_api_method`, which contains the methods used to communicate to the Taler merchant API.
  - `taler_invoicing`, which contains the methods used when creating invoices with Taler.
  - `taler_provider`, which contains the methods used by the Taler payment provider.
  - `taler_transaction`, which contains the methods used to complete a transaction with Taler.
- `payment_taler/README_Pictures` contains all the pictures shown in this README.
- `static` contains logo data and other image assets for the addon.
- `tests` contains unit tests for this project.
- `utils` contains utility methods (such as logging).
- `views` contains a view for each of the models.

---

## Running unit tests

- To run unit tests on a new db, use this command:
  - `./odoo-bin --addons-path=./addons,{custom_addon_path} --test-enable -d test_db_2 -i tops --stop-after-init --test-tags taler`
  - The db name after -d is arbitrary and can be replaced by any other names.
- In the results, you should expect to see `odoo.tests.result: 0 failed, 0 error(s) of 9 tests when loading database`.

---

> If any of these tutorials or information seem inaccurate, please either reach out for clarifications or changes on [Support email not created yet], or open an issue on the [TOPS repository](https://codeberg.org/Nemael/tops/)

---

## Common issues

### The "Check URL validity" button is showing me an error

- This button is meant to check that the Taler merchant is valid and supports the same currencies that you are using.
  - The error message will explain if there are any discrepancies, and show the supported currencies on the merchant side.
- To change the currencies you'd like to support with Taler, go to the `Configuration` tab in the payment provider, and navigate to `Availability -> Currencies`.
  - This change will be overwritten when you restart the Odoo server.
  - For a more permanent change, you can edit the `const.py` file, and comment/uncomment the currencies that you want to set as Taler configuration.
  - `const.py` is loaded at server start, 

_Note: Because KUDOS is an imaginary currency, you will not find it in this list._

---

## Translation & Available languages

- This module is currently available in English and French
  - Invoices and emails sent to customer for refund are also translated, adn will be snet in the language that is set for the customer, in their customer profile.
  - This README is also translated in file README_FR (Add the link to the README_FR file here) 
  - Translation in other languages is welcome, please see ADD LINK HERE TO `How to translate` SECTION for a how-to-translate.

---

---

## Following the updates of this module:

- You can see updates announcement in this category of the ICH.taler.net forum: https://ich.taler.net/c/integrations/odoo/29
- I also post regular devlogs in this thread of the same forum, where I explain my process: https://ich.taler.net/t/taler-odoo-payment-system-devlog/437

---

## How to contribute? (WIP)

- Guide on how to clone, run, and contribute to the code.
- Ideas on features that could be implemented.
  - More translations (See ADD LINK HERE TO `How to translate` SECTION)
  - Partial refunds.
  - Implementing functionality for
    - Odoo 19 (will probably be done by the time 1.0 is released)
    - Future Odoo releases (20, ...)

---

## How to translate

- If you would like to do a translation of the module, the process is rather simple
  - The file `i18n/payment_taler.pot` ADD LINK TO THIS FILE HERE is the base translation file, with all the strings of text stored in it
  - Copy this file into a new file `{New language}.po`, such as `fr.po`
  - In this new file, translate all the strings of text that you would like to translate, you can use `fr.po` ADD LINK TO THIS FILE HERE as a guide on how to format the translation.
  - Once complete, you can re-make your Odoo test database, and change your user's language to the desired language. The translation you made should appear on Odoo.
  - If you are encountering any issues, please open a thread in this forum category https://ich.taler.net/c/integrations/odoo/29 (You can ping me as well @Nemael), and specify that you are doing a new translation.
---

## Tech support

If you are encountering any issues with the add-on, please don't hesitate to either
- Open a thread in this forum category https://ich.taler.net/c/integrations/odoo/29 (You can ping me as well @Nemael). Please explain your situation in detail, and the problem you are encountering.
- Open an issue on the Codeberg repository https://codeberg.org/Nemael/tops/issue. Please explain the issue you are having on a technical point-of-view.

---

## Funding

This project is funded through [NGI TALER Fund](https://nlnet.nl/taler), a fund established by [NLnet](https://nlnet.nl) with financial support from the European Commission's [Next Generation Internet](https://ngi.eu) program. Learn more at the [NLnet project page](https://nlnet.nl/project/TALER-Odoo-module).

[<img src="https://nlnet.nl/logo/banner.png" alt="NLnet foundation logo" width="20%" />](https://nlnet.nl) 

---

## Special thanks to

- The [Odoo Community Association (OCA)](https://github.com/OCA) and their many Open-Source addons, which helped me find my way around which Odoo flows to work on.
- [petites singularites](https://ps.lesoiseaux.io/taler/) for the administration of the [ICH Forum](https://ich.taler.net/), where I could post questions and updates about my progress, and get support from the community.
- The [Kashier](https://github.com/Kashier-payments/Kashier-Odoo-Payment-Add-on) and [Sadad](https://github.com/Adnanghanchi/Odoo-Payment-Provider) payment providers integrations in Odoo, which provided examples that helped me steer my work in the right direction.

---

## Licensing

[![REUSE status](https://api.reuse.software/badge/codeberg.org/Nemael/tops)](https://api.reuse.software/info/codeberg.org/Nemael/tops)

This work is published under license [LGPL-3.0-or-later](./LICENSES/LGPL-3.0-or-later), and the devlog is published under license [CC0-1.0](./LICENSES/CC0-1.0.txt). You can find license information at the top of each file.
