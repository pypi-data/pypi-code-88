# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import (
   UserPasswordHistory,
)


@admin.register(UserPasswordHistory)
class UserPasswordHistoryAdmin(admin.ModelAdmin):
    pass



