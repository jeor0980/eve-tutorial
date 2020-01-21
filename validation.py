import re

from eve.io.mongo import Validator


class MyValidator(Validator):
    def _validate_isodd(self, isodd, field, value):
        """ Define a brand new 'isodd' rule """
        if isodd and not bool(value & 1):
            self._error(field, 'Value must be an odd number')

    def _validate_type_email(self, value):
        """ Extend types by adding a new 'email' type """
        if re.match(r"[^@]+@[^@]+\.[^@]+", value):
            return True
