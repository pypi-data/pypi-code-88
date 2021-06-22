from django.apps import apps
from django.contrib import admin
from django.db.utils import ImproperlyConfigured, OperationalError, ProgrammingError
from django.shortcuts import redirect
from django.urls import include, path, reverse
from django.utils.html import format_html

from .models import Table
from .utils import get_model

class TableAdmin(admin.ModelAdmin):
    list_display = [
        'app',
        'name',
        'db_table',
        'count',
        'buttons_refresh',
        'buttons_truncate',
    ]
    list_filter = ['app',]
    # readonly_fields = ['is_running','started_at','completed_at','duration','timesince']
    search_fields = ['db_table','name', ]

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                'admin_truncate_refresh/<slug:db_table>',
                self.admin_site.admin_view(self.refresh),
                name='admin_truncate_refresh',
            ),
            path(
                'admin_truncate_table/<slug:db_table>',
                self.admin_site.admin_view(self.truncate),
                name='admin_truncate_table',
            ),
        ]
        return custom_urls + urls

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
       return False

    def buttons_refresh(self, model):
        return format_html(
            '<a class="button" href="{}">Refresh</a>',
            reverse('admin:admin_truncate_refresh', args=[model.db_table]),
        )
    buttons_refresh.short_description = ''
    buttons_refresh.allow_tags = True

    def buttons_truncate(self, model):
        return format_html(
            '<a class="button" href="{}">Truncate %s</a>' % model.db_table,
            reverse('admin:admin_truncate_table', args=[model.db_table]),
        )
    buttons_truncate.short_description = ''
    buttons_truncate.allow_tags = True

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        db_tables = []
        table_list = list(Table.objects.all())
        for m in apps.get_models():
            app, name, db_table = m._meta.app_label, m.__name__, m._meta.db_table
            db_tables.append(db_table)
            try:
                count = m.objects.all().count()
            except (ImproperlyConfigured, OperationalError, ProgrammingError):
                count = None
            kwargs = dict(app=app,name=name,db_table=db_table,count=count)
            table = next(filter(lambda t: t.app==app and t.name==name, table_list), None)
            if table:
                for k,v in kwargs.items():
                    if getattr(table,k)!=v:
                        Table.objects.filter(pk=table.pk).update(**{k:v})
            else:
                Table(**kwargs).save()
        Table.objects.exclude(db_table__in=db_tables).delete()
        return qs

    def refresh(self, request, db_table):
        model = get_model(db_table)
        Table.objects.filter(db_table=db_table).update(count=model.objects.all().count())
        url = reverse('admin:django_truncate_table_table_changelist')
        return redirect(url)

    def truncate(self, request, db_table):
        model = get_model(db_table)
        model.objects.all().delete()
        Table.objects.filter(db_table=db_table).update(count=model.objects.all().count())
        url = reverse('admin:django_truncate_table_table_changelist')
        return redirect(url)

admin.site.register(Table, TableAdmin)
