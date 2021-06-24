from django.apps import apps
from django.contrib import admin
from django.urls import include, path, reverse
from django.shortcuts import redirect
from django.utils.html import format_html

from .models import Model
from .utils import get_count, init_models, update_count

class ModelAdmin(admin.ModelAdmin):
    list_display = ['id','app','name','db_table','is_admin','is_middleware','count','refresh_button',]
    list_filter = ('is_admin','is_middleware','app',)
    readonly_fields = ('app','name','db_table','is_admin','count',)
    search_fields = ('db_table', 'app', 'name',)

    def get_queryset(self, request):
        init_models()
        return super().get_queryset(request)

    def get_urls(self):
        return [
            path(
                'django_objects_count/<slug:db_table>',
                self.admin_site.admin_view(self.refresh),
                name='django_objects_count_refresh',
            ),
        ] + super().get_urls()

    def refresh_button(self, model):
        return format_html(
            '<a class="button" href="{}">Refresh</a>',
            reverse('admin:django_objects_count_refresh', args=[model.db_table]),
        )
    refresh_button.short_description = ''
    refresh_button.allow_tags = True

    def refresh(self, request, db_table):
        model, created = Model.objects.get_or_create(db_table=db_table)
        update_count(model,get_count(db_table))
        url = reverse('admin:django_objects_count_model_changelist')
        return redirect(url)

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
       return False

admin.site.register(Model, ModelAdmin)
