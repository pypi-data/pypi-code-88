# -*- coding:utf-8 -*-

__author__ = 'denishuang'

from . import models, serializers, stats
from rest_framework import viewsets, decorators, response
from xyz_restful.decorators import register
from xyz_util.statutils import do_rest_stat_action
from xyz_restful.mixins import BatchActionMixin

@register()
class CourseViewSet(viewsets.ModelViewSet):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer
    search_fields = ('name', 'code')
    filter_fields = {
        'id': ['exact', 'in'],
        'is_active': ['exact'],
        'name': ['exact'],
        'category': ['exact'],
        'code': ['exact']
    }
    ordering_fields = ('is_active', 'title', 'create_time')

    @decorators.action(['get'], detail=False)
    def stat(self, request):
        return do_rest_stat_action(self, stats.stats_course)

    @decorators.action(['post'], detail=True)
    def go_pass(self, request, pk):
        course = self.get_object()
        course.passes.update_or_create(
            user=request.user,
            defaults=dict(
                is_pass=request.data.get('is_pass')
            )
        )
        return response.Response(dict(detail='ok'))


@register()
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    search_fields = ('name', 'code')
    filter_fields = ('code', 'name')


@register()
class ChapterViewSet(viewsets.ModelViewSet):
    queryset = models.Chapter.objects.all()
    serializer_class = serializers.ChapterSerializer
    search_fields = ('name', 'code')
    filter_fields = {
        'id': ['exact', 'in'],
        'course': ['exact']
    }

@register()
class PassViewSet(BatchActionMixin, viewsets.ModelViewSet):
    queryset = models.Pass.objects.all()
    serializer_class = serializers.PassSerializer
    filter_fields = {
        'id': ['exact', 'in'],
        'course': ['exact'],
        'is_pass': ['exact']
    }

    def filter_queryset(self, queryset):
        qset = super(PassViewSet, self).filter_queryset(queryset)
        if self.action == 'current':
            qset = qset.filter(user=self.request.user)
        return qset

    @decorators.action(['get'], detail=False)
    def current(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @decorators.action(['post'], detail=False)
    def batch_pass(self, request, *args, **kwargs):
        return self.do_batch_action('is_pass')
