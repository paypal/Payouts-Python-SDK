import unittest
import json
import sys
from paypalpayoutssdk.payouts import PayoutsItemGetRequest
from tests.test_harness import TestHarness
from tests.payouts.payouts_get_test import getPayouts

class PayoutsItemGetTest(TestHarness):

    def testPayoutsItemGetTest(self):
        response = getPayoutItem(self.client)

        sys.stdout.write('PayoutsPostTest')
        sys.stdout.write(response.headers)
        sys.stdout.write(response.status_code)
        sys.stdout.write(response.result)
        sys.stdout.write(response.result.links)
        sys.stdout.flush()

        self.assertEqual(200, response.status_code)
        self.assertIsNotNone(response.result)

        self.assertIsNotNone(response.result.links)

        self.assertIsNotNone(response.result.payout_item_id)
        self.assertIsNotNone(response.result.transaction_status)
        self.assertEquals("1.00", response.result.payout_item.amount.value)
        self.assertEquals("USD", response.result.payout_item.amount.currency)
        self.assertEquals("Test_txn_1", response.result.payout_item.sender_item_id)
        self.assertEquals("payout-sdk-1@paypal.com", response.result.payout_item.receiver)


def getPayoutItem(client):
    get_response = getPayouts(client)

    request = PayoutsItemGetRequest(get_response.result.items[0].payout_item_id)
    return client.execute(request)

if __name__ == "__main__":
    unittest.main()
