from django.contrib import admin
from .models import (
    Agency, Provider, Referrer, Tour, TourImage,
    Client, Sale, Payment, Commission, Employee, Role
)



@admin.register(Agency)
class AgencyAdmin(admin.ModelAdmin):
    list_display = ('name_agency', 'nit', 'email_agency', 'tel_agency')
    search_fields = ('name_agency', 'nit')


@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    list_display = ('name_provider', 'nit', 'email_provider', 'tel_provider')
    search_fields = ('name_provider', 'nit')


@admin.register(Referrer)
class ReferrerAdmin(admin.ModelAdmin):
    list_display = ('name', 'num_doc', 'email', 'bank')
    search_fields = ('name', 'num_doc')


@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ('name_tour', 'date_tour','agency', 'provider', 'price_sale')
    list_filter = ('agency', 'provider','date_tour')
    search_fields = ('name_tour',)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'num_doc', 'email', 'hotel', 'country', 'city')
    search_fields = ('name', 'num_doc', 'country', 'city')


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'num_doc', 'email')
    search_fields = ('name', 'num_doc')


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ('id', 'tour', 'client', 'employee', 'referrer', 'total_sale')
    list_filter = ('employee', 'referrer')
    search_fields = ('id',)


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'sale',
        'options_payment',
        'bank_platform',
        'value',
        'payment_date',
        'confirmed',
        'payment_reference',
        'created_at',
    )
    list_filter = (
        'options_payment',
        'bank_platform',
        'confirmed',
        'created_at',
    )
    search_fields = (
        'sale__id',
        'payment_reference',
        'note',
        'document_url',
    )
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at', 'payment_date')
    date_hierarchy = 'created_at'
    fieldsets = (
        (None, {
            'fields': (
                'sale',
                'options_payment',
                'bank_platform',
                'value',
                'payment_date',
                'payment_reference',
                'confirmed',
                'note',
                'document_url',
                'created_at',
                'updated_at',
            )
        }),
    )


@admin.register(Commission)
class CommissionAdmin(admin.ModelAdmin):
    list_display = ('id', 'sale', 'beneficiary_name', 'percentage', 'value_commission')
    search_fields = ('beneficiary_name',)


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('id', 'role')
    search_fields = ('role',)


@admin.register(TourImage)
class TourImageAdmin(admin.ModelAdmin):
    list_display = ['tour', 'caption']