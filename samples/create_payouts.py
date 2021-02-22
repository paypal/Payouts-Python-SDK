import json
import random
import string
from paypal_client import PayPalClient
from paypalpayoutssdk.payouts import PayoutsPostRequest
from paypalhttp.serializers.json_serializer import Json
from paypalhttp.http_error import HttpError
from paypalhttp.encoder import Encoder

class CreatePayouts(PayPalClient):

    """ Creates a payout batch with 5 payout items
    Calls the create batch api (POST - /v1/payments/payouts)
    A maximum of 15000 payout items are supported in a single batch request"""
    @staticmethod
    def build_request_body(include_validation_failure = False):
        senderBatchId = str(''.join(random.sample(
            string.ascii_uppercase + string.digits, k=7)))
        amount = "1.0.0" if include_validation_failure else "1.00"
        return \
            {
                "sender_batch_header": {
                    "recipient_type": "EMAIL",
                    "email_message": "SDK payouts test txn",
                    "note": "Enjoy your Payout!!",
                    "sender_batch_id": senderBatchId,
                    "email_subject": "This is a test transaction from SDK"
                },
                "items": [{
                    "note": "Your 1$ Payout!",
                    "amount": {
                        "currency": "USD",
                        "value": amount
                    },
                    "receiver": "payout-sdk-1@paypal.com",
                    "sender_item_id": "Test_txn_1"
                }, {
                    "note": "Your 1$ Payout!",
                    "amount": {
                        "currency": "USD",
                        "value": amount
                    },
                    "receiver": "payout-sdk-2@paypal.com",
                    "sender_item_id": "Test_txn_2"
                }, {
                    "note": "Your 1$ Payout!",
                    "amount": {
                        "currency": "USD",
                        "value": amount
                    },
                    "receiver": "payout-sdk-3@paypal.com",
                    "sender_item_id": "Test_txn_3"
                }, {
                    "note": "Your 1$ Payout!",
                    "amount": {
                        "currency": "USD",
                        "value": amount
                    },
                    "receiver": "payout-sdk-4@paypal.com",
                    "sender_item_id": "Test_txn_4"
                }, {
                    "note": "Your 1$ Payout!",
                    "amount": {
                        "currency": "USD",
                        "value": amount
                    },
                    "receiver": "payout-sdk-5@paypal.com",
                    "sender_item_id": "Test_txn_5"
                }]
            }

    def create_payouts(self, debug=False):
        request = PayoutsPostRequest()
        request.request_body(self.build_request_body(False))
        response = self.client.execute(request)

        if debug:
            print("Status Code: ", response.status_code)
            print("Payout Batch ID: " +
                  response.result.batch_header.payout_batch_id)
            print("Payout Batch Status: " +
                  response.result.batch_header.batch_status)
            print("Links: ")
            for link in response.result.links:
                print('\t{}: {}\tCall Type: {}'.format(
                    link.rel, link.href, link.method))

            # To toggle print the whole body comment/uncomment the below line
            #json_data = self.object_to_json(response.result)
            #print "json_data: ", json.dumps(json_data, indent=4)
        
        return response

    
    def create_payouts_failure(self, debug=False):
        request = PayoutsPostRequest()
        request.request_body(self.build_request_body(True))

        try:
            response = self.client.execute(request)
        except HttpError as httpe:
            if debug:
                # Handle server side API failure
                encoder = Encoder([Json()])
                error = encoder.deserialize_response(httpe.message, httpe.headers)
                print("Error: " + error["name"])
                print("Error message: " + error["message"])
                print("Information link: " + error["information_link"])
                print("Debug id: " + error["debug_id"])
                print("Details: ")
                for detail in error["details"]:
                    print("Error location: " + detail["location"])
                    print("Error field: " + detail["field"])
                    print("Error issue: " + detail["issue"])

        except IOError as ioe:
            #Handle cient side connection failures
            print(ioe.message)
            

"""This is the driver function which invokes the create_payouts function to create
   a Payouts Batch."""
if __name__ == "__main__":
    CreatePayouts().create_payouts(debug=True)
    #Simulate failure in create payload to showcase validation failure and how to parse the reason for failure
    CreatePayouts().create_payouts_failure(debug=True)
