"""Default settings for messaging."""

# Django Built-in modules
import django
from django.conf import settings

# Local apps
from gateways.apps import GatewaysConfig

if django.__version__ >= '3.0':
    from django.db import models

    TEXT_CHOICES = models.TextChoices
else:
    from .models.enum_django import TextChoices

    TEXT_CHOICES = TextChoices
BANK_CLASS = getattr(
    settings,
    'CLASS',
    {
        'BMI': 'gateways.banks.BMI',
        'SEP': 'gateways.banks.SEP',
        'ZARINPAL': 'gateways.banks.Zarinpal',
        'IDPAY': 'gateways.banks.IDPay',
        'ZIBAL': 'gateways.banks.Zibal',
        'BAHAMTA': 'gateways.banks.Bahamta',
        'MELLAT': 'gateways.banks.Mellat',
    }
)
_BANK_GATEWAYS = getattr(settings, 'BANK_GATEWAYS', {})
BANK_PRIORITIES = _BANK_GATEWAYS.get('BANK_PRIORITIES', [])
BANK_GATEWAYS = _BANK_GATEWAYS.get('GATEWAYS', {})
BANK_DEFAULT = _BANK_GATEWAYS.get('DEFAULT', 'BMI')
SETTING_VALUE_READER_CLASS = _BANK_GATEWAYS.get('SETTING_VALUE_READER_CLASS',
                                                           'gateways.readers.DefaultReader')
CURRENCY = _BANK_GATEWAYS.get('CURRENCY', 'IRR')
TRACKING_CODE_QUERY_PARAM = _BANK_GATEWAYS.get('TRACKING_CODE_QUERY_PARAM', 'tc')
TRACKING_CODE_LENGTH = _BANK_GATEWAYS.get('TRACKING_CODE_LENGTH', 16)
CALLBACK_NAMESPACE = f'{GatewaysConfig.name}:callback'
GO_TO_BANK_GATEWAY_NAMESPACE = f'{GatewaysConfig.name}:go-to-bank-gateway'
IS_SAMPLE_FORM_ENABLE = _BANK_GATEWAYS.get('IS_SAMPLE_FORM_ENABLE', False)
