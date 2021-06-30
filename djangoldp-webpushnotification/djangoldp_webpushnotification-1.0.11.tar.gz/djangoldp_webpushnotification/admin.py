from django.contrib import admin
from djangoldp.admin import DjangoLDPAdmin

from .models import VAPIDKeyset


class VAPIDKeysetAdmin(DjangoLDPAdmin):
    readonly_fields = ('public_key_view', 'private_key_view')

    def public_key_view(self, obj):
        return obj.public_key

    def private_key_view(self, obj):
        return obj.private_key

    class Meta:
        verbose_name = 'VAPID key-set'

admin.site.register(VAPIDKeyset, VAPIDKeysetAdmin)
