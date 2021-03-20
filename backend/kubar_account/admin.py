from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import KubarUser


class KubarUserAdmin(UserAdmin):
    search_fields = ('pk', 'username', 'first_name', 'last_name', 'email')


admin.site.register(KubarUser, KubarUserAdmin)
