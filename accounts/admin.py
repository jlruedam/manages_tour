from django.contrib import admin
from .models import User

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'agency', 'is_admin', 'created_at')
    list_filter = ('is_admin', 'agency')
    search_fields = ('username',)