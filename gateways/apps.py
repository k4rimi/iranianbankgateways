# -*- coding: utf-8 -*-
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class GatewaysConfig(AppConfig):
    name = 'gateways'
    verbose_name = _('درگاه بانکی')
    verbose_name_plural = _('درگاه های بانکی')
    # compatible with django >= 3.2
    default_auto_field = 'django.db.models.AutoField'
