import unittest
import os
from paypalpayoutssdk.core import PayPalHttpClient, SandboxEnvironment

class TestHarness(unittest.TestCase):

    def setUp(self):
        client_id =  os.environ["PAYPAL_CLIENT_ID"] if 'PAYPAL_CLIENT_ID' in os.environ else "<<PAYPAL-CLIENT-ID>>"
        client_secret = os.environ["PAYPAL_CLIENT_SECRET"] if 'PAYPAL_CLIENT_SECRET' in os.environ else "<<PAYPAL-CLIENT-SECRET>>"
        self.environment = SandboxEnvironment(client_id=client_id, client_secret=client_secret)
        self.client = PayPalHttpClient(self.environment)