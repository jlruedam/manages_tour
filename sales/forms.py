from django import forms
from .models import (
    Agency, Provider, Referrer, Tour, TourImage,
    Client, Employee, Sale, Payment, Commission
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


class TourImageForm(forms.ModelForm):
    class Meta:
        model = TourImage
        fields = [
            'image_path', 'caption'
        ]

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['type_doc', 'num_doc', 'name', 'email', 'tel', 'hotel']


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['type_doc', 'num_doc', 'name', 'tel', 'email']


# class SaleForm(forms.ModelForm):
#     class Meta:
#         model = Sale
#         fields = [
#             'tour', 'client', 'vendor', 'referrer',
#             'value_sale_unit', 'quantity', 'total_sale', 'observations'
#         ]

# forms.py
class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = [
            'tour',
            'client',
            'employee',
            'referrer',
            'value_sale_unit',
            'quantity',
            'observations',
        ]
        widgets = {
            'tour': forms.Select(attrs={'class': 'form-control'}),
            'client': forms.Select(attrs={'class': 'form-control'}),
            'employee': forms.Select(attrs={'class': 'form-control'}),
            'referrer': forms.Select(attrs={'class': 'form-control'}),
            'value_sale_unit': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'observations': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Observaciones adicionales (opcional)'
            }),
        }
        labels = {
            'tour': 'Tour',
            'client': 'Cliente',
            'employee': 'Employee',
            'referrer': 'Referido por',
            'value_sale_unit': 'Valor unitario de la venta',
            'quantity': 'Cantidad',
            'observations': 'Observaciones',
        }


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
