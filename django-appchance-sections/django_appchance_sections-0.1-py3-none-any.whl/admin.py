from appchance_sections.forms import SectionAdminForm
from django.contrib import admin


class SectionAdminMixin(admin.ModelAdmin):
    list_display = ("name", "content_name", "widget", "placement", "order", "content_url")
    form = SectionAdminForm
