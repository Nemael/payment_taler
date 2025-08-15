import requests
import pytest

class TestWelcome:
    def testPostPlaceOrder(requests_mock):
        url = 'https://backend.demo.taler.net/instances/sandbox/private/orders'
        data = {'orderid': '', 'age': 25}
        response = requests.post(url, json=data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()['name'], 'John')

    def testGetToken(self):
        response = requests.get('https://backend.demo.taler.net/instances/sandbox/private/orders')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('token' in response.json())
