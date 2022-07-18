class BankGatewaysException(Exception):
    """Bank gateways exception"""


class SettingDoesNotExist(BankGatewaysException):
    """The requested setting does not exist"""


class CurrencyDoesNotSupport(BankGatewaysException):
    """The requested currency does not support"""


class AmountDoesNotSupport(BankGatewaysException):
    """The requested amount does not support"""


class BankGatewayConnectionError(BankGatewaysException):
    """The requested gateway connection error"""


class BankGatewayRejectPayment(BankGatewaysException):
    """The requested bank reject payment"""


class BankGatewayTokenExpired(BankGatewaysException):
    """The requested bank token expire"""


class BankGatewayUnclear(BankGatewaysException):
    """The requested bank unclear"""


class BankGatewayStateInvalid(BankGatewaysException):
    """The requested bank unclear"""


class BankGatewayAutoConnectionFailed(BankGatewaysException):
    """The auto connection cant find bank"""
