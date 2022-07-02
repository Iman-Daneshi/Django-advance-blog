from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

from .models import User, Profile

# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('email', 'is_superuser', 'is_active')
    list_filter = ('email', 'is_superuser', 'is_active')
    search_fields = ('email',)
    ordering = ('email',)
    fieldsets = (
        ('Authentications', {
            "fields": (
                'email', 'password',
            ),
        }),
        ('Permissions', {
            "fields": (
                'is_staff', 'is_active', 'is_superuser',
            ),
        }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active', 'is_superuser')}
        ),
    )
    

admin.site.register(Profile)
admin.site.register(User, CustomUserAdmin)


