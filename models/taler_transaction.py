# SPDX-FileCopyrightText: 2025 Mael Panouillot <panouillot.mael@gmail.com>
#
# SPDX-License-Identifier: LGPL-3.0-or-later

from odoo.exceptions import ValidationError
from odoo import models, fields
from odoo.addons.tops.utils.utils import talog, tawarn, tadebug, generate_UUID, get_datetime_now_to_epoch
from odoo.addons.tops.models.taler_api_methods import requestGetToken, postPlaceOrderWithFulfillmentUrl, getOrderTalerUri, requestGetOrderFromId, getOrderIdStatus, checkOrderIsPaid, sendRefundForOrder
from odoo.addons.tops.controllers.taler_controller import TalerController


import logging


class TalerTransaction(models.Model):
    _inherit = 'payment.transaction'
    #Because this model inherits, and does not have its own name, there is no need for it to appear in ir.model.access.csv
    #It will inherit the ir security settings from the account.move model

    taler_order_id = fields.Char(string="Taler Order Id", default="")
    taler_order_url = fields.Char(string="Taler Order Url", default="")
    taler_order_uri = fields.Char(string="Taler Order Uri", default="")
    # This UUID is only used for the fulfillment url. Without the UUID in the url, the Taler merchant could mix up two orders with the same Odoo ID, on two different Odoo instances
    # This is not a perfect solution, as two duplicate UUID + OrderID could be generated on two different Odoo instances, on the same Taler Merchant, but this is highly unlikely.
    taler_uuid = fields.Char(string="Taler UUID", readonly=True, default=generate_UUID())

    def getToken(self):
        requestGetToken(self)

    def isPaid(self):
        return checkOrderIsPaid(self)

    def _process_notification_data(self, data):
        super()._process_notification_data(data)
        if self.provider_code != 'taler':
            tadebug("Getting different provider code than taler: ", self.provider_code, ". This is not necessarily an error")
            return
        self.provider_reference = data.get('merchantOrderId')

        # Update the payment state based on payment status on the merchant's side
        payment_status = data.get('paymentStatus')
        if (payment_status == 'paid'):
            talog("Order paidzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz")
            _logger = logging.getLogger(__name__)
            self._set_done()
            print("SETTING DONE TRANSACTION")
            print("payment_id: ", self.payment_id)
            print("state", self.state)  # must be 'done'
            print("payment", self.payment_id)  # must exist
            print("payment state", self.payment_id.state)  # must be 'posted'
            print("payment move state", self.payment_id.move_id.state)  # must be 'posted'
            print("calling post process")
            print("is post processed", self.is_post_processed)
            self._post_process()
            print("SETTING DONE TRANSACTION")
            print("payment_id: ", self.payment_id)
            print("state", self.state)  # must be 'done'
            print("payment", self.payment_id)  # must exist
            print("payment state", self.payment_id.state)  # must be 'posted'
            print("payment move state", self.payment_id.move_id.state)  # must be 'posted'
            print("calling post process")
            print("is post processed", self.is_post_processed)
            print("called post process")
            print("is post processed", self.is_post_processed)
            #Testing process, remove the following line action_validate for release
            #This line skips the reconciliation process, that should be done manually
            #Sets the payment as "Paid" when transaction is completed
            self.payment_id.action_validate()
            # self._set_transaction_done()
            print("state_message: ", str(self.state_message))
            print("sale_order_ids: ", self.sale_order_ids)
            print("Transaction %s successfully called _set_done(). Final state: %s", self.reference,
                         self.state)
            print("Transaction %s is_post_processed: %s", self.reference, self.is_post_processed)
            print("state", self.state)  # must be 'done'
            print("state", self.payment_id.state)  # must be 'posted'
            print("operation", self.operation)
            # self.operation = "online"
            print("operation fixed?", self.operation)
            # print("is_refundable", self.payment_id.is_refundable)
            print("payment state", self.payment_id.state)  # must be 'posted'
            print("refund support: ", self.provider_id.support_refund)
            print("child transaction ids", self.child_transaction_ids)
            print("refunds_count", self.refunds_count)
            print("invoices_count", self.invoices_count)
            print("self.amount", self.amount)
            # print("payment_id.refunded_amount", self.payment_id.refunded_amount) doesn't exist
            print("payment_id.amount_available_for_refund", self.payment_id.amount_available_for_refund)
            self.payment_id.amount_available_for_refund = 100
            print("payment_id.amount_available_for_refund", self.payment_id.amount_available_for_refund)
            # self.refunds_count = 1
            # self.invoices_count = 1
            # print("refunds_count fixed?", self.refunds_count)
            # print("invoices_count fixed?", self.invoices_count)

            # print("COMPUTING STUFF")
            # for payment in self.payment_id:
            #     print("payment", payment)
            #     print("IN FOR LOOP")
            #     tx_sudo = payment.payment_transaction_id.sudo()
            #     payment_method = (
            #             tx_sudo.payment_method_id.primary_payment_method_id
            #             or tx_sudo.payment_method_id
            #     )
            #     print(payment_method)
            #     print("if values:")
            #     print(tx_sudo)
            #     print(tx_sudo.provider_id.support_refund, tx_sudo.provider_id.support_refund != 'none')
            #     print(payment_method.support_refund, payment_method.support_refund != 'none')
            #     print(tx_sudo.operation, tx_sudo.operation != 'refund')
            #     if (
            #             tx_sudo  # The payment was created by a transaction.
            #             and tx_sudo.provider_id.support_refund != 'none'
            #             and payment_method.support_refund != 'none'
            #             and tx_sudo.operation != 'refund'
            #     ):
            #         print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
            #         # Only consider refund transactions that are confirmed by summing the amounts of
            #         # payments linked to such refund transactions. Indeed, should a refund transaction
            #         # be stuck forever in a transient state (due to webhook failure, for example), the
            #         # user would never be allowed to refund the source transaction again.
            #         refund_payments = self.search([('source_payment_id', '=', payment.id)])
            #         refunded_amount = abs(sum(refund_payments.mapped('amount')))
            #         print(payment.amount_available_for_refund)
            #         payment.amount_available_for_refund = payment.amount - refunded_amount
            #         print(payment.amount_available_for_refund)
            #
            #     else:
            #         print("BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB")
            #         print(payment.amount_available_for_refund)
            #         payment.amount_available_for_refund = 0
            #         print(payment.amount_available_for_refund)
            #     print("ZZZZZZZZZZZZZZZZ", payment.amount_available_for_refund)

            # except Exception as e:
            #     _logger.error("CRITICAL ERROR during _set_done() for transaction %s: %s", self.reference, e,
            #                   exc_info=True)
            #     # This will catch errors during post-processing and log the full traceback
            #     self._set_error(f"Post-processing failed: {e}")
            #     return False
            return False
        elif (payment_status == 'claimed'):
            talog("Order is claimed by a wallet")
        elif (payment_status == 'unpaid'):
            talog("Order is unpaid")
        else:
            tawarn("Received data with invalid payment status " + payment_status + " for transaction with reference " + self.reference + " and taler order id " + data.get('merchantOrderId'))
            tawarn("Setting this transaction as cancelled, with error")
            self._set_canceled()
            self._set_error("Taler: Received data with invalid payment status: " + payment_status)


    def _get_specific_rendering_values(self, values):
        new_values = super()._get_specific_rendering_values(values)
        if self.provider_code != 'taler':
            return new_values
        order_summary = "Odoo reference " + self.reference + " for " + str(self.amount) + str(self.currency_id.symbol) + " " + self.currency_id.name
        currency = self.currency_id.name # Gets the currency by name for the current order
        if self.provider_id.is_in_test_mode(): # Checks if provider used is currently in test mode
            currency = "KUDOS"
        self.getToken()
        expiration_time_in_epoch = get_datetime_now_to_epoch(15)  # Calculate the epoch seconds in 15 minutes, to be used in the Taler order creation to set a max payment date
        self.taler_order_id, self.taler_order_url, self.taler_order_uri = postPlaceOrderWithFulfillmentUrl(
                                                                                  self,
                                                                                  # currency,
                                                                                  "KUDOS",
                                                                                  # self.amount,
                                                                                  "0.02",
                                                                                  order_summary,
                                                                                  self.provider_id.fulfillment_message,
                                                                                  TalerController._fulfillment_url + "/" + self.taler_uuid,
                                                                                  expiration_time_in_epoch)  # Orders expire 15 minutes after creation
        rendering_values = {
            'taler_merchant_url': self.taler_order_url
        }
        tadebug("Order Taler Id: ", self.taler_order_id)
        tadebug("Order Reference: ", self.reference)

        return rendering_values

    def _get_orderid_status(self):
        return getOrderIdStatus(self)

    def _get_tx_from_notification_data(self, provider_code, notification_data):
        """Override of payment to find the transaction based on taler data."""
        transaction = super()._get_tx_from_notification_data(provider_code, notification_data)
        if provider_code != 'taler' or len(transaction) == 1:
            return transaction

        reference = notification_data.get('reference')
        if not reference:
            raise ValidationError("Taler: Received data with missing reference.")
        transaction = self.search([('reference', '=', reference), ('provider_code', '=', 'taler')])

        if not transaction:
            raise ValidationError("Taler: No transaction found matching reference " + reference)

        return transaction


    def _send_refund_request(self, amount_to_refund=None):
        print("RUNNING SEND REFUND REQUEST")
        print("TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT")
        self.ensure_one()

        if self.provider_code != 'taler':
            return super()._send_refund_request(amount_to_refund)

        # refund_amount is a float, may be partial
        #amount = refund_amount or self.amount
        # For now, only refund the full amount, and at later step, see if Taler can manage a partial refund
        amount = amount_to_refund or self.amount

        try:
            response = sendRefundForOrder(amount)
        except Exception as e:
            self._set_error(str(e))
            return

        print("Taler order id:")
        print(self.taler_order_id)

        self._process_refund_response(response)

    def _process_refund_response(self, response):
        print("PROCESSING REFUND RESPONSE")
        if response.get("status") == "success":
            self._set_done()
            self._post_process()
            self.provider_reference = response.get("refund_id")
            print("SETTING DONE INVOICING")
            print("payment_id: ", self.payment_id)
            print("calling post process")
            print("called post process")
        elif response.get("status") == "pending":
            #This one is useful for asynchronous refunds, which is not relevant for Taler refunds.
            #I can probably remove this "elif"
            self._set_pending()
            self.provider_reference = response.get("refund_id")
        else:
            self._set_error(response.get("error", "Refund failed"))
