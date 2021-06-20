# -*- coding:utf-8 -*-
from __future__ import division

from django.db import DataError
from xyz_restful.mixins import UserApiMixin, BatchActionMixin
from . import models, serializers
from rest_framework import viewsets, decorators, response, status
from xyz_restful.decorators import register


@register()
class CourseViewSet(UserApiMixin, BatchActionMixin, viewsets.ModelViewSet):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer
    search_fields = ('name',)
    filter_fields = {
        'id': ['in', 'exact'],
        'is_active': ['exact'],
        'name': ['exact'],
        'create_time': ['range']
    }
    ordering_fields = ('is_active', 'name', 'create_time')

    @decorators.action(['POST'], detail=False)
    def batch_active(self, request):
        return self.do_batch_action('is_active', True)

    @decorators.action(['POST'], detail=True)
    def deposit(self, request, pk):
        course = self.get_object()
        data = request.data
        the_date = data.pop('the_date')
        course.deposit(the_date, **data)
        s = self.get_serializer(instance=course)
        return response.Response(s.data)

    @decorators.action(['POST'], detail=True)
    def withdraw(self, request, pk):
        course = self.get_object()
        data = request.data
        the_date = data.pop('the_date')
        try:
            course.withdraw(the_date, **data)
            s = self.get_serializer(instance=course)
            return response.Response(s.data)
        except DataError as e:
            return response.Response({'detail': e.message}, status=status.HTTP_406_NOT_ACCEPTABLE)



    # @decorators.list_route(['get'])
    # def stat(self, request):
    #     return do_rest_stat_action(self, stats.stats_paper)
    #

@register()
class TransactionViewSet(UserApiMixin, viewsets.ModelViewSet):
    queryset = models.Transaction.objects.all()
    serializer_class = serializers.TransactionSerializer
    filter_fields = {
        'id': ['in', 'exact'],
        'type': ['exact'],
        'course': ['exact'],
        'trans_date': ['range'],
        'create_time': ['range']
    }
    ordering_fields = ('type', 'trans_date')
