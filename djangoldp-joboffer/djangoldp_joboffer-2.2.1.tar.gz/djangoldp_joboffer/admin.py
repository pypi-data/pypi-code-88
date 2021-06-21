from django.contrib import admin
from djangoldp.admin import DjangoLDPAdmin
from djangoldp.models import Model
from .models import JobOffer


class JobOfferAdmin(DjangoLDPAdmin):
    list_display = ('urlid', 'title', 'author')
    exclude = ('urlid', 'is_backlink', 'allow_create_backlink')
    search_fields = ['urlid', 'title', 'author__urlid', 'skills__name', 'description']
    ordering = ['urlid']

    def get_queryset(self, request):
        # Hide distant jobs
        queryset = super(JobOfferAdmin, self).get_queryset(request)
        internal_ids = [x.pk for x in queryset if not Model.is_external(x)]
        return queryset.filter(pk__in=internal_ids)


admin.site.register(JobOffer, JobOfferAdmin)
