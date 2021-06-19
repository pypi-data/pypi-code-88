from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model

User = get_user_model()


class UserAdmin(auth_admin.UserAdmin):
    fieldsets = auth_admin.UserAdmin.fieldsets + (
        ('Extra', {
            'fields': ('base_group', 'parent', 'friends'),
        }),
    )


admin.site.register(User, UserAdmin)
