from django.contrib import admin

from .models import Dictionary, Newsletter


class NewsletterAdmin(admin.ModelAdmin):
    pass


class DictionaryAdmin(admin.ModelAdmin):
    search_fields = ("word", "pronunciation")
    list_display = ("word", "pronunciation")


admin.site.register(Newsletter, NewsletterAdmin)
admin.site.register(Dictionary, DictionaryAdmin)
