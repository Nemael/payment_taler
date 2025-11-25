from odoo import _, models
from odoo.exceptions import ValidationError

from odoo.addons.tops import const
from ..utils.utils import *



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

    def _get_specific_rendering_values(self, values):
        tawarn('Processing rendering values')
        new_values = super()._get_specific_rendering_values(values)
        if self.provider_code != 'taler':
            return new_values

        base_url = self.provider_id.get_base_url()
        # if self.fees:
            # Similarly to what is done in `payment::payment.transaction.create`, we need to round
            # the sum of the amount and of the fees to avoid inconsistent string representations.
            # E.g., str(1111.11 + 7.09) == '1118.1999999999998'
            # total_fee = self.currency_id.round(self.amount + self.fees)
        # else:
        #     total_fee = self.amount
        rendering_values = {
            '_input_charset': 'utf-8',
            'notify_url': 'abcd', #urls.url_join(base_url, KashierController._webhook_url),
            'out_trade_no': 'dddddo', #self.reference,
            'partner': 'tttt', #self.provider_id.kashier_merchant_id,
            'kashier_key': 'pppppo', #self.provider_id.kashier_key,
            'return_url': 'sssss', #urls.url_join(base_url, KashierController._return_url),
            'subject': 'araaaaa', #self.reference,

            "allowedMethods": "taler", #"card,wallet,bank_installments",
            'total_fee': f'4' #f'{total_fee:.2f}',
        }
        # if self.provider_id.kashier_payment_method == 'standard_checkout':
        #     # https://global.kashier.com/docs/ac/global/create_forex_trade
        #     rendering_values.update({
        #         'service': 'create_forex_trade',
        #         'product_code': 'NEW_OVERSEAS_SELLER',
        #         'currency': self.currency_id.name,
        #     })
        # else:
        #     rendering_values.update({
        #         'service': 'create_direct_pay_by_user',
        #         'payment_type': 1,
        #     })
        #
        # sign = self.provider_id._kashier_compute_signature(rendering_values)
        # rendering_values.update({
        #     'mode': self.provider_id._kashier_get_mode(),
        #     'sign': sign,
        #     'api_url': self.provider_id._kashier_get_api_url(),
        # })
        tawarn(rendering_values)
        return rendering_values

    def _get_specific_secret_keys(self):
        tawarn('get specific secret keys')
        new_values = super()._get_specific_secret_keys()
        if self.provider_code != 'taler':
            return new_values
        key = {'talerpass': 'secret taler password'}
        return (key)

    def _send_payment_request(self):
        tawarn('send payment request')
        super()._send_payment_request()
        if self.provider_code != 'taler':
            return
        return
