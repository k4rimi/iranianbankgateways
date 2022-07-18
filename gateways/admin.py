# Django Built-in modules
from django.contrib import admin

# Local apps
from .models import Bank
from utils.admin import DateTimeAdminMixin


@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    fields = (
        'pk',
        'status',
        'bank_type',
        'tracking_code',
        'amount',
        'reference_number',
        'response_result',
        'callback_url',
        'extra_information',
        'bank_choose_identifier',
        *DateTimeAdminMixin.fields,
    )
    list_display = (
        'pk',
        'status',
        'bank_type',
        'tracking_code',
        'amount',
        'reference_number',
        *DateTimeAdminMixin.list_display,
    )
    list_filter = (
        'status',
        'bank_type',
        *DateTimeAdminMixin.list_filter,
    )
    search_fields = (
        'status',
        'bank_type',
        'tracking_code',
        'amount',
        'reference_number',
        'response_result',
        'callback_url',
        'extra_information',
    )
    readonly_fields = (
        'pk',
        'status',
        'bank_type',
        'tracking_code',
        'amount',
        'reference_number',
        'response_result',
        'callback_url',
        'extra_information',
        *DateTimeAdminMixin.readonly_fields,
    )
    date_hierarchy = DateTimeAdminMixin.date_hierarchy

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
