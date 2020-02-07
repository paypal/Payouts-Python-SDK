import json
import time
from paypal_client import PayPalClient
from paypalpayoutssdk.payouts import PayoutsItemCancelRequest
from create_payouts import CreatePayouts
from get_payouts import GetPayouts
from get_payout_item import GetPayoutItem
from paypalhttp.serializers.json_serializer import Json

class CancelPayoutItem(PayPalClient):

    """ Cancels an UNCLAIMED payout item
     An item can be cancelled only when the item status is UNCLAIMED and the batch status is SUCCESS
     Upon cancelling the item status becomes RETURNED and the funds returned back to the sender"""
    def cancel_payout_item(self, payout_item_id, debug=False):
        request = PayoutsItemCancelRequest(payout_item_id)
        response = self.client.execute(request)

        if debug:
            print("Status Code: ", response.status_code)
            print("Payout Item ID: " + response.result.payout_item_id)
            print("Payout Item Status: " + response.result.transaction_status)
            print("Links: ")
            for link in response.result.links:
                print('\t{}: {}\tCall Type: {}'.format(
                    link.rel, link.href, link.method))

            # To toggle print the whole body comment/uncomment the below line
            #json_data = self.object_to_json(response.result)
            #print "json_data: ", json.dumps(json_data, indent=4)

        return response


"""This is the driver function which invokes the cancel_payout_item function to cancel an UNCLAIMED payout item."""
if __name__ == "__main__":
    create_response = CreatePayouts().create_payouts(debug=True)
    batch_id = create_response.result.batch_header.payout_batch_id
    get_response = GetPayouts().get_payouts(batch_id, True)
    item_id = get_response.result.items[0].payout_item_id
    time.sleep(20)
    CancelPayoutItem().cancel_payout_item(item_id)
