
from django.apps import apps
from django.db import models
from django.contrib import admin

from modeltranslation.admin import TranslationAdmin
from modeltranslation.utils import get_translation_fields

from flatpages.forms import FlatpageForm
from flatpages.models import FlatPage


def _get_wising_editor():

    if apps.is_installed('ckeditor_uploader'):
        from ckeditor_uploader.widgets import CKEditorUploadingWidget
        return CKEditorUploadingWidget

    if apps.is_installed('ckeditor'):
        from ckeditor.widgets import CKEditorWidget
        return CKEditorWidget

    return None


@admin.register(FlatPage)
class FlatPageAdmin(TranslationAdmin):

    form = FlatpageForm

    list_display = ['url', 'title']

    list_filter = ['registration_required']

    search_fields = ['url', 'title']

    fields = (
        'url',
        tuple(get_translation_fields('title')),
        tuple(get_translation_fields('content')),
        ('registration_required', 'template_name', ),
    )

    def __init__(self, *args, **kwargs):

        editor = _get_wising_editor()

        if editor:
            self.formfield_overrides = {
                models.TextField: {
                    'widget': editor
                }
            }

        super().__init__(*args, **kwargs)
