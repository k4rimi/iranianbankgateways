from django.utils.translation import gettext_lazy as _

import azbankgateways.default_settings as settings


class BankType(settings.TEXT_CHOICES):
    BMI = 'BMI', _('ملی')
    SEP = 'SEP', _('سپه')
    ZARINPAL = 'ZARINPAL', _('زرین پال')
    IDPAY = 'IDPAY', _('آیدی پی')
    ZIBAL = 'ZIBAL', _('زیبال')
    BAHAMTA = 'BAHAMTA', _('باهمتا')
    MELLAT = 'MELLAT', _('ملت')


class CurrencyEnum(settings.TEXT_CHOICES):
    IRR = 'IRR', _('ریال')
    IRT = 'IRT', _('تومان')

    @classmethod
    def rial_to_toman(cls, amount):
        return amount / 10

    @classmethod
    def toman_to_rial(cls, amount):
        return amount * 10


class PaymentStatus(settings.TEXT_CHOICES):
    WAITING = _('در انتظار')
    REDIRECT_TO_BANK = _('هدایت شده به بانک')
    RETURN_FROM_BANK = _('بازگشته از بانک')
    CANCEL_BY_USER = _('لغو توسط کاربر')
    EXPIRE_GATEWAY_TOKEN = _('توکن منقضی شده')
    EXPIRE_VERIFY_PAYMENT = _('تاییدیه پرداخت منقضی شده')
    COMPLETE = _('تکمیل شده')
