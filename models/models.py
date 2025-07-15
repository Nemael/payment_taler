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
    token = fields.Char(string="Current Token")
    test_order_id = fields.Char(string="Test OrderID", default="2025.191-02D3GX2J9ME3M")

    order_summary  = fields.Char(string="Order Summary", default="Test order")
    order_fullfilment_message = fields.Char(string="Order Fulfillment Message", default="Thank youze for your purchase!")
    order_currency = fields.Char(string="Order Currency", default="KUDOS")
    order_amount = fields.Char(string="Order Amount", default="1")
    order_latest_order_id = fields.Char(string="Latest Order Id", default="1")

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
        response = requests.request("POST", url, json=payload, headers=headers)
        print("Request received")
        talog(response.text)
        if response.status_code != 200:
            talog("Error getting token, bad response: ", response.text)
            return
        if response.json()["token"] is None:
            talog("Error getting new token: ", response.text)
            return
        self.token = response.json()["token"]

    def requestGetOrderFromId(self):
        url = self.taler_url + "/private/orders/" + self.test_order_id
        payload = ""
        headers = {
            "User-Agent": "TalerOdoo",
            "Authorization": "Bearer " + self.token
        }
        response = requests.request("GET", url, data=payload, headers=headers)
        talog(response.text)

    def requestGetConfig(self):
        url = self.taler_url + "/config"
        payload = ""
        headers = {"User-Agent": "TalerOdoo"}
        response = requests.request("GET", url, data=payload, headers=headers)
        talog(response.text)

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
            "Authorization": "Bearer secret-token:BSE1SCQR7B8WKR9PW79K6VV9K99RND95HNX0VPW9B4JVR8DYQAQG"
        }
        response = requests.request("POST", url, json=payload, headers=headers)
        talog(response.text)
        if response.status_code != 200:
            talog("Error getting token, bad response: ", response.text)
            return
        if response.json()["order_id"] is None:
            talog("Error getting new order_id: ", response.text)
            return
        self.order_latest_order_id = response.json()["order_id"]