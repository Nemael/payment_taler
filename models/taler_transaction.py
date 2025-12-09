from odoo import _, models
from odoo.exceptions import ValidationError

from odoo.addons.tops import const
from odoo import models, fields
import requests
from odoo.addons.tops.utils.utils import talog, tawarn

from odoo.addons.tops.models.taler_api_methods import requestGetToken, postPlaceOrderWithFulfillmentUrl, getOrderTalerUri, requestGetOrderFromId, getOrderIdStatus, generateUUID

from odoo.addons.tops.controllers.taler_controller import TalerController

from werkzeug import urls

from odoo.http import request




class PaymentTransaction(models.Model):
    _inherit = 'payment.transaction'
    test_summary = fields.Char(string="Test Order Summary", default="Test order")
    test_merchant_refund_window = fields.Char(string="Test Merchant Refund Window", default="14")

    #Real fields
    #Add "taler_" in front of each really used fields
    taler_order_id = fields.Char(string="Taler Order Id", default="")
    taler_order_url = fields.Char(string="Taler Order Url", default="")
    taler_order_uri = fields.Char(string="Taler Order Uri", default="")
    taler_uuid = fields.Char(string="Taler UUID", default="")


    def _process_notification_data(self, data):
        print("PROCESSING TALER NOTIFICATION DATA")
        super()._process_notification_data(data)
        if self.provider_code != 'taler':
            print("Getting not taler provider code: ", self.provider_code)
            return

        # Update the payment state.
        payment_status = data.get('paymentStatus')
        print(payment_status)
        if (payment_status == 'paid'):
            talog("Order paid")
            self._set_done()
        elif (payment_status == 'claimed'):
            talog("Order is claimed by a wallet")
        elif (payment_status == 'unpaid'):
            talog("Order is unpaid")
        else:
            talog(
                "Received data with invalid payment status (%s) for transaction with reference %s and taler order id %s",
                payment_status, self.reference, data.get('merchantOrderId')
            )
            self._set_error(
                "Taler: " + _("Received data with invalid payment status: %s", payment_status)
            )


    def _get_specific_rendering_values(self, values):
        tawarn('Processing rendering values')
        new_values = super()._get_specific_rendering_values(values)
        print("aaaaa", self.amount)
        print("aaaaa", self.currency_id)
        print("aaaaa", self.currency_id.name)
        print("aaaaa", self.currency_id.symbol)
        order_summary = "Odoo reference " + self.reference + " for " + str(self.amount) + str(self.currency_id.symbol) + " " + self.currency_id.name
        print("?????", self.provider_id.taler_token)
        requestGetToken(self)
        print("?????", self.provider_id.taler_token)
        print(">>>>>>>>>>>>>", self.reference)
        print(">>>>>>>>>>>>>", TalerController._fulfillment_url)

        #This UUID is only used for the fulfillment url. Without the UUID in the url, the Taler merchant could mix up two orders with the same Odoo ID, on two different Odoo instances
        #This is not a perfect solution, as two duplicate UUID + OrderID could be generated on two different Odoo instances, on the same Taler Merchant, but this is highly unlikely.
        self.taler_uuid = generateUUID()
        self.taler_order_id, self.taler_order_url, self.taler_order_uri = postPlaceOrderWithFulfillmentUrl(
                                                                                  self,
                                                                                  #self.currency_id.name,
                                                                                  "KUDOS", #testing value, remove for release and uncomment line above
                                                                                  #self.amount,
                                                                                  "0.01", #testing amount, remove for release and uncomment line above
                                                                                  order_summary,
                                                                                  self.provider_id.fulfillment_message,
                                                                                  TalerController._fulfillment_url + "/" + self.taler_uuid)
        tawarn(self.taler_order_url)
        tawarn(self.taler_order_uri)

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

        # I can remove these and clean up the related xml file
        rendering_values = {
            '_input_charset': 'utf-8',
            'notify_url': 'abcd', #urls.url_join(base_url, TalerController._webhook_url),
            'out_trade_no': 'dddddo', #self.reference,
            'partner': 'tttt', #self.provider_id.kashier_merchant_id,
            'return_url': urls.url_join(base_url, TalerController._fulfillment_url),
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
        rendering_values.update({
            'api_url': self.taler_order_url
        })
        talog("rendering_values: ", rendering_values['api_url'])
        print("LATEST ORDER ID 4: ", self.taler_order_id)
        print("!!!!!!!!!!!!!!!!! Order Reference", self.reference)
        # self.reference = self.taler_order_id
        # print("!!!!!!!!!!!!!!!!!", self.reference)

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

    def _get_orderid_status(self):
        return getOrderIdStatus(self)
