# Python Standard Library
import datetime

# Django Built-in modules
from django.db import models
from django.utils.translation import gettext_lazy as _

# Local apps
from .enum import BankType, PaymentStatus


class BankQuerySet(models.QuerySet):
    def __init__(self, *args, **kwargs):
        super(BankQuerySet, self).__init__(*args, **kwargs)

    def active(self):
        return self.filter()


class BankManager(models.Manager):
    def get_queryset(self):
        return BankQuerySet(self.model, using=self._db)

    def active(self):
        return self.get_queryset().active()

    def update_expire_records(self):
        count = self.active().filter(
            status=PaymentStatus.RETURN_FROM_BANK,
            update_at__lte=datetime.datetime.now() - datetime.timedelta(minutes=15)
        ).update(
            status=PaymentStatus.EXPIRE_VERIFY_PAYMENT
        )

        count = count + self.active().filter(
            status=PaymentStatus.REDIRECT_TO_BANK,
            update_at__lt=datetime.datetime.now() - datetime.timedelta(minutes=15)
        ).update(
            status=PaymentStatus.EXPIRE_GATEWAY_TOKEN
        )
        return count

    def filter_return_from_bank(self):
        return self.active().filter(status=PaymentStatus.RETURN_FROM_BANK)


class Bank(models.Model):
    status = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        choices=PaymentStatus.choices,
        verbose_name=_('وضعیت'),
    )
    bank_type = models.CharField(
        max_length=50,
        choices=BankType.choices,
        verbose_name=_('بانک'),
    )
    # It's local and generate locally
    tracking_code = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        verbose_name=_('کد پیگیری')
    )
    amount = models.CharField(
        max_length=10,
        null=False,
        blank=False,
        verbose_name=_('مبلغ')
    )
    # Reference number return from bank
    reference_number = models.CharField(
        unique=True,
        max_length=255,
        null=False,
        blank=False,
        verbose_name=_('رفرنس')
    )
    response_result = models.TextField(
        null=True,
        blank=True,
        verbose_name=_('نتیجه بانک')
    )
    callback_url = models.TextField(
        null=False,
        blank=False,
        verbose_name=_('آدرس کال بک')
    )
    extra_information = models.TextField(
        null=True,
        blank=True,
        verbose_name=_('اطلاعات تکمیلی')
    )
    bank_choose_identifier = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_('شناسه بانک انتخابی')
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
    )
    update_at = models.DateTimeField(
        auto_now=True,
        editable=False,
    )

    objects = BankManager()

    class Meta:
        verbose_name = _('تراکنش')
        verbose_name_plural = _('تراکنش ها')

    def __str__(self):
        return '{}-{}'.format(self.pk, self.tracking_code)

    @property
    def is_success(self):
        return self.status == PaymentStatus.COMPLETE
