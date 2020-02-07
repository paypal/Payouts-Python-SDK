import unittest
import json
from paypalpayoutssdk.payouts import PayoutsGetRequest
from tests.test_harness import TestHarness
from payouts_post_test import createPayouts

class PayoutsGetTest(TestHarness):

    def testPayoutsGetTest(self):
        response = getPayouts(self.client)
        self.assertEqual(200, response.status_code)
        self.assertIsNotNone(response.result)

        self.assertIsNotNone(response.result.batch_header.payout_batch_id)
        self.assertIsNotNone(response.result.batch_header.batch_status)
        self.assertEqual("This is a test transaction from SDK",
                         response.result.batch_header.sender_batch_header.email_subject)
        self.assertEqual("SDK payouts test txn",
                         response.result.batch_header.sender_batch_header.email_message)

        self.assertIsNotNone(response.result.items)
        self.assertEquals(5, len(response.result.items))
        self.assertEquals(1, response.result.total_pages)

        self.assertIsNotNone(response.result.links)

        self.assertIsNotNone(response.result.items[0].payout_item_id)
        self.assertIsNotNone(response.result.items[0].transaction_status)
        self.assertEquals("1.00", response.result.items[0].payout_item.amount.value)
        self.assertEquals("USD", response.result.items[0].payout_item.amount.currency)
        self.assertEquals("Test_txn_1", response.result.items[0].payout_item.sender_item_id)
        self.assertEquals("payout-sdk-1@paypal.com", response.result.items[0].payout_item.receiver)


def getPayouts(client):
    create_response = createPayouts(client)

    request = PayoutsGetRequest(create_response.result.batch_header.payout_batch_id)
    request.page(1)
    request.page_size(10)
    request.total_required(True)
    return client.execute(request)


if __name__ == "__main__":
    unittest.main()
