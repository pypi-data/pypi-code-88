from django.contrib.auth.models import AbstractUser
from django.db import models
from django.dispatch import receiver
from guardian.mixins import GuardianUserMixin
from simple_history.models import HistoricalRecords


class User(AbstractUser, GuardianUserMixin):
    email = models.EmailField(
        blank=True, max_length=254, unique=True, verbose_name="email address"
    )


def get_anonymous_user_instance(UserModel):
    return UserModel(username="AnonymousUser", email="anonymous_user@localhost")


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    affiliation = models.CharField(max_length=512, blank=True)
    affiliation_id = models.CharField(max_length=512, blank=True)
    is_tech_account = models.BooleanField(default=False)

    history = HistoricalRecords()

    def __str__(self):
        return f"Profile ({self.user.username})"

    @property
    def display_id(self):
        return (
            f"ID: {self.user.username.split('@')[0]}"
            if "@" in self.user.username
            else None
        )

    @property
    def display_name(self):
        if self.user.first_name or self.user.last_name:
            name = " ".join(filter(bool, (self.user.first_name, self.user.last_name)))
        else:
            name = self.user.username
        display_id = self.display_id and f"({self.display_id})"
        display_email = self.user.email and f"({self.user.email})"
        return " ".join(filter(bool, (f"{name}", display_id, display_email)))


@receiver(models.signals.post_save, sender=User)
def create_or_update_user_profile(
    sender, instance, created, **kwargs
):  # pylint: disable=unused-argument
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
