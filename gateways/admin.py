# Django Built-in modules
from django.contrib import admin

# Local apps
from .models import Bank


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
        'created_at',
        'update_at',
    )
    list_display = (
        'pk',
        'status',
        'bank_type',
        'tracking_code',
        'amount',
        'reference_number',
        'created_at',
        'update_at',
    )
    list_filter = (
        'status',
        'bank_type',
        'created_at',
        'update_at',
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
        'created_at',
        'update_at',
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
        'created_at',
        'update_at',
    )

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
