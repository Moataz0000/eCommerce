from django.contrib import admin
from .models import Account


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'email', 'username']
    search_fields = ['user_name']

