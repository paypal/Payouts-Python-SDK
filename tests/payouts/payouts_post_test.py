import unittest
import json
import string
import random
from paypalpayoutssdk.payouts import PayoutsPostRequest
from tests import TestHarness

class PayoutsPostTest(TestHarness):

    def testCreatePayouts(self):
        response = createPayouts(self.client)

        self.assertEqual(201, response.status_code)
        self.assertIsNotNone(response.result)

        self.assertIsNotNone(response.result.batch_header.payout_batch_id)
        self.assertIsNotNone(response.result.batch_header.batch_status)

        self.assertEqual("This is a test transaction from SDK",
                         response.result.batch_header.sender_batch_header.email_subject)
        self.assertEqual("SDK payouts test txn",
                         response.result.batch_header.sender_batch_header.email_message)

        self.assertIsNotNone(response.result.links)


def createPayouts(client):
    request = PayoutsPostRequest()
    sender_batch_id = str(''.join(random.sample(
        string.ascii_uppercase + string.digits, k=7)))
    body = {
        "sender_batch_header": {
            "recipient_type": "EMAIL",
            "email_message": "SDK payouts test txn",
            "note": "Enjoy your Payout!!",
            "sender_batch_id": sender_batch_id,
            "email_subject": "This is a test transaction from SDK"
        },
        "items": [{
            "note": "Your 5$ Payout!",
            "amount": {
                "currency": "USD",
                "value": "1.00"
            },
            "receiver": "payout-sdk-1@paypal.com",
            "sender_item_id": "Test_txn_1"
        }, {
            "note": "Your 5$ Payout!",
            "amount": {
                "currency": "USD",
                "value": "1.00"
            },
            "receiver": "payout-sdk-2@paypal.com",
            "sender_item_id": "Test_txn_2"
        }, {
            "note": "Your 5$ Payout!",
            "amount": {
                "currency": "USD",
                "value": "1.00"
            },
            "receiver": "payout-sdk-3@paypal.com",
            "sender_item_id": "Test_txn_3"
        }, {
            "note": "Your 5$ Payout!",
            "amount": {
                "currency": "USD",
                "value": "1.00"
            },
            "receiver": "payout-sdk-4@paypal.com",
            "sender_item_id": "Test_txn_4"
        }, {
            "note": "Your 5$ Payout!",
            "amount": {
                "currency": "USD",
                "value": "1.00"
            },
            "receiver": "payout-sdk-5@paypal.com",
            "sender_item_id": "Test_txn_5"
        }]
    }
    request.request_body(body)
    return client.execute(request)


if __name__ == "__main__":
    unittest.main()
