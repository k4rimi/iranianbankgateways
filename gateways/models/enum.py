# Django Built-in modules
from django.utils.translation import gettext_lazy as _

# Local apps
import gateways.default_settings as settings


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
    WAITING = 'Waiting', _('در انتظار')
    REDIRECT_TO_BANK = 'Redirect to bank', _('هدایت شده به بانک')
    RETURN_FROM_BANK = 'Return from bank', _('بازگشته از بانک')
    CANCEL_BY_USER = 'Cancel by user', _('لغو توسط کاربر')
    EXPIRE_GATEWAY_TOKEN = 'Expire gateway token', _('توکن منقضی شده')
    EXPIRE_VERIFY_PAYMENT = 'Expire verify payment', _('تاییدیه پرداخت منقضی شده')
    COMPLETE = 'Complete', _('تکمیل شده')
