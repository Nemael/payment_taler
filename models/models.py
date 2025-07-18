from odoo import models, fields
import requests
# from ..utils import *
from ..utils.utils import *

class Student(models.Model):
    _name = 'wb.student'
    _description = 'This is student profile.'
    name = fields.Char(string="Name")
    description = fields.Text(string="Description")


    name1 = fields.Char(string="Name1")
    name2 = fields.Char(string="Name2")
    name3 = fields.Char(string="Name3")
    name4 = fields.Char(string="Name4")
    taler_url = fields.Char(string="Taler URL", default="https://backend.demo.taler.net/instances/sandbox")
    secret_token = fields.Char(string="Current Secret Token")
    test_order_id = fields.Char(string="Test OrderID", default="2025.191-02D3GX2J9ME3M")

    order_summary  = fields.Char(string="Order Summary", default="Test order")
    order_fullfilment_message = fields.Char(string="Order Fulfillment Message", default="Thank youze for your purchase!")
    order_currency = fields.Char(string="Order Currency", default="KUDOS")
    order_amount = fields.Char(string="Order Amount", default="1")
    order_latest_order_id = fields.Char(string="Latest Order Id", default="1")
    order_last_order_url = fields.Char(string="Last Order URL", default="")

    last_order_uri = fields.Char(string="Last Order URI", default="")

    merchant_refund_window = fields.Char(string="Merchant Refund Window", default="14")

    def changeRecord(self):
        self.name4 = self.name4 + '+'
        print('Starting transaction')

    def requestGetToken(self):
        talog("Getting token")
        url = self.taler_url + "/private/token"
        payload = {"scope": "write"}
        headers = {
            "Content-Type": "application/json",
            "User-Agent": "TalerOdoo",
            "Authorization": "Bearer secret-token:sandbox"
        }
        talog("Headers: ", headers)
        talog("Payload: ", payload)
        response = requests.request("POST", url, json=payload, headers=headers)
        print("Response received")
        talog(response.text)
        if response.status_code != 200:
            talog("Error getting token, bad response: ", response.text)
            return
        if "token" not in response.json():
            talog("Error getting new token: ", response.text)
            return
        self.secret_token = response.json()["token"]

    def requestGetOrderFromId(self):
        url = self.taler_url + "/private/orders/" + self.test_order_id
        payload = ""
        headers = {
            "User-Agent": "TalerOdoo",
            "Authorization": "Bearer " + self.token
        }
        talog("Headers: ", headers)
        talog("Payload: ", payload)
        response = requests.request("GET", url, data=payload, headers=headers)
        print("Response received")
        talog(response.text)
        if response.status_code != 200:
            talog("Error getting order from id, bad response: ", response.text)
            return

    def requestGetConfig(self):
        url = self.taler_url + "/config"
        payload = ""
        headers = {"User-Agent": "TalerOdoo"}
        talog("Headers: ", headers)
        talog("Payload: ", payload)
        response = requests.request("GET", url, data=payload, headers=headers)
        print("Response received")
        talog(response.text)
        if response.status_code != 200:
            talog("Error getting config, bad response: ", response.text)
            return

    def postPlaceOrder(self):
        url = self.taler_url + "/private/orders"
        payload = {
            "order": {
                "amount": self.order_currency + ":" + self.order_amount,
                "summary": self.order_summary,
                "fullfilment_message": self.order_fullfilment_message
            },
            "create_token": False
        }
        headers = {
            "Content-Type": "application/json",
            "User-Agent": "TalerOdoo/insomnia/11.3.0",
            "Authorization": "Bearer " + self.secret_token
        }
        talog("Headers: ", headers)
        talog("Payload: ", payload)
        response = requests.request("POST", url, json=payload, headers=headers)
        print("Response received")
        talog(response.text)
        if response.status_code != 200:
            talog("Error placing order token, bad response: ", response.text)
            return
        if "order_id" not in response.json():
            talog("Error getting new order_id: ", response.text)
            return
        self.order_latest_order_id = response.json()["order_id"]
        self.order_last_order_url = self.taler_url + "/orders/" + self.order_latest_order_id

    def getOrderTalerUri(self):
        url = "https://backend.demo.taler.net/instances/sandbox/private/orders/" + self.order_latest_order_id

        payload = ""
        headers = {
            "User-Agent": "TalerOdoo/insomnia/11.3.0",
            "Authorization": "Bearer " + self.secret_token
        }
        talog("Headers: ", headers)
        talog("Payload: ", payload)
        response = requests.request("GET", url, data=payload, headers=headers)
        print("Response received")
        if response.status_code != 200:
            talog("Error getting order talery payment URI, bad response: ", response.text)
            return
        if "taler_pay_uri" not in response.json():
            talog("Error getting taler_pay_uri field: ", response.text)
            return
        self.last_order_uri = response.json()["taler_pay_uri"]
