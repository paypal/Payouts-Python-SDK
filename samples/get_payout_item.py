import json
from paypal_client import PayPalClient
from paypalpayoutssdk.payouts import PayoutsItemGetRequest
from create_payouts import CreatePayouts
from get_payouts import GetPayouts
from paypalhttp.serializers.json_serializer import Json
from paypalhttp.http_error import HttpError
from paypalhttp.encoder import Encoder

class GetPayoutItem(PayPalClient):

    """ Retrieves the details of an individual Payout item provided the item_id"""
    def get_payout_item(self, payout_item_id, debug=False):
        request = PayoutsItemGetRequest(payout_item_id)

        try:
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
        except HttpError as httpe:
            # Handle server side API failure
            encoder = Encoder([Json()])
            error = encoder.deserialize_response(httpe.message, httpe.headers)
            print("Error: " + error["name"])
            print("Error message: " + error["message"])
            print("Information link: " + error["information_link"])
            print("Debug id: " + error["debug_id"])

        except IOError as ioe:
            #Handle cient side connection failures
            print(ioe.message)


"""This is the driver function which invokes the get_payout_item retrieve a Payout item."""
if __name__ == "__main__":
    create_response = CreatePayouts().create_payouts(debug=True)
    batch_id = create_response.result.batch_header.payout_batch_id
    get_response = GetPayouts().get_payouts(batch_id, True)
    item_id = get_response.result.items[0].payout_item_id
    GetPayoutItem().get_payout_item(item_id, True)
    print("Retrieve an invalid payout item")
    GetPayoutItem().get_payout_item("DUMMY", True)
