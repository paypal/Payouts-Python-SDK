import os
import sys
from paypalpayoutssdk.core import PayPalHttpClient, SandboxEnvironment

class PayPalClient:
    def __init__(self):
        self.client_id =  os.environ["PAYPAL_CLIENT_ID"] if 'PAYPAL_CLIENT_ID' in os.environ else "<<PAYPAL-CLIENT-ID>>"
        self.client_secret = os.environ["PAYPAL_CLIENT_SECRET"] if 'PAYPAL_CLIENT_SECRET' in os.environ else "<<PAYPAL-CLIENT-SECRET>>"
        
        """Setting up and Returns PayPal SDK environment with PayPal Access credentials.
           For demo purpose, we are using SandboxEnvironment. In production this will be
           LiveEnvironment."""
        self.environment = SandboxEnvironment(client_id=self.client_id, client_secret=self.client_secret)
        
        """ Returns PayPal HTTP client instance with environment which has access
            credentials context. This can be used invoke PayPal API's provided the
            credentials have the access to do so. """
        self.client = PayPalHttpClient(self.environment)

    def object_to_json(self, json_data):
        """
        Function to print all json data in an organized readable manner
        """
        result = {}
        if sys.version_info[0] < 3:
            itr = json_data.__dict__.iteritems()
        else:
            itr = json_data.__dict__.items()
        for key,value in itr:
            # Skip internal attributes.
            if key.startswith("__"):
                continue
            result[key] = self.array_to_json_array(value) if isinstance(value, list) else\
                        self.object_to_json(value) if not self.is_primittive(value) else\
                         value
        return result
    def array_to_json_array(self, json_array):
        result =[]
        if isinstance(json_array, list):
            for item in json_array:
                result.append(self.object_to_json(item) if  not self.is_primittive(item) \
                              else self.array_to_json_array(item) if isinstance(item, list) else item)
        return result
    
    def is_primittive(self, data):
        return isinstance(data, str) or isinstance(data, unicode) or isinstance(data, int)