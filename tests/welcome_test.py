# import requests
# import pytest
# from ..utils.utils import *
#
# class TestWelcome:
#     """def testPostPlaceOrder(requests_mock):
#         url = 'https://backend.demo.taler.net/instances/sandbox/private/orders'
#         data = {'orderid': '', 'age': 25}
#         response = requests.post(url, json=data)
#         self.assertEqual(response.status_code, 201)
#         self.assertEqual(response.json()['token'], 'abcdefgh')"""
#
#     def testUnitTest():
#         assert squareNumber(5) == 25
#
#     """def testGetToken(self):
#         response = requests.get('https://backend.demo.taler.net/instances/sandbox/private/orders')
#         self.assertEqual(response.status_code, 200)
#         self.assertTrue('token' in response.json())"""


from odoo.tests.common import TransactionCase
from odoo.exceptions import UserError
from odoo.tests import tagged

# The CI will run these tests after all the modules are installed,
# not right after installing the one defining it.
@tagged('post_install', '-at_install')
class SimpleTest(TransactionCase):

    @classmethod
    def setUpClass(cls):
        # add env on cls and many other things
        super(SimpleTest, cls).setUpClass()

        # create the data for each test. By doing it in the setUpClass instead
        # of in a setUp or in each test case, we reduce the testing time and
        # the duplication of code.
        cls.welcome = cls.env['tops.welcome'].create([...])

    def test_creation_area(self):
        """Test that the merchantUrl is sanitized like it should."""
        self.welcome.merchant_url = 'https://backend.demo.taler.net/instances/sandbox///'
        self.assertRecordValues(self.welcome, [
           {'merchant_url': "https://backend.demo.taler.net/instances/sandbox"},
           {'merchant_url': "https://backend.demo.taler.net/instances/sandbox"},
        ])


    # def test_action_sell(self):
    #     """Test that everything behaves like it should when selling a property."""
    #     self.properties.action_sold()
    #     self.assertRecordValues(self.properties, [
    #        {'name': ..., 'state': ...},
    #        {'name': ..., 'state': ...},
    #     ])
    #
    #     with self.assertRaises(UserError):
    #         self.properties.forbidden_action_on_sold_property()
