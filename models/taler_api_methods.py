from odoo.addons.tops.utils.utils import talog, tawarn
import requests
from werkzeug import urls

#This is a temporary solution, I cannot do proper inheritance due to Odoo mixins, and this solution allows for some genericity that's enough for now+
def requestGetToken(model):
    talog("Getting token")
    print(model)
    print(model.provider_id)
    print(model.provider_id.taler_merchant_url)
    print("?")
    taler_url = getTalerUrl(model)
    talog(taler_url)
    url = taler_url + "/private/token"
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
    model.provider_id.taler_token = response.json()["token"]
    talog(model.provider_id.taler_token)

def getOrderTalerUri(model, order_id):
    taler_url = getTalerUrl(model)
    url = taler_url + "/private/orders/" + order_id

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

def postPlaceOrderWithFulfillmentMessage(model, currency, amount, summary, fulfillment_message):
    taler_url = getTalerUrl(model)
    url = taler_url + "/private/orders"
    payload = {
        "order": {
            "amount": currency + ":" + str(amount),
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
    order_url = taler_url + "/orders/" + order_id
    order_uri = getOrderTalerUri(model, order_id)
    print("??????????????????", order_uri)
    talog("order_id: ", order_id)

    return order_id, order_url, order_uri

def postPlaceOrderWithFulfillmentUrl(model, currency, amount, summary, fulfillment_message, fulfillment_url):
    taler_url = getTalerUrl(model)
    odoo_base_url = model.provider_id.get_base_url()
    url = taler_url + "/private/orders"
    payload = {
        "order": {
            "amount": currency + ":" + str(amount),
            "summary": summary,
            "fulfillment_message": fulfillment_message,
            'fulfillment_url': urls.url_join(odoo_base_url, fulfillment_url + "/" + model.reference)
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
        return None, None, None
    if "order_id" not in response.json():
        talog("Error getting new order_id: ", response.text)
        return None, None, None
    order_id = response.json()["order_id"]
    order_url = taler_url + "/orders/" + order_id
    order_uri = getOrderTalerUri(model, order_id)
    print("??????????????????", order_uri)
    talog("order_id: ", order_id)

    return order_id, order_url, order_uri


def requestGetOrderFromId(model):
    print(model.taler_order_id)
    taler_url = getTalerUrl(model)
    print(taler_url)
    url = taler_url + "/private/orders/" + model.taler_order_id
    payload = ""
    headers = {
        "User-Agent": "TalerOdoo",
        "Authorization": "Bearer " + model.env['ir.config_parameter'].sudo().get_param('tops.secret_token')
    }
    talog("requestGetOrderFromId logs")
    talog("URL: ", url)
    talog("Headers: ", headers)
    talog("Payload: ", payload)
    response = requests.request("GET", url, data=payload, headers=headers)
    talog("Response received: ", response.text)
    # talog(response.text)
    if response.status_code != 200:
        talog("Error getting order from id, bad response: ", response.text)
        return
    return response.json()

def checkOrderIsPaid(model):
    print("CHECK IF ORDER IS PAID")
    print("LATEST ORDER ID 2: ", model.taler_order_id)
    response = requestGetOrderFromId(model)
    print(response.json()["order_status"])
    return response.json()["order_status"] == "paid"

def getOrderIdStatus(model):
    print("GET ORDER STATUS")
    response = requestGetOrderFromId(model)
    print("RESPONSE: ", response)
    print("Order status:" + response["order_status"])
    return response["contract_terms"]["order_id"], response["order_status"]

def getTalerUrl(model):
    taler_url = model.provider_id.taler_merchant_url
    if not taler_url or taler_url == "":
        raise Exception("Taler URL is empty. Did you set it correctly in the provider view?")
    return model.provider_id.taler_merchant_url
