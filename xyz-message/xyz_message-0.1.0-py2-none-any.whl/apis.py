# -*- coding:utf-8 -*-
from xyz_restful.mixins import BatchActionMixin, UserApiMixin

__author__ = 'denishuang'

from . import models, serializers
from rest_framework import viewsets, decorators, response
from xyz_restful.decorators import register


@register()
class TaskViewSet(UserApiMixin, viewsets.ModelViewSet):
    queryset = models.Task.objects.all()
    serializer_class = serializers.TaskSerializer
    search_fields = ['title', 'link']
    filter_fields = {
        "is_force": ['exact'],
        "is_active": ['exact'],
        "is_sent": ['exact'],
        "category": ['exact'],
        "send_time": ['range']
    }


@register()
class MessageViewSet(BatchActionMixin, viewsets.ModelViewSet):
    queryset = models.Message.objects.all()
    serializer_class = serializers.MessageSerializer
    filter_fields = {
        "is_force": ['exact'],
        "is_read": ['exact'],
        "is_active": ['exact'],
        "task": ['exact'],
    }
    search_fields = ['title']

    @decorators.action(['POST'], detail=False)
    def batch_read(self, request):
        from datetime import datetime
        return self.do_batch_action('is_read', True, extra_params={'read_time': datetime.now()})

    @decorators.action(['POST'], detail=True)
    def read(self, request, pk):
        from datetime import datetime
        message = self.get_object()
        message.is_read = True
        message.read_time = datetime.now()
        message.save()
        return response.Response({'detail': 'Success'})

    def get_queryset(self):
        qset = super(MessageViewSet, self).get_queryset()
        if self.action == 'current':
            from datetime import datetime
            user = self.request.user
            if user.is_authenticated:
                qset = qset.filter(receiver=user, expiration__gt=datetime.now())
        return qset

    @decorators.action(methods=['GET'], detail=False)
    def current(self, request):
        return self.list(request)
