from odoo import models, fields
import requests
# from ..utils import *
from ..utils.utils import *


class Welcome(models.Model):
    _name = 'tops.welcome'
    _description = 'This is the Taler-Odoo Payment System Welcome model.'

    test_summary = fields.Char(string="Test Order Summary", default="Test order")
    test_fulfilment_message = fields.Char(string="Test Order Fulfilment Message", default="Thank youze for your purchase!")
    test_currency = fields.Char(string="Test Order Currency", default="KUDOS")
    test_amount = fields.Char(string="Test Order Amount", default="1")
    test_latest_order_id = fields.Char(string="Test Latest Order Id", default="1")
    test_order_url = fields.Char(string="Test Last Order URL", default="")
    test_order_uri = fields.Char(string="Test Last Order URI", default="")
    test_merchant_refund_window = fields.Char(string="Test Merchant Refund Window", default="14")

    def create(self, vals):
        if self.search_count([]) > 0:
            raise ValidationError("Only one record of Welcome is allowed.")
        return super(Welcome, self).create(vals)

    def action_open_singleton(self):
        record = self.search([], limit=1)
        if not record:
            record = self.create({})
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'tops.welcome',
            'res_id': record.id,
            'view_mode': 'form',
            'view_id': self.env.ref('tops.view_form_tops_welcome').id,
            'target': 'current',
        }

    def requestGetToken(self):
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


    def requestGetOrderFromId(self):
        merchant_url = self.env['ir.config_parameter'].sudo().get_param('tops.merchant_url', default='')
        url = merchant_url + "/private/orders/" + self.test_latest_order_id
        payload = ""
        headers = {
            "User-Agent": "TalerOdoo",
            "Authorization": "Bearer " + self.env['ir.config_parameter'].sudo().get_param('tops.secret_token')
        }
        talog("Headers: ", headers)
        talog("Payload: ", payload)
        response = requests.request("GET", url, data=payload, headers=headers)
        talog("Response received")
        talog(response.text)
        if response.status_code != 200:
            talog("Error getting order from id, bad response: ", response.text)
            return


    def requestGetConfig(self):
        merchant_url = self.env['ir.config_parameter'].sudo().get_param('tops.merchant_url', default='')
        url = merchant_url + "/config"
        payload = ""
        headers = {"User-Agent": "TalerOdoo"}
        talog("Headers: ", headers)
        talog("Payload: ", payload)
        response = requests.request("GET", url, data=payload, headers=headers)
        talog("Response received")
        talog(response.text)
        if response.status_code != 200:
            talog("Error getting config, bad response: ", response.text)
            return


    def postPlaceOrder(self):
        merchant_url = self.env['ir.config_parameter'].sudo().get_param('tops.merchant_url', default='')
        url = merchant_url + "/private/orders"
        payload = {
            "order": {
                "amount": self.test_currency + ":" + self.test_amount,
                "summary": self.test_summary,
                "fulfilment_message": self.test_fulfilment_message
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
        new_order_record = self.createOrder(order_id, order_url)
        order_uri = self.getOrderTalerUri(order_id)
        new_order_record.uri = order_uri

        self.test_latest_order_id = order_id
        self.test_order_url = order_url
        self.test_order_uri = order_uri



    def getOrderTalerUri(self, order_id):
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

    def getSettingAndPrintIt(self):
        talog(self.env['ir.config_parameter'].sudo().get_param('tops.merchant_url', default=''))
        talog(self.env['ir.config_parameter'])

    def createOrder(self, taler_id, url):
        return(self.env['tops.order'].create({
            'taler_id': taler_id,
            'summary': self.test_summary,
            'fulfilment_message': self.test_fulfilment_message,
            'amount': self.test_amount,
            'currency': self.test_currency,
            'creation_time': fields.Datetime.now().isoformat(),
            'url': url,
            'merchant_refund_window': self.test_merchant_refund_window,
            'merchant_server': self.env['ir.config_parameter'].sudo().get_param('tops.merchant_url', default=''),
        }))

    def setSetting(self, setting, value):
        # To be integrated in the rest of the code
        self.env['ir.config_parameter'].sudo().set_param('tops.' + setting, value)
        talog(self.env['ir.config_parameter'].sudo().get_param('tops.secret_token'))

    def getSetting(self, setting,):
        # To be integrated in the rest of the code
        return self.env['ir.config_parameter'].sudo().get_param('tops.' + setting, default=''),
