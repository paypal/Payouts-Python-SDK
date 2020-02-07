import unittest
import json
import time
from paypalpayoutssdk.payouts import PayoutsItemCancelRequest
from tests.test_harness import TestHarness
from payouts_item_get_test import getPayoutItem

class PayoutsItemCancelTest(TestHarness):

    def testPayoutsItemCancelTest(self):
        response = getPayoutItem(self.client)
        time.sleep(20)

        request = PayoutsItemCancelRequest(response.result.payout_item_id)
        response = self.client.execute(request)
        self.assertEqual(200, response.status_code)
        self.assertIsNotNone(response.result)

        self.assertIsNotNone(response.result.links)

        self.assertIsNotNone(response.result.payout_item_id)
        self.assertIsNotNone(response.result.transaction_id)
        self.assertIsNotNone(response.result.transaction_status)
        self.assertEquals("RETURNED", response.result.transaction_status)
        self.assertEquals("1.00", response.result.payout_item.amount.value)
        self.assertEquals("USD", response.result.payout_item.amount.currency)
        self.assertEquals("Test_txn_1", response.result.payout_item.sender_item_id)
        self.assertEquals("payout-sdk-1@paypal.com", response.result.payout_item.receiver)

        #print(json.dumps(response.result.__str__, indent=2))


    # Add your own checks here
if __name__ == "__main__":
    unittest.main()
