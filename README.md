# PayPal Payouts API SDK for Python

![PayPal Developer](homepage.jpg)

__Welcome to PayPal Python SDK__. This repository contains PayPal's Python SDK and samples for [v1/payments/payouts](https://developer.paypal.com/docs/api/payments.payouts-batch/v1/) APIs.

This is a part of the next major PayPal SDK. It includes a simplified interface to only provide simple model objects and blueprints for HTTP calls. This repo currently contains functionality for PayPal Payouts APIs which includes [Payouts](https://developer.paypal.com/docs/api/payments.payouts-batch/v1/).

Please refer to the [PayPal Payouts Integration Guide](https://developer.paypal.com/docs/payouts/) for more information. Also refer to [Setup your SDK](https://developer.paypal.com/docs/payouts/standard/reference/sdk/#link-install) for additional information about setting up the SDK's.

## Prerequisites

Python 2.0+ or Python 3.0+

An environment which supports TLS 1.2 (see the TLS-update site for more information)

## Requirements

PayPalHttp can be found at https://pypi.org/project/paypalhttp/

## Usage

### Binaries

It is not mandatory to fork this repository for using the PayPal SDK. You can refer [PayPal Payouts SDK](https://developer.paypal.com/docs/payouts/standard/reference/sdk/#link-install) for configuring and working with SDK without forking this code.

For contributing or referring the samples, You can fork/refer this repository. 

### Setting up credentials
Get client ID and client secret by going to https://developer.paypal.com/developer/applications and generating a REST API app. Get <b>Client ID</b> and <b>Secret</b> from there.

```python
from paypalpayoutssdk.core import PayPalHttpClient, SandboxEnvironment


# Creating Access Token for Sandbox
client_id = "<<PAYPAL-CLIENT-ID>>"
client_secret = "<<PAYPAL-CLIENT-SECRET>>"
# Creating an environment
environment = SandboxEnvironment(client_id=client_id, client_secret=client_secret)
client = PayPalHttpClient(environment)
```

## Examples

### Creating a Payouts
This code created a Payout and prints the batch_id for the Payout.
#### Code:
```python
from paypalpayoutssdk.payouts import PayoutsPostRequest
from paypalhttp import HttpError

# Construct a request object and set desired parameters
# Here, PayoutsPostRequest() creates a POST request to /v1/payments/payouts
body = {
    "sender_batch_header": {
        "recipient_type": "EMAIL",
        "email_message": "SDK payouts test txn",
        "note": "Enjoy your Payout!!",
        "sender_batch_id": "Test_SDK_1",
        "email_subject": "This is a test transaction from SDK"
    },
    "items": [{
        "note": "Your 1$ Payout!",
        "amount": {
            "currency": "USD",
            "value": "1.00"
        },
        "receiver": "payout-sdk-1@paypal.com",
        "sender_item_id": "Test_txn_1"
    }, {
        "note": "Your 1$ Payout!",
        "amount": {
            "currency": "USD",
            "value": "1.00"
        },
        "receiver": "payout-sdk-2@paypal.com",
        "sender_item_id": "Test_txn_2"
    }, {
        "note": "Your 1$ Payout!",
        "amount": {
            "currency": "USD",
            "value": "1.00"
        },
        "receiver": "payout-sdk-3@paypal.com",
        "sender_item_id": "Test_txn_3"
    }, {
        "note": "Your 1$ Payout!",
        "amount": {
            "currency": "USD",
            "value": "1.00"
        },
        "receiver": "payout-sdk-4@paypal.com",
        "sender_item_id": "Test_txn_4"
    }, {
        "note": "Your 1$ Payout!",
        "amount": {
            "currency": "USD",
            "value": "1.00"
        },
        "receiver": "payout-sdk-5@paypal.com",
        "sender_item_id": "Test_txn_5"
    }]
}

request = PayoutsPostRequest()
request.request_body(body)

try:
    # Call API with your client and get a response for your call
    response = client.execute(request)
    # If call returns body in response, you can get the deserialized version from the result attribute of the response
    batch_id = response.result.batch_header.payout_batch_id
    print batch_id        
except IOError as ioe:
    print ioe
    if isinstance(ioe, HttpError):
        # Something went wrong server-side
        print ioe.status_code
```

### Handle API Failure
This will create a Payout with validation failure to showcase how to parse the failed response entity. Refer samples for more scenarios
#### Code:
```python
from paypalpayoutssdk.payouts import PayoutsPostRequest
from paypalhttp import HttpError
from paypalhttp.encoder import Encoder
from paypalhttp.serializers.json_serializer import Json

# Construct a request object and set desired parameters
# Here, PayoutsPostRequest() creates a POST request to /v1/payments/payouts
body = {
    "sender_batch_header": {
        "recipient_type": "EMAIL",
        "email_message": "SDK payouts test txn",
        "note": "Enjoy your Payout!!",
        "sender_batch_id": "Test_SDK_1",
        "email_subject": "This is a test transaction from SDK"
    },
    "items": [{
        "note": "Your 1$ Payout!",
        "amount": {
            "currency": "USD",
            "value": "1.0.0"
        },
        "receiver": "payout-sdk-1@paypal.com",
        "sender_item_id": "Test_txn_1"
    }, {
        "note": "Your 1$ Payout!",
        "amount": {
            "currency": "USD",
            "value": "1.0.0"
        },
        "receiver": "payout-sdk-2@paypal.com",
        "sender_item_id": "Test_txn_2"
    }, {
        "note": "Your 1$ Payout!",
        "amount": {
            "currency": "USD",
            "value": "1.0.0"
        },
        "receiver": "payout-sdk-3@paypal.com",
        "sender_item_id": "Test_txn_3"
    }, {
        "note": "Your 1$ Payout!",
        "amount": {
            "currency": "USD",
            "value": "1.0.0"
        },
        "receiver": "payout-sdk-4@paypal.com",
        "sender_item_id": "Test_txn_4"
    }, {
        "note": "Your 1$ Payout!",
        "amount": {
            "currency": "USD",
            "value": "1.0.0"
        },
        "receiver": "payout-sdk-5@paypal.com",
        "sender_item_id": "Test_txn_5"
    }]
}

request = PayoutsPostRequest()
request.request_body(body)

try:
    # Call API with your client and get a response for your call
    response = client.execute(request)
    # If call returns body in response, you can get the deserialized version from the result attribute of the response
    batch_id = response.result.batch_header.payout_batch_id
    print batch_id
    
except HttpError as httpe:
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
```

### Retrieve a Payout Batch
Pass the batch_id from the previous sample to retrieve Payouts batch details

#### Code:
```python
from paypalpayoutssdk.payouts import PayoutsGetRequest
# Here, PayoutsGetRequest() creates a GET request to /v1/payments/payouts/<batch-id>
request = PayoutsGetRequest("PAYOUT-BATCH-ID")

try:
    # Call API with your client and get a response for your call
    response = client.execute(request)

    # If call returns body in response, you can get the deserialized version from the result attribute of the response
    batch_status = response.result.batch_header.batch_status
    print batch_status
except IOError as ioe:
    if isinstance(ioe, HttpError):
        # Something went wrong server-side
        print ioe.status_code
        print ioe.headers
	print ioe
    else:
        # Something went wrong client side
        print ioe
```

## Running tests

To run integration tests using your client id and secret, clone this repository and run the following command:
```sh
$ pip install nose # if not already installed
$ PAYPAL_CLIENT_ID=your_client_id PAYPAL_CLIENT_SECRET=your_client_secret nosetests --exe
```

## Samples

You can start off by trying out [Payouts Samples](samples/run_all.py)

To try out different samples head to [this link](samples)

Note: Update the `paypal_client.py` with your sandbox client credentials or pass your client credentials as environment variable whie executing the samples.


## License
Code released under [SDK LICENSE](LICENSE)
