from odoo import _, models
from odoo.exceptions import ValidationError

from odoo.addons.tops import const
from werkzeug import urls
from odoo import models, fields
import requests
from odoo.addons.tops.utils.utils import *

from odoo.addons.tops.controllers.taler_controller import TalerController




class PaymentTransaction(models.Model):
    _inherit = 'payment.transaction'
    test_summary = fields.Char(string="Test Order Summary", default="Test order")
    test_fulfillment_message = fields.Char(string="Test Order Fulfilment Message", default="Thank youze for your purchase!")
    #test_fulfillment_url = fields.Char(string="Test Order Fulfilment Url", default="Thank youze for your purchase!")
    test_currency = fields.Char(string="Test Order Currency", default="KUDOS")
    test_amount = fields.Char(string="Test Order Amount", default="0.01")
    test_latest_order_id = fields.Char(string="Test Latest Order Id", default="1")
    test_order_url = fields.Char(string="Test Last Order URL", default="")
    test_order_uri = fields.Char(string="Test Last Order URI", default="")
    test_merchant_refund_window = fields.Char(string="Test Merchant Refund Window", default="14")

    #Real fields
    #Add "taler_" in front of each really used fields
    merchant_order_id = fields.Char(string="Merchant Order Id", default="")


    def _process_notification_data(self, data):
        print("PROCESSING TALER NOTIFICATION DATA")
        super()._process_notification_data(data)
        if self.provider_code != 'taler':
            print("Wrong provider code for trancaction. Provider_code: ", self.provider_code)
            return

        # payment_data = self.provider_id._taler_make_request(
        #     f'/payments/{self.provider_reference}', method="GET"
        # )

        # Update the payment method.
        # payment_method_type = payment_data.get('method', '')
        # if payment_method_type == 'creditcard':
        #     payment_method_type = payment_data.get('details', {}).get('cardLabel', '').lower()
        # payment_method = self.env['payment.method']._get_from_code(
        #     payment_method_type, mapping=const.PAYMENT_METHODS_MAPPING
        # )
        # self.payment_method_id = payment_method or self.payment_method_id

        # Update the payment state.
        payment_status = data.get('paymentStatus')
        print(payment_status)
        # if payment_status == 'pending':
        #     self._set_pending()
        # elif payment_status == 'authorized':
        #     self._set_authorized()
        # elif payment_status == 'paid':
        #     self._set_done()
        # elif payment_status in ['expired', 'canceled', 'failed']:
        #     self._set_canceled("Mollie: " + _("Cancelled payment with status: %s", payment_status))
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
        self._requestGetToken()
        self._postPlaceOrder()
        tawarn(self.test_order_url)
        tawarn(self.test_order_uri)


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
            'api_url': self.test_order_url
        })
        talog("rendering_values: ", rendering_values['api_url'])
        print("LATEST ORDER ID 4: ", self.merchant_order_id)
        print("!!!!!!!!!!!!!!!!! Order Reference", self.reference)
        # self.reference = self.merchant_order_id
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

    def _requestGetToken(self):
        talog("Getting token")
        merchant_url = self.env['ir.config_parameter'].sudo().get_param('tops.merchant_url', default='')
        talog(merchant_url)
        url = merchant_url + "/private/token"
        payload = {"scope": "write"}
        headers = {
            "Content-Type": "application/json",
            "User-Agent": "TalerOdoo",
            "Authorization": "Bearer secret-token:" + self.env['ir.config_parameter'].sudo().get_param('tops.password', default='')
        }
        talog("Headers: ", headers)
        talog("Payload: ", payload)
        response = requests.request("POST", url, json=payload, headers=headers)
        talog("Response received")
        talog(response.text)
        if response.status_code != 200:
            talog("Error getting token, bad response: ", response.text)
            return
        if "token" not in response.json():
            talog("Error getting new token: ", response.text)
            return
        self.env['ir.config_parameter'].sudo().set_param('tops.secret_token', response.json()["token"])
        talog(self.env['ir.config_parameter'].sudo().get_param('tops.secret_token'))

    def _createOrderInOdoo(self, taler_id, url):
        #DELETE THIS ONE
        return (self.env['tops.order'].create({
            'taler_id': taler_id,
            'summary': self.test_summary,
            'fulfilment_message': self.test_fulfillment_message,
            'amount': self.test_amount,
            'currency': self.test_currency,
            'creation_time': fields.Datetime.now().isoformat(),
            'url': url,
            'merchant_refund_window': self.test_merchant_refund_window,
            'merchant_server': self.env['ir.config_parameter'].sudo().get_param('tops.merchant_url', default=''),
        }))

    def _getOrderTalerUri(self, order_id):
        merchant_url = self.env['ir.config_parameter'].sudo().get_param('tops.merchant_url', default='')
        url = merchant_url + "/private/orders/" + order_id

        payload = ""
        headers = {
            "User-Agent": "TalerOdoo/insomnia/11.3.0",
            "Authorization": "Bearer " + self.env['ir.config_parameter'].sudo().get_param('tops.secret_token')
        }
        talog("Headers: ", headers)
        talog("Payload: ", payload)
        response = requests.request("GET", url, data=payload, headers=headers)
        talog("Response received")
        if response.status_code != 200:
            talog("Error getting order taler payment URI, bad response: ", response.text)
            return ''
        if "taler_pay_uri" not in response.json():
            talog("Error getting taler_pay_uri field: ", response.text)
            return ''
        return response.json()["taler_pay_uri"]

    def _postPlaceOrder(self):
        merchant_url = self.env['ir.config_parameter'].sudo().get_param('tops.merchant_url', default='')
        url = merchant_url + "/private/orders"
        odoo_base_url = self.provider_id.get_base_url()
        print('@@@@@@@@@@@@@@@@@@@@@@@@@' + urls.url_join(odoo_base_url, TalerController._fulfillment_url + "/${ORDER_ID}"))
        payload = {
            "order": {
                "amount": self.test_currency + ":" + self.test_amount,
                "summary": self.test_summary,
                "fulfillment_message": self.test_fulfillment_message,
                # 'fulfillment_url': urls.url_join(odoo_base_url, TalerController._fulfillment_url + "/${ORDER_ID}")
                'fulfillment_url': urls.url_join(odoo_base_url, TalerController._fulfillment_url + "/" + self.reference)
            },
            "create_token": False
        }
        talog(self.env['ir.config_parameter'].sudo().get_param('tops.secret_token'))
        headers = {
            "Content-Type": "application/json",
            "User-Agent": "TalerOdoo/insomnia/11.3.0",
            "Authorization": "Bearer " + self.env['ir.config_parameter'].sudo().get_param('tops.secret_token')
        }
        talog("Headers: ", headers)
        talog("Payload: ", payload)
        response = requests.request("POST", url, json=payload, headers=headers)
        talog("Response received")
        talog(response.text)
        if response.status_code != 200:
            talog("Error placing order, bad response: ", response.text)
            return
        if "order_id" not in response.json():
            talog("Error getting new order_id: ", response.text)
            return
        order_id = response.json()["order_id"]
        order_url = merchant_url + "/orders/" + order_id
        new_order_record = self._createOrderInOdoo(order_id, order_url)
        order_uri = self._getOrderTalerUri(order_id)
        new_order_record.uri = order_uri
        talog("order_id: ", order_id)

        self.merchant_order_id = order_id
        self.test_order_url = order_url
        self.test_order_uri = order_uri
        print("LATEST ORDER ID 1: ", self.merchant_order_id)

    def _check_if_order_is_paid(self):
        print("CHECK IF ORDER IS PAID")
        print("LATEST ORDER ID 2: ", self.merchant_order_id)
        response = self.requestGetOrderFromId()
        print(response.json()["order_status"])
        return response.json()["order_status"] == "paid"

    def _get_orderid_status(self):
        print("GET ORDER STATUS")
        response = self.requestGetOrderFromId()
        print("RESPONSE: ", response.json())
        print("Order status:" + response.json()["order_status"])
        return (response.json()["contract_terms"]["order_id"], response.json()["order_status"])


    def requestGetOrderFromId(self):
        print(self.merchant_order_id)
        merchant_url = self.env['ir.config_parameter'].sudo().get_param('tops.merchant_url', default='')
        print(merchant_url)
        url = merchant_url + "/private/orders/" + self.merchant_order_id
        payload = ""
        headers = {
            "User-Agent": "TalerOdoo",
            "Authorization": "Bearer " + self.env['ir.config_parameter'].sudo().get_param('tops.secret_token')
        }
        talog("Headers: ", headers)
        talog("Payload: ", payload)
        response = requests.request("GET", url, data=payload, headers=headers)
        talog("Response received")
        # talog(response.text)
        if response.status_code != 200:
            talog("Error getting order from id, bad response: ", response.text)
            return
        return(response)
