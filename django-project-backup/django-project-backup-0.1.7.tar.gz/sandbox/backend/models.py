from django.contrib.auth.models import AbstractUser, Group
from django.db import models
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    base_group = models.ForeignKey(Group, verbose_name=_("Base Group"),
                                   related_name='base_users', blank=True, null=True,
                                   on_delete=models.SET_NULL)

    parent = models.OneToOneField('backend.User', verbose_name=_("Parent"), blank=True, null=True,
                                  related_name='child',
                                  on_delete=models.SET_NULL)

    friends = models.ManyToManyField('backend.User', verbose_name=_("Friends"), blank=True, null=True)
