"""Exceptions"""

__copyright__ = "Copyright (C) 2014 Ivan D Vasin"
__docformat__ = "restructuredtext"

import exceptions as _py_exc


class Exception(_py_exc.Exception):
    pass


class Error(RuntimeError, Exception):
    pass


class InsufficientConnSettings(Error):
    """The connection settings are insufficient.

    :param <str> missing_attrs:
        The required attributes that are missing.

    """
    def __init__(self, missing_attrs):

        self.missing_attrs = missing_attrs

        message = 'insufficient connection settings'
        if missing_attrs:
            message += ' (missing attributes {})'.format(missing_attrs)

        super(InsufficientConnSettings, self).__init__(message)
