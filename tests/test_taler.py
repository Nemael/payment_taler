from datetime import datetime, time, timedelta
from unittest.mock import patch

from werkzeug.exceptions import Forbidden

from odoo.exceptions import ValidationError
from odoo.tests import tagged, TransactionCase
from odoo.tools import mute_logger

import json
import random
import string

from unittest.mock import patch, Mock

from odoo.addons.tops.utils.utils import talog, generate_qr, generate_UUID, get_datetime_date_to_epoch, get_datetime_now_to_epoch

from odoo.addons.payment.tests.http_common import PaymentHttpCommon
from odoo.addons.tops.controllers.taler_controller import TalerController
from odoo.addons.tops.tests.test_taler_common import TestTalerCommon

@tagged('taler')
class TestTaler(TestTalerCommon, PaymentHttpCommon):
    def test_compatible_providers(self):
        # Tests if the list of compatible providers for EUR and CHF include Taler, and do not include other currencies, such as ZAR
        talog("Unit test test_compatible_providers")
        providers = self.env['payment.provider']._get_compatible_providers(
            self.company.id, self.partner.id, self.amount, currency_id=self.currency_eur.id
        )
        self.assertIn(self.taler, providers)

        providers = self.env['payment.provider']._get_compatible_providers(
            self.company.id, self.partner.id, self.amount, currency_id=self.currency_chf.id
        )
        self.assertIn(self.taler, providers)

        providers = self.env['payment.provider']._get_compatible_providers(
            self.company.id, self.partner.id, self.amount, currency_id=self.currency_zar.id
        )
        self.assertNotIn(self.taler, providers)

    def test_get_taler_token(self):
        # Tests if the token-fetching method updates the provider settings properly
        talog("Unit test test_get_taler_token")
        provider = self.env['payment.provider'].search([('code', '=', 'taler')], limit=1)
        # This randomly generated string is used to create a random token string value, to check that the provider's field is being updated properly
        mocked_random_secret_taler_token = "secret-token:mocked_access_token" + ''.join(random.choice(string.ascii_lowercase) for i in range(10))
        mock_response_token = Mock()
        mock_response_token.status_code = 200
        mock_response_token.json.return_value = {
            "access_token": mocked_random_secret_taler_token,
            "token": mocked_random_secret_taler_token,
            "scope": "write",
            "refreshable": False,
            "expiration": {"t_s": 1234567890},
        }

        self.assertEqual(provider.taler_token, "dummy token")
        transaction = self._create_transaction(flow='redirect')  # Only flow implemented
        with patch('requests.request', side_effect=[mock_response_token]) as mock_get:
            transaction.getToken()
        self.assertEqual(provider.taler_token, mocked_random_secret_taler_token)


    def test_taler_redirect_form(self):
        # Tests the value of the redirect form used by Odoo when a transaction is processed
        # Also tests that the transaction's internal values are updated appropriately
        talog("Unit test test_taler_redirect_form")
        transaction = self._create_transaction(flow='redirect')  # Only flow implemented

        mock_response_token = Mock()
        mock_response_token.status_code = 200
        mock_response_token.json.return_value = {
            "access_token": "secret-token:mocked_access_token",
            "token": "secret-token:mocked_secret_token",
            "scope": "write",
            "refreshable": False,
            "expiration": {"t_s": 1234567890},
        }

        mock_response_place_order = Mock()
        mock_response_place_order.status_code = 200
        mock_response_place_order.json.return_value = {
            "order_id": "mock.order-id"
        }

        mock_response_get_uri = Mock()
        mock_response_get_uri.status_code = 200
        mock_response_get_uri.json.return_value = {
            "taler_pay_uri": "taler://mock_taler_uri",
            "order_status_url": "https://mock_status_url",
            "order_status": "unpaid",
            "total_amount": "KUDOS:0.01",
            "summary": "Odoo reference S_MOCK for 0.01$ EUR",
            "creation_time": {"t_s": 1234567890}
        }

        with patch('requests.request', side_effect=[mock_response_token, mock_response_place_order, mock_response_get_uri]) as mock_get:
            processing_values = transaction._get_processing_values()
        redirect_form_data = self._extract_values_from_html_form(processing_values['redirect_form_html'])

        self.assertEqual(
            redirect_form_data['action'],
            'https://backend.demo.taler.net/instances/sandbox/orders/mock.order-id',
        )

        # Checks that the action is the mock url
        self.assertEqual(
            redirect_form_data['action'],
            "https://backend.demo.taler.net/instances/sandbox/orders/mock.order-id",
            "Taler: invalid action specified in the redirect form: " + str(redirect_form_data['action'])
        )
        #Checks that the received method is "get"
        self.assertEqual(
            redirect_form_data['method'],
            "get",
            "Taler: invalid method specified in the redirect form: " + str(redirect_form_data['method'])
        )
        #Checks that the received inputs are an empty dict
        self.assertDictEqual(
            redirect_form_data['inputs'],
            {},
            "Taler: invalid inputs specified in the redirect form: " + str(redirect_form_data['inputs'])
        )

    def test_taler_redirect_processing(self):
        # Test that a transaction is indeed completed once receiving the "paid" value from Mocked Taler response
        talog("Unit test test_taler_redirect_processing")
        with self.assertRaises(ValidationError):
            self.env['payment.transaction']._handle_notification_data(
                'taler', self.notification_data
            )

        transaction = self._create_transaction('redirect')
        self.notification_data['reference'] = transaction.reference
        data = {'reference': transaction.reference,
                                 'merchantOrderId': '98765432100123456789',
                                 'paymentStatus': 'paid'
        }
        self.env['payment.transaction']._handle_notification_data('taler', data)
        self.assertEqual(transaction.state, 'done')
        self.assertEqual(transaction.provider_reference, self.notification_data['merchantOrderId'])

    def test_check_if_order_is_paid(self):
        # Tests the generation of an invoice
        talog("Unit test test_check_if_order_is_paid")
        transaction = self._create_transaction(flow='redirect')  # Only flow implemented
        mock_response_is_paid_incorrect = Mock()
        mock_response_is_paid_incorrect.status_code = 200
        mock_response_is_paid_incorrect.json.return_value = {
            "taler_pay_uri": "taler://mock_taler_uri",
            "order_status_url": "https://mock_status_url",
            "order_status": "unpaid",
            "total_amount": "KUDOS:0.01",
            "summary": "Odoo reference S0MOCK for 0.01$ EUR",
            "creation_time": {"t_s": 1234567890}
        }
        mock_response_is_paid_correct = Mock()
        mock_response_is_paid_correct.status_code = 200
        mock_response_is_paid_correct.json.return_value = {
            "taler_pay_uri": "taler://mock_taler_uri",
            "order_status_url": "https://mock_status_url",
            "order_status": "paid",
            "total_amount": "KUDOS:0.01",
            "summary": "Odoo reference S0MOCK for 0.01$ EUR",
            "creation_time": {"t_s": 1234567890}
        }
        with patch('requests.request', side_effect=[mock_response_is_paid_incorrect]) as mock_get:
            paid_status = transaction.isPaid()
        self.assertEqual(paid_status, False)
        with patch('requests.request', side_effect=[mock_response_is_paid_correct]) as mock_get:
            paid_status = transaction.isPaid()
        self.assertEqual(paid_status, True)

    def test_generate_uuid(self):
        # Tests that the uuid generation does not produce two duplicates in a row
        talog("Unit test test_generate_uuid")
        uuid1 = generate_UUID()
        uuid2 = generate_UUID()
        self.assertNotEqual(uuid1, uuid2)

    def test_qr_creation(self):
        # Tests that the QR code generation stays consistent
        talog("Unit test test_qr_creation")
        mock_uri = "taler://mock_taler_uri"
        expected_qr = "iVBORw0KGgoAAAANSUhEUgAAASIAAAEiAQAAAAB1xeIbAAAB7UlEQVR4nO2aTW7bMBCFvykJeEkDPUCOQt2gZ+qRegPpKDlAAHIZgMLrgpSdZNNuFP1RK9H+AD/Yj08zQ5v49zX9+A8IOtWpA1HZ2jUANmQzAJZX/Va6LkE5SZIgezSGAmQPUZKUttN1DarZm9mY7k5Md6gbYthU17kp/2nlisVXX4jp58a6LkeFAoT3xe3f8ImXpqrvl0Jz9u2u/goC8ja6rkLNtaCBfJMN+VafukxmZnbfTtfZKd/sDTSPh1IXH5uuvao/PJXb89YGZtPIbEvoz933a1LUCj4mJ404QZA0BkkjUCv/ca/qj009aszZ2k32xcAQ4c0zDa7sV/0ZqMXjpfW1UUtzu62uc1MeQvEGYACKCTSZkxHeli9/r+qPTSEltwR8kIjJCXDSGErP+zWpZ957CCB4N02/EgY39bxfkaq+f1Y31ffxmfzJdd+vRH3InLqO6fneI332qv7wVLX3cwcUNOLq6L6N83es/sBU662AelhSfV+DJz12xV7VH5vygKsTHIPZa3oRNt0dIrvSxjt7VX8Gajm3crIB0LiMcvp57bdRsxFfzWxYmluNu9B1Tsp/WQuKJ/65CZh9Oz3cq/ozUJLa1N6G7NHvlwKT3dR9vyL1qc5Jj6lacqqjtV7nrEdZ/09gpy5I/QU1Jwoe8+FDuwAAAABJRU5ErkJggg=="
        generated_qr = generate_qr(mock_uri)
        self.assertEqual(expected_qr, generated_qr)

    def test_get_datetime_date_to_epoch(self):
        # Tests the datetime-to-epoch-seconds conversion
        talog("Unit test test_get_datetime_date_to_epoch")
        date = datetime(2020, 5, 17, 14, 30, 5)
        epoch_date1 = get_datetime_date_to_epoch(date)
        self.assertEqual(epoch_date1, 1589673600)

        #Checks if the calculated epoch is really for the beginning of the day
        date_beginning_of_day = datetime(2020, 5, 17, 0, 0, 0)
        epoch_date2 = get_datetime_date_to_epoch(date_beginning_of_day)
        self.assertEqual(epoch_date1, epoch_date2)

    def test_get_datetime_now_to_epoch(self):
        # Tests the now-datetime-to-epoch-seconds conversion
        talog("Unit test test_get_datetime_now_to_epoch")
        epoch_in_15_minute = get_datetime_now_to_epoch(15)
        # Test that epoch_in_15_minute is bigger that epoch in 14 minutes
        self.assertGreater(epoch_in_15_minute, int((datetime.now() + timedelta(minutes=14)).timestamp()))
        # Test that epoch_in_15_minute is smaller that epoch in 6 minutes
        self.assertLess(epoch_in_15_minute, int((datetime.now() + timedelta(minutes=16)).timestamp()))

