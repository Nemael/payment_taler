from odoo import _, models
from odoo.exceptions import ValidationError

from odoo.addons.taler import const


class PaymentTransaction(models.Model):
    _inherit = 'payment.transaction'


    def _process_notification_data(self, notification_data):
        """ Override of payment to process the transaction based on Taler data.

        Note: self.ensure_one()

        :param dict notification_data: The notification data sent by the provider
        :return: None
        """
        super()._process_notification_data(notification_data)
        if self.provider_code != 'taler':
            print("Getting into wrong provider code??")
            return

        payment_data = self.provider_id._taler_make_request(
            f'/payments/{self.provider_reference}', method="GET"
        )

        # Update the payment method.
        payment_method_type = payment_data.get('method', '')
        if payment_method_type == 'creditcard':
            payment_method_type = payment_data.get('details', {}).get('cardLabel', '').lower()
        payment_method = self.env['payment.method']._get_from_code(
            payment_method_type, mapping=const.PAYMENT_METHODS_MAPPING
        )
        self.payment_method_id = payment_method or self.payment_method_id

        # Update the payment state.
        payment_status = payment_data.get('status')
        if payment_status == 'pending':
            self._set_pending()
        elif payment_status == 'authorized':
            self._set_authorized()
        elif payment_status == 'paid':
            self._set_done()
        elif payment_status in ['expired', 'canceled', 'failed']:
            self._set_canceled("Mollie: " + _("Cancelled payment with status: %s", payment_status))
        else:
            _logger.info(
                "received data with invalid payment status (%s) for transaction with reference %s",
                payment_status, self.reference
            )
            self._set_error(
                "Taler: " + _("Received data with invalid payment status: %s", payment_status)
            )
