from django import forms
from .models import (
    Agency, Provider, Referrer, Tour,
    Client, Vendor, Sale, Payment, Commission
)



class AgencyForm(forms.ModelForm):
    class Meta:
        model = Agency
        fields = ['nit', 'name_agency', 'email_agency', 'tel_agency', 'contact']


class ProviderForm(forms.ModelForm):
    class Meta:
        model = Provider
        fields = ['nit', 'name_provider', 'email_provider', 'tel_provider', 'contact']


class ReferrerForm(forms.ModelForm):
    class Meta:
        model = Referrer
        fields = [
            'type_doc', 'num_doc', 'name', 'tel', 'email',
            'client_data', 'bank', 'type_count', 'num_count'
        ]


class TourForm(forms.ModelForm):
    class Meta:
        model = Tour
        fields = [
            'agency', 'provider', 'name_tour', 'description',
            'price_sale', 'price_total', 'image_path'
        ]


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['tipo_doc', 'num_doc', 'name', 'email', 'tel', 'hotel']


class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ['type_doc', 'num_doc', 'name', 'tel', 'email']


class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = [
            'tour', 'client', 'vendor', 'referrer',
            'value_sale_unit', 'quantity', 'total_sale', 'observations'
        ]


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['sale', 'options_payment', 'value']


class CommissionForm(forms.ModelForm):
    class Meta:
        model = Commission
        fields = [
            'sale', 'type', 'beneficiary_num', 'beneficiary_name',
            'percentage', 'value_sale', 'value_commission', 'observations'
        ]
