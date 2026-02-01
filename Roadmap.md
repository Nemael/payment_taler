These are the Milestones to the end of the project

### Groundwork & Mock up - Done!
Groundwork of the project. Setup of a basic Odoo module to implement the project's functionalities
down the line, mock-up of the module's UI, and alpha release of the module. This release is meant
to allow easy distribution of the module for developers, and quick deployment of features once
developed.

Work toward this milestone will be tagged "0.1.x"

- Basic Odoo module, groundwork of module's structure, mock UI of the different interfaces
to manage Taler on the merchant's side

- Roadmap, logging and debug information

- Alpha release of the module intended for ad hoc distribution to developers

### Basic Payment with Taler - Done!
First implementation of Taler payment in the accounting app, using the basic module previously
setup. First implementation of administrator settings (for banking information), and unit testing
implementation, wherever possible.

Work toward this milestone will be tagged "0.2.x"

- Enable Taler payment for invoice payment with the Accounting app

- Allow admins to set and modify backend Taler settings (bank account number, etc.)

- Implementation of unit testing

### Odoo ecosystem integration - Done!
Integration of Taler payment in more apps (Ecommerce and Point-of-Sale). Integration of right-of-
access system in the module.
Work toward this milestone will be tagged "0.3.x"

- Enable Taler payment for the Ecommerce app, allowing payment of online shopping, online
booking with the Website app and event tickets with the Sales app

- Enable Taler payment for Self-Ordering using the Point-of-Sale app

- Integration of right-of-access system to determine who can modify merchant settings within
Odoo.

### Internationalisation & Accessibility - In progress
This is the polishing step of the module, which is very important to make it reach a larger public.
Work toward this milestone will be tagged "i18n&a11y"

- Internationalisation of the module. Implementation of i18n solutions to facilitate translation of the
module in multiple languages.

- Translation of the module in French
Accessibilisation of the module, ensuring ease of use of the module with screen readers and
ensuring that the module follows Odoo's accessibility best practices

### Merchant Test Mode - Done!
Implement a "Test Mode" in the module. This allows merchants to ensure that everything is
working properly.

This is similar to existing payment system test mode
https://www.odoo.com/documentation/master/applications/finance/payment_providers.html#test-mode

Work toward this milestone will be tagged "merchants test mode"

- Implement a "Test mode" to allow merchants to ensure that everything is working properly
with their Taler payment system.

### Taler Refunds - Done!
Implements refund to customers using Taler.

Work toward this milestone will be tagged "refunds"

- Implement refunds for customers using Taler.

### Documentation - In progress
Documentation is a very important part of every software, and this milestone ensures that budget
and time is set aside to make a complete documentation of the software I am making.
Documentation will be integrated in the git repository, and will be readable in the form of a wiki on
Codeberg. 

Work toward this milestone will be tagged "documentation"

- Installation how-to guide (with and without the Odoo Add-ons shop)

- Usage tutorial

- UI Explanation

### Security audit - In progress
Software security is important, payment software security is mandatory and non-trivial. This
milestone sets some time aside to respond to a Security Audit, address any bugs that may be
found, and report on any lessons learned.

Work toward this milestone will be tagged "0.8.x"

- Allocate some budget and time to resolve potential security flaws that would arise and go
through the NGI Security Audit process.

- Write a report on security concerns that arose during development and/or audit.

### Package Release - To be started
This is the release of the software. It is important to create an attractive main page for the module,
to catch the interest of users. This release will also allow for finishing touches to be implemented,
such as documenting on how to further improve on the project, and automate the release process.

Work toward this milestone will be tagged "release"

- Automate release process

- Document "how to contribute" on the repository

- Distribute module on the Odoo App Store and create an attractive main page for the
module

- Distribute the module on the OCA shop
