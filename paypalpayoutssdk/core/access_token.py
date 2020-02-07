import time

class AccessToken(object):

    def __init__(self, access_token, expires_in, token_type):
        self.access_token = access_token
        self.expires_in = expires_in
        self.token_type = token_type
        self.created_at = time.time()

    def is_expired(self):
        return self.created_at + self.expires_in <= time.time()

    def authorization_string(self):
        return "{0} {1}".format(self.token_type, self.access_token)