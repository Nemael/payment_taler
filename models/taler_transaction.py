# SPDX-FileCopyrightText: 2025 Mael Panouillot <panouillot.mael@gmail.com>
#
# SPDX-License-Identifier: LGPL-3.0-or-later

from odoo.exceptions import ValidationError
from odoo import models, fields
from odoo.addons.tops.utils.utils import talog, tawarn, tadebug, generate_UUID, get_datetime_now_to_epoch
from odoo.addons.tops.models.taler_api_methods import requestGetToken, postPlaceOrderWithFulfillmentUrl, getOrderTalerUri, requestGetOrderFromId, getOrderIdStatus, checkOrderIsPaid
from odoo.addons.tops.controllers.taler_controller import TalerController


class TalerTransaction(models.Model):
    _inherit = 'payment.transaction'
    #Because this model inherits, and does not have its own name, there is no need for it to appear in ir.model.access.csv
    #It will inherit the ir security settings from the account.move model

    taler_order_id = fields.Char(string="Taler Order ID", default="")
    taler_order_url = fields.Char(string="Taler Order URL", default="")
    taler_order_uri = fields.Char(string="Taler Order URI", default="")
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
            talog("Order paid")
            self._set_done()
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
                                                                                  currency,
                                                                                  self.amount,
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
