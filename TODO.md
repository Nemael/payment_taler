<!--
SPDX-FileCopyrightText: 2025 Mael Panouillot <panouillot.mael@gmail.com>

SPDX-License-Identifier: LGPL-3.0-or-later
-->

- Make a dedicated email address for this add-on, to put on the addon shops' webpage, to receive emails for support and such

Get a better version of the Taler logo to put in my app

Have a discussion with the people that do auto licenses
- Make a post on ICH about my experience and a summary of the discussions, and an explanation of the process

Make a post on ICH asking about the Taler logos
- Maybe ask if they have a Taler logo like this one https://www.taler.net/images/logo-2021.svg, but which would have the words removed a replaced by the full circles?
- Post in the message all the references that Michiel gave me about the logos, and also specify that it is Michiel who gave me these references

Have a discussion with the person that can help on the security aspect
- Commons Caretakers BV, Eric Herman


Change the tab name for every page in my addon (it currently shows "tops.welcome, 1" on the welcome page, which looks very bad


At the end of the project, make sure that none of the logs are displaying sensitive information (such as passwords or secret-tokens)


Add the acknowledgement to NGI and the grant to the Readme file, check email from Michiel


Add the license text for CC0. This is for the purpose of marking files that are not copyrightable, for example configuration files such as .gitignore (See the PR from Gabriel from REUSE)
This is functionally identical to putting the file into the public domain.

Put a license on the text files I made (devlog?). Maybe I want these text files to go into the public domain with CC0, maybe I want LGPL-3.0-or-later on these?  Unsure yet

Add a gitignore file to ignore the pycache folder

Put license cc0 to the devlog files

When I initiate a payment using Taler on the website, I maybe should check for the validity of the password - by requesting a new token maybe?

In the readme, tell which version of Odoo the addon is working for, and it was tested for

- For the payment "Test Mode", there is a radio button right in Odoo's interface to activate "Test Mode" for the payment method
- Credentials are integrated as well

- Do a "Neutralize.sql" file, as can be found in odoo git, in odoo/addons/payment_flutterwave/data/neutralize.sql. I need more information on what this file is, but I probably need it


- Add to the readme that users are advised to create a "Taler" payment journal to record  taler payments
  - If I can, ask the users on install if they want to have a new taler journal created + set this journal by default for the addon

- see if my add-on has "iframe support", such as what is shown in the features for this repo https://github.com/Kashier-payments/Kashier-Odoo-Payment-Add-on


- use this repo's example to make my TODO more robust 
  - https://github.com/Kashier-payments/Kashier-Odoo-Payment-Add-on
  - https://github.com/Kashier-payments/Kashier-Odoo-Payment-Add-on/blob/v16/README.md


- remove the restriction to the US on the payment method's data file
  - maybe add a restriction to only accept european countries or something

- Add checks for which currency is used when the website or accounting systems are used

- add maybe a "powered by Taler" on the invoices with Taler qr code
  - With the "Taler" being the logo of Taler

- When an invoice is created with a taler qr code, try to edit the invoice, and see if the taler qr code is still there

- Don't forget to set the maximum payment time in Taler orders, depending on the time set on the invoice, or the expected time for eCommerce

- Make sure to add license lines to every file

- Add a token refresh system that refreshes a token when the current one is expired


- Write in the documentation that, to sell tickets, you have to install the "event" module, and then go to the settings for events, and check the "online ticketing", and maybe the pos side as well
  - Note, to have the proper ticketing system, you might need to install the python module pycairo:
    - 1. sudo apt install libcairo2-dev
    - 2. pip install rlPyCairo

- Add a button "test connection" next to the field merchant url field that allows you to test if the url you used is a valid merchant url

- Manage connection errors when doing calls from Odoo to Taler merchant
  - For example, if we don't get a response from Taler merchant, make sure that I go back to Odoo payment page with an error message?

- Add in the thanks section in the README
  - OCA with all their repositories
  - GNU Taler
  - Petites Singularite for the support on the ICH forum, where I could share my progress and discussions when making this software
  - The Kashier and Sadad as examples on github (add a link to their)


- take care of the warning:
  - "2025-12-17 05:33:23,720 188137 WARNING test_db_2 odoo.modules.module: Missing `license` key in manifest for 'tops', defaulting to LGPL-3"

- When I do translation, don't forget to do translation of the .xml files

- Remove the warnings that appear when running tests

- Remove the logs in tests

- Put the license on top of every file

- Check if every kind of Taler payment is recorded correctly in the journal (ecommerce, invoice online payment, invoice qr payment with manual payment reconciliation, pos, event ticket sale)

- Make sure that the taler payment qr code on the invoice, expires at the same time as the invoice validity itself

- For the refund system, use the field "refund_delay?: RelativeTime;" in the order creation payload
  - See https://docs.taler.net/core/api-merchant.html#creating-orders

- When adding the merchant url, I should run a quick check that the inserted merchant URL accepts the currencies that I want to use.
  - I can send empty request to [merchant_url]/config to know that, see video https://tutorials.taler.net/dev/merchant-api/versioning at 54 seconds

- Add to the README file that, if there is an issue, they can open an issue on the git repository [repository_url]

- Remove the too many logs, and make them warning, errors, info as required

- Change the currency used in payments to use eur or chf

- Add "How to remove the addon" in the guides
  - Show how to proceed with the removal on the app portal
  - Show, for pos, how to remove the record manually added
  - Show, for pos, if needed, how to remove the added payment option from the setting of a pos store

- Remove unused imports everywhere

- Translate the README in french
  - Redo the tutorial pictures in French as well

- Check at the beginning of any methods from taler_api_method, what the model's type is, and raise a ValidationError() when the model type is wrong

- After all the code cleanup is finished, and the only todos left are the ones to do at later steps of the project, then I should make picture tutorials in the readme for
  - Activation of taler payment provider after installation
    - Including explanation on what to put in the fields such as merchant_url, password, etc
  - online ecommerce transaction completion
  - invoice creation focused on the qr code on invoice
    - plus maybe invoice reconciliation after payment through qr code? In that case I'll have to read the qr code using the addon
  - invoice creation + payment on the online portal
  - ticket sale process, with the info from the readme or TODO on how to install the ticket addon
  - pos setup for the online payment provider
  - pos payment process with qr code for the user

