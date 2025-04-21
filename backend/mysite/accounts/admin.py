# mysite/accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from mysite.accounts.models import User

admin.site.register(User, UserAdmin)
