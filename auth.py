from eve.auth import BasicAuth


class MyBasicAuth(BasicAuth):
    """ Custom auth logic is provided by a subclass of eve.auth.BasicAuth"""
    def check_auth(self, username, password, allowed_roles, resource, method):
        return username == 'admin' and password == 'secret'
