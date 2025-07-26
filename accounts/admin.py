from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .models import User
from .forms import CustomUserCreationForm, CustomUserChangeForm

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

    # Campos que se mostrarán como solo lectura
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Información personal'), {
            'fields': ('first_name', 'last_name', 'email', 'agency')
        }),
        (_('Permisos'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Fechas importantes'), {
            'fields': ('last_login', 'date_joined'),
        }),
        (_('Tiempos internos'), {
            'fields': ('created_at', 'updated_at'),
        }),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username',
                'password1',
                'password2',
                'email',
                'first_name',
                'last_name',
                'agency',
            ),
        }),
    )

    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'created_at')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('-created_at',)
