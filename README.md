<!--
SPDX-FileCopyrightText: 2025 Mael Panouillot <panouillot.mael@gmail.com>

SPDX-License-Identifier: LGPL-3.0-or-later
-->

---

# TOPS: Taler-Odoo Payment System

TOPS is a module for Odoo. It allows users to pay with Taler, similar to other existing payment integrations in Odoo.

The module integrates into and increase functionality of other existing Odoo modules (eCommerce, invoices, ticket sales, online payment, etc.). It also implements refunds to customers that used Taler to pay.

Installing this module enables merchants to accept payments from customers using their Taler Wallet, giving them the option to choose a payment system that respects their privacy.

The module is also available on the Odoo Apps store (https://apps.odoo.com/apps/modules/18.0/payment_taler). It has been built for Odoo 18, and is compatible with Odoo 19 as well. The technical name for this add-on is payment_taler.

---

## Documentation

A complete documentation for this module is available here: https://taler-odoo-payment-system.readthedocs.io/en/

A French version of the documentation is also available here. https://taler-odoo-payment-system.readthedocs.io/en/

Contributions and translations are welcome! A detailed explanation on how to contribute or translate is available here: https://taler-odoo-payment-system.readthedocs.io/en/latest/project/how-to-contribute.html

---

## Special thanks to

- The [Odoo Community Association (OCA)](https://github.com/OCA) and their many Open-Source addons, which helped me find my way around which Odoo flows to work on.
- [petites singularites](https://ps.lesoiseaux.io/taler/) for the support, and the administration of the [ICH Forum](https://ich.taler.net/), where I could post questions and updates about my progress, and get support from the community.
- The [Kashier](https://github.com/Kashier-payments/Kashier-Odoo-Payment-Add-on) and [Sadad](https://github.com/Adnanghanchi/Odoo-Payment-Provider) payment providers integrations in Odoo, which provided payment integration examples that helped me steer my work in the right direction.
- Codeberg user @jans for their QA and their help to standardize my code. 

---

## Funding

This project is funded through [NGI TALER Fund](https://nlnet.nl/taler), a fund established by [NLnet](https://nlnet.nl) with financial support from the European Commission's [Next Generation Internet](https://ngi.eu) program. More information at the [NLnet project page](https://nlnet.nl/project/TALER-Odoo-module).

[<img src="https://nlnet.nl/logo/banner.png" alt="NLnet foundation logo" width="20%" />](https://nlnet.nl) 

---

## Licensing

[![REUSE status](https://api.reuse.software/badge/codeberg.org/Nemael/tops)](https://api.reuse.software/info/codeberg.org/Nemael/tops)

This work is published under license [LGPL-3.0-or-later](./LICENSES/LGPL-3.0-or-later), and the devlog is published under license [CC0-1.0](./LICENSES/CC0-1.0.txt). You can find license information at the top of each file.
