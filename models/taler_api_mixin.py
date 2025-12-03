from odoo.addons.tops.utils.utils import talog, tawarn
import requests


def requestGetToken(model):
    talog("Getting token")
    merchant_url = model.env['ir.config_parameter'].sudo().get_param('tops.merchant_url', default='')
    talog(merchant_url)
    url = merchant_url + "/private/token"
    payload = {"scope": "write"}
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "TalerOdoo",
        "Authorization": "Bearer secret-token:" + model.env['ir.config_parameter'].sudo().get_param('tops.password', default='')
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
    model.env['ir.config_parameter'].sudo().set_param('tops.secret_token', response.json()["token"])
    talog(model.env['ir.config_parameter'].sudo().get_param('tops.secret_token'))

def getOrderTalerUri(model, order_id):
    merchant_url = model.env['ir.config_parameter'].sudo().get_param('tops.merchant_url', default='')
    url = merchant_url + "/private/orders/" + order_id

    payload = ""
    headers = {
        "User-Agent": "TalerOdoo/insomnia/11.3.0",
        "Authorization": "Bearer " + model.env['ir.config_parameter'].sudo().get_param('tops.secret_token')
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

def postPlaceOrder(model, currency, amount, summary, fulfillment_message):
    merchant_url = model.env['ir.config_parameter'].sudo().get_param('tops.merchant_url', default='')
    url = merchant_url + "/private/orders"
    payload = {
        "order": {
            "amount": currency + ":" + amount,
            "summary": summary,
            "fulfillment_message": fulfillment_message,
        },
        "create_token": False
    }
    talog(model.env['ir.config_parameter'].sudo().get_param('tops.secret_token'))
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "TalerOdoo/insomnia/11.3.0",
        "Authorization": "Bearer " + model.env['ir.config_parameter'].sudo().get_param('tops.secret_token')
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
    order_uri = getOrderTalerUri(model, order_id)
    print("??????????????????", order_uri)
    talog("order_id: ", order_id)

    return order_id, order_url, order_uri
