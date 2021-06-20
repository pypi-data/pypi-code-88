# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from . import choices
from django.db import models, DataError
from django.contrib.auth.models import User
from django.db import transaction


class Course(models.Model):
    class Meta:
        verbose_name_plural = verbose_name = "课程"
        ordering = ('-is_active', '-create_time',)
        unique_together = ('user', 'name')

    user = models.ForeignKey(User, verbose_name=User._meta.verbose_name, related_name="mytraining_courses",
                             on_delete=models.PROTECT)
    name = models.CharField("名称", max_length=128, blank=False)
    create_time = models.DateTimeField("创建时间", auto_now_add=True)
    is_active = models.BooleanField("有效", blank=False, default=True)
    balance = models.PositiveSmallIntegerField("剩余课时", default=0)

    def __unicode__(self):
        return self.name

    def recount(self):
        bl = 0
        for t in self.transations.order_by('trans_date', 'type'):
            bl += (t.type == choices.TRANS_TYPE_DEPOSIT and 1 or -1) * t.amount
            if bl < 0:
                raise DataError('余额不足')
            t.balance = bl
            t.save()
        self.balance = bl
        self.save()

    def deposit(self, the_date, amount=1, memo=''):
        with transaction.atomic():
            t, created = self.transations.update_or_create(
                trans_date=the_date,
                type=choices.TRANS_TYPE_DEPOSIT,
                defaults=dict(
                    amount=amount,
                    balance=amount,
                    memo=''
                )
            )
            self.recount()

    def withdraw(self, the_date, amount=1, memo=''):
        with transaction.atomic():
            t, created = self.transations.update_or_create(
                trans_date=the_date,
                type=choices.TRANS_TYPE_WITHDRAW,
                defaults=dict(
                    amount=amount,
                    balance=0,
                    memo=''
                )
            )
            self.recount()


class Transaction(models.Model):
    class Meta:
        verbose_name_plural = verbose_name = "交易"
        ordering = ('-create_time',)
        unique_together = ('user', 'course', 'type', 'trans_date')

    user = models.ForeignKey(User, verbose_name=User._meta.verbose_name, related_name="mytraining_transations",
                             on_delete=models.PROTECT)
    course = models.ForeignKey(Course, verbose_name=Course._meta.verbose_name, related_name='transations',
                               on_delete=models.PROTECT)
    type = models.PositiveIntegerField('类别', choices=choices.CHOICES_TRANS_TYPE)
    amount = models.PositiveSmallIntegerField('数量', default=1)
    balance = models.PositiveSmallIntegerField('余额')
    memo = models.CharField('备注', max_length=255, blank=True, default='')
    create_time = models.DateTimeField("创建时间", auto_now_add=True)
    update_time = models.DateTimeField("创建时间", auto_now=True)
    trans_date = models.DateField("创建时间")

    def save(self, **kwargs):
        self.user = self.course.user
        super(Transaction, self).save(**kwargs)

    def __unicode__(self):
        return "%s %s %s @ %s" % (self.user, self.get_type_display(), self.amount, self.trans_date)