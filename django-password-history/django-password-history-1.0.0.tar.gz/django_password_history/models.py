from django.db import models
from django.conf import settings
from django.apps import apps
from django.contrib.auth.hashers import make_password, check_password


class UserPasswordHistory(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    password_1 = models.CharField(blank=True, null=True, max_length=128)
    password_2 = models.CharField(blank=True, null=True, max_length=128)
    password_3 = models.CharField(blank=True, null=True, max_length=128)
    password_4 = models.CharField(blank=True, null=True, max_length=128)
    password_5 = models.CharField(blank=True, null=True, max_length=128)
    updated_at = models.DateTimeField(auto_now=True)

    def password_is_used(self, password):
        if settings.PREVIOUS_PASSWORD_COUNT:
            previous_passwords_count = settings.PREVIOUS_PASSWORD_COUNT
        else:
            previous_passwords_count = 5

        if previous_passwords_count:
            for x in range(1, min(previous_passwords_count, 5) + 1):
                f = getattr(self, f'password_{x}', None)
                if f is not None and check_password(password, f):
                    return True

        return False

    def store_password(self):
        self.password_5 = self.password_4
        self.password_4 = self.password_3
        self.password_3 = self.password_2
        self.password_2 = self.password_1
        self.password_1 = self.user.password
        self.save()
