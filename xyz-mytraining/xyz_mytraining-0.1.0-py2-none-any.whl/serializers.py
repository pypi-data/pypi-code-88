# -*- coding:utf-8 -*- 
# author = 'denishuang'
from __future__ import unicode_literals

from rest_framework.validators import UniqueTogetherValidator
from xyz_restful.mixins import IDAndStrFieldSerializerMixin
from rest_framework import serializers
from . import models


class CourseSerializer(IDAndStrFieldSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = models.Course
        exclude = ()
        read_only_fields = ('user', )
        # validators = [
        #     UniqueTogetherValidator(
        #         queryset=models.Course.objects.all(),
        #         fields=('user', 'name'),
        #         message='相同名称的记录已存在, 请不要重复创建.'
        #     )
        # ]


class TransactionSerializer(IDAndStrFieldSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = models.Transaction
        exclude = ()
        read_only_fields = ('user', )

