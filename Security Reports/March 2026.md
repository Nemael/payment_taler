<!--
SPDX-FileCopyrightText: 2025 Mael Panouillot <panouillot.mael@gmail.com>

SPDX-License-Identifier: CC0-1.0
-->

# Security Concerns Report

Project: Taler-Odoo Payment System
Date: 14th of March 2026

## 1. Introduction
This report outlines the security concerns identified during the development of the Odoo module `payment_taler`. The purpose of the module is to allow Odoo users to accept payments using GNU Taler. The review focuses on potential vulnerabilities that could compromise the confidentiality or integrity of payment transactions made using this module.

The security assessment was performed during the development phase to ensure that the integration adheres to best practices for secure payment processing and follows relevant security standards.

## 2. Scope of the Security Review
The scope of this review covered the following aspects of the Odoo module:
- Integration between Odoo and GNU Taler
- Payment processing flow and transaction handling
- User authentication and authorization mechanisms
- Secure storage and transmission of payment data
- Interaction with third-party dependencies and external services
- Input validation and sanitization in the payment form
- Infrastructure components such as web server security and external API configurations were not within the scope of this review.

## 3. Methodology
The security concerns were identified during code review: a manual review of the payment_taler Odoo module’s source code was performed to identify insecure coding practices and improper handling of sensitive information.

## 4. Mitigated risks
After discussion with security professionals, it was decided that the safest way to store sensitive Taler data in Odoo, was to use Odoo's buit-in `password` fields, and ensure of the correct security access rights.

From this discussion, I made sure to:
- Limit the amount of sensitive data stored in the add-on (it is limited to the Taler Merchant instance password, and the access token created from it)
- Store the password in an Odoo `password` field, as well as the access token created using this password.
- Restrict these field's access to the `base.group_system` Odoo group, which can only be accessed using an administrator account on the Odoo instance.

## 5. Identified Security Concerns
### 5.1. Exposure of payment data in logs
> Risk Level: Low

#### Description
Payment data, including Taler Order ID, is being logged in plaintext as debug data. This occurs only if Odoo is started with the parameter `log_level = debug`. This poses a significant security risk if the logs are accessed by unauthorized individuals.

#### Impact
(If Odoo's debug logs are activated) Exposure of payment information in the Odoo server's logs, specifically the Order ID, amount, currency, summary, fulfillment_url and pay deadline parameter. This data leak could lead to data theft or fraud.

#### Recommended mitigation steps
- Ensure that logs contain only essential information and do not record full payment details.
- Mask or encrypt sensitive payment data in logs to prevent unauthorized access.

### 5.2. Capture of Taler Merchant instance access token
> Risk Level: Low 

#### Description
The access token used to connect to the Taler Merchant could be captured by a malicious actor.

- Payments are sent and accepted to the Taler Merchant using the user's access token. An access token is obtained by sending the user's password to url `{taler_instance}/private/token`.
- The token is only used with `https` endpoints.
- A token's lifetime is limited by default (with duration set on the Taler Merchant's configuration).
- The tokens also can be limited in scope between `readonly`, `all`, `spa`, `order-simple`, `order-read`, etc... ([see GNU Taler documentation](https://docs.taler.net/core/api-merchant.html#scopes))

#### Impact
The access token could be captured by a malicious actor, and be used to the extent of the token's capabilities to read or create orders in the name of the victim. They can also trigger refunds for paid orders.
- Order cannot be paid for using this token, because orders are paid from a Taler wallet only, which is unrelated to this access token.

#### Recommended mitigation steps
- Limit the lifetime of a token on the Odoo add-on's side.
- Limit the scope of a token when its creation is requested, this avoids having tokens with `all-access`, when they only need `read-access`. 

### 5.3. Capture of Taler Merchant instance password
> Risk Level: Medium

#### Description
The password to the Taler Merchant can be used to request an access token. This password could be captured by a malicious actor.
- The password to the Taler Merchant is stored securely in an Odoo `password` field.
- When a request is sent to request an access token (using a `http` endpoint), the password is sent to authenticate the user.
- The password can be used to request access tokens.

#### Impact
The password can be used to request any number of access tokens, with any access-rights or lifetime-length. Subsequently, these access tokens can be used to read or create orders in the name of the victim. They can also trigger refunds for paid orders.
- You cannot pay for an order using the password to the Taler Merchant instance.

#### Recommended mitigation steps
- Regularly scheduled password changes.
- Send the password in an obfuscated way to the `https` endpoint.

## 6. Risk Summary
| Security Issue              | Risk Level | Status                  |
|-----------------------------|------------|-------------------------|
| Instance user password leak | Medium     | Needs improvement       |
| Instance access token leak  | Low        | Needs improvement       |
| Payment data exposure       | Low        | No improvement required |

### 7. List of outgoing API calls
There are a few API calls to the Taler Merchant instance. They're all used during the process of setting up the Taler payment provider, or creating an order, and validating its payment.
The [GNU Taler API documentation](https://docs.taler.net/core/api-merchant.html#merchant-backend-restful-api) is useful to understand this section.
- `getMerchantConfiguration()`
  - Used to confirm that the chosen merchant is valid, and compatible with the Odoo currencies.
  - This is the only call to a non-restricted Taler endpoint
- `requestGetToken()`
  - Get the access token from the user password.
  - Uses the user-entered password to obtain an access token.
    - The access token is used for identification by all the other API calls.
    - This is the only call that uses the user password.
  - The requested access token has an access scope of `write`.
- `getOrderTalerUri()`
  - Gets the URI from an order ID
  - Return the URI of an order. This URI is then shown to the user for them to pay the order.
  - This method uses the access token for authentication.
- `postPlaceOrderWithFulfillmentMessage()`
  - This method uses the access token for authentication.
- `postPlaceOrderWithFulfillmentUrl()`
  - The fulfillment URL used is Odoo's return page.
    - Where a further method checks if the order has been paid for, using another API call.
  - This method uses the access token for authentication.
- `requestRefundForOrder()`
  - This method triggers the refund for an order.
    - If triggered, the customer has to scan the created refund URI into a Taler Wallet
  - This method uses the access token for authentication.
- `requestGetOrderFromId()`
  - Obtain all the order metadata based on an order ID.
  - This is used to check if an order has been paid by the customer.
  - This method uses the access token for authentication.

## 8. Recommendations

Based on the findings, the following steps are recommended:
- Improve the access token request system to secure the password more thoroughly.
- Improve the requested access token to reduce their scope or lifetime.

## 9. Conclusion

The add-on Taler-Odoo Payment System (payment_taler) introduces several potential security risks regarding authentication to the Taler Merchant instance, particularly in the areas of password-sharing over the network. By addressing the identified vulnerabilities and implementing the recommended mitigations, the security posture of the system can be significantly improved, providing a secure environment for processing transactions and protecting user data.
