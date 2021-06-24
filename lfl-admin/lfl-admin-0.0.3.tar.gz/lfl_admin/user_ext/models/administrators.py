import logging

from bitfield import BitField
from django.db.models import OneToOneField, PROTECT, DateTimeField

from isc_common.auth.models.user import User
from isc_common.fields.related import ForeignKeyProtect
from isc_common.models.audit import AuditQuerySet, AuditManager, AuditModel, Model_withOldId
from lfl_admin.common.models.posts import Posts

logger = logging.getLogger(__name__)


class AdministratorsQuerySet(AuditQuerySet):
    def delete(self):
        return super().delete()

    def create(self, **kwargs):
        return super().create(**kwargs)

    def filter(self, *args, **kwargs):
        return super().filter(*args, **kwargs)


class AdministratorsManager(AuditManager):
    @classmethod
    def props(cls):
        return BitField(flags=(
            ('active', 'Актуальность'),  # 1
            ('send_email', 'send_email'),  # 2
            ('kdk_fine_deleting', 'kdk_fine_deleting'),  # 4
            ('person_editing', 'person_editing'),  # 8
            ('all_news_access', 'all_news_access'),  # 16
            ('public_access', 'public_access'),  # 32
            ('transfer_right', 'transfer_right'),  # 64
            ('news', 'news'),  # 128
            ('documents', 'documents'),  # 256
            ('official', 'official'),  # 512
            ('video', 'video'),  # 1024
            ('blocks', 'blocks'),  # 2048
            ('upload', 'upload'),  # 4096
            ('tournament_members', 'tournament_members'),  # 8192
        ), default=1, db_index=True)

    @staticmethod
    def getRecord(record):
        res = {
            'id': record.id,
            'editing': record.editing,
            'deliting': record.deliting,
        }
        return res

    def get_queryset(self):
        return AdministratorsQuerySet(self.model, using=self._db)

    def get_user(self, old_id):
        editor = super().getOptional(old_id=old_id)
        if editor is None:
            return None
        return editor.user


class Administrators(AuditModel, Model_withOldId):
    editor = ForeignKeyProtect(User, related_name='Administrators_editor', null=True, blank=True)
    register_date = DateTimeField(null=True, blank=True)
    user = OneToOneField(User, on_delete=PROTECT)

    props = AdministratorsManager.props()

    objects = AdministratorsManager()

    @classmethod
    def unknown(cls):
        res, _ = cls.objects.get_or_create(user=User.unknown())
        return res

    def __str__(self):
        return f'ID:{self.id}'

    def __repr__(self):
        return self.__str__()

    class Meta:
        verbose_name = 'Кросс-таблица'
