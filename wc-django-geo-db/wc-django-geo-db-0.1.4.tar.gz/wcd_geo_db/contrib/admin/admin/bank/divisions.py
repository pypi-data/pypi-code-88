from django.contrib import admin

from pxd_lingua.admin import TranslationsInlineAdmin
from wcd_geo_db.modules.bank.db import Division, DivisionTranslation


class DivisionTranslationsInlineAdmin(TranslationsInlineAdmin):
    model = DivisionTranslation


@admin.register(Division)
class DivisionAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 'level', 'path', 'types'
    list_filter = 'level',
    search_fields = 'name', 'types', 'codes'
    autocomplete_fields = 'parent', 'geometry'

    inlines = (DivisionTranslationsInlineAdmin,)


@admin.register(DivisionTranslation)
class DivisionTranslationAdmin(admin.ModelAdmin):
    list_display = 'id', '__str__', 'language'
    list_filter = 'language',
    search_fields = 'name', 'synonyms', 'language'
    autocomplete_fields = 'entity',
