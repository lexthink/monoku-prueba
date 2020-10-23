from django.contrib import admin
from django.contrib.auth.models import Group
from . import models


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'is_admin']
    list_filter = ['is_admin']


admin.site.unregister(Group)
