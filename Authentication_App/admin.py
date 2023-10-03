from django.contrib import admin
from .models import user
from django.contrib.auth.admin import UserAdmin
# Register your models here.


@admin.register(user)
class userAdmin(UserAdmin):
    list_display = ['id', 'username', 'Type', 'first_name', 'Middle_name',
                    'last_name', 'Date_of_birth', 'nationality', 'Where_do_you_live']
    fieldsets = (
        (None, {
            "fields": ('username', 'Type', 'first_name', 'Middle_name', 'last_name', 'Date_of_birth', 'nationality', 'Where_do_you_live', 'is_staff', 'is_active', 'is_superuser'),
        }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'Type', 'first_name', 'Middle_name', 'last_name', 'Date_of_birth', 'nationality', 'Where_do_you_live',)}
         ),
    )
