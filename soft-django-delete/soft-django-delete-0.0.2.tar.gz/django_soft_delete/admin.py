from django.contrib import admin
from .admin_utils import custom_get_deleted_objects


class SoftDeleteAdmin(admin.ModelAdmin):
    def get_deleted_objects(self, objs, request):
        return custom_get_deleted_objects(objs, request, self.admin_site)
