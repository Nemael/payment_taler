from odoo.tests.common import TransactionCase
from odoo.exceptions import UserError
from odoo.tests import tagged, TransactionCase

from odoo.addons.payment.tests.common import PaymentCommon

# @tagged('taler', 'post_install', '-at_install')
@tagged('taler')
class TestTalerCommon(PaymentCommon):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Unit test setUpClass")

        cls.currency_eur = cls._prepare_currency('EUR')
        cls.currency_chf = cls._prepare_currency('CHF')
        cls.currency_zar = cls._prepare_currency('ZAR')
        cls.taler = cls._prepare_provider('taler', update_values={
            'taler_merchant_url': 'https://backend.demo.taler.net/instances/sandbox',
            'taler_merchant_password': 'dummy password',
            'taler_token': 'dummy token',
            'fulfillment_message': 'dummy fulfillment message'
        })

        cls.provider = cls.taler
        cls.currency = cls.currency_chf

        cls.notification_data = {'reference': '01234567899876543210',
                                 'merchantOrderId': '98765432100123456789',
                                 'paymentStatus': 'paid'
        }
        # cls.notification_data = {
        #     'currency': 'EGP',
        #     'notify_id': '1234567890123456789012345678901234',
        #     'notify_time': '2021-12-01 01:01:01',
        #     'notify_type': 'trade_status_sync',
        #     'out_trade_no': cls.reference,
        #     'sign': '782b6d1015549f847e2ab27d1edb65c7',
        #     'sign_type': 'MD5',
        #     'total_fee': '1111.11',
        #     'trade_no': '2021111111111111111111111111',
        #     'trade_status': 'TRADE_FINISHED',
        # }


    # def test_creation_area(self):
    #     """Test that the merchantUrl is sanitized like it should."""
    #     self.welcome.merchant_url = 'https://backend.demo.taler.net/instances/sandbox///'
    #     self.assertRecordValues(self.welcome, [
    #        {'merchant_url': "https://backend.demo.taler.net/instances/sandbox"},
    #        {'merchant_url': "https://backend.demo.taler.net/instances/sandbox"},
    #     ])


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
