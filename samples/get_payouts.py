import json
from paypal_client import PayPalClient
from paypalpayoutssdk.payouts import PayoutsGetRequest
from create_payouts import CreatePayouts
from paypalhttp.serializers.json_serializer import Json
from paypalhttp.http_error import HttpError
from paypalhttp.encoder import Encoder

class GetPayouts(PayPalClient):

    
    """ Retries a Payout batch details provided the batch_id
     This API is paginated - by default 1000 payout items are retrieved
     Use pagination links to navigate through all the items, use total_required to get the total pages"""
    def get_payouts(self, payout_batch_id, debug=False):
        request = PayoutsGetRequest(payout_batch_id)
        request.page(1)
        request.page_size(10)
        request.total_required(True)

        try:
            response = self.client.execute(request)

            if debug:
                print(response.result)
                print("Status Code: ", response.status_code)
                print("Payout Batch ID: " +
                    response.result.batch_header.payout_batch_id)
                print("Payout Batch Status: " +
                    response.result.batch_header.batch_status)
                print("Items count: ", len(response.result.items))
                print("First item id: " + response.result.items[0].payout_item_id)
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




"""This is the driver function which invokes the get_payouts function to retrieve Payouts Batch."""
if __name__ == "__main__":
    create_response = CreatePayouts().create_payouts(debug=True)
    batch_id = create_response.result.batch_header.payout_batch_id
    GetPayouts().get_payouts(batch_id, True)
    print("Retrieve an invalid payout")
    GetPayouts().get_payouts("DUMMY", True)
