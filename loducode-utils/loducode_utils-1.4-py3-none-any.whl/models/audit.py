import uuid

from crum import get_current_user
from django.contrib.auth import get_user_model
from django.db.models import Model, UUIDField, DateTimeField, ForeignKey, CASCADE
from django.utils.translation import ugettext_lazy as _


class Audit(Model):
    '''Audit Model
    AuditModel acts as an abstract base class from which every
    other model in the project will inherit. This class provides
    every table with the following attributes:
        + created_at (DateTime): Stores the datetime the object was created.
        + modified_at (DateTime): Stores the last datetime the object was modified.
        + created_by (ForeignKey): Stores the user who created the object.
        + modified_by (ForeignKey): Stores the user who modified the object.
    '''
    id: UUIDField = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = DateTimeField(
        auto_now_add=True,
        verbose_name=_('creation date'),
        help_text=_('date when the object was created'),
        db_index=True
    )
    modified_at = DateTimeField(
        auto_now=True,
        verbose_name=_('update date'),
        help_text=_('date when the object was modified'),
    )
    created_by = ForeignKey(
        get_user_model(), on_delete=CASCADE,
        related_name='%(class)s_created_by',
        null=True, blank=True,
        verbose_name=_('creation user'),
        help_text=_('user who created the object'),
    )
    modified_by = ForeignKey(
        get_user_model(), on_delete=CASCADE,
        related_name='%(class)s_modified_by',
        null=True, blank=True,
        verbose_name=_('update user'),
        help_text=_('user who performed the update'),
    )

    class Meta:
        abstract = True
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user:
            if self.created_at is None and not user.is_anonymous:
                self.created_by = user
                self.modified_by = user
            elif not user.is_anonymous:
                self.modified_by = user
        super(Audit, self).save(*args, **kwargs)