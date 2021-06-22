"""
This is a models.py file for otp module
"""
import datetime
import random
import re

from django.conf import settings
from django.db import models
from django.utils import timezone


# Create your models here.
class OtpModel(models.Model):
    """
    This model hold otp code and user id information
    """
    code = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    user_id = models.CharField(max_length=100)
    is_valid = models.BooleanField(default=True)
    expires_on = models.DateTimeField()
    remaining_attempts = models.IntegerField(default=settings.OTP_REMAINING_ATTEMPTS)
    can_send_otp_after = models.DateTimeField(auto_now_add=True)

    def is_valid_otp(self, otp):
        if len(re.findall("\d{4}", str(otp))):
            return True
        return False

    def update_attempts(self):
        self.remaining_attempts -= 1
        if self.remaining_attempts == 0:
            """
            if there are more than 5 attempts
            - expire current otp
            - update can_send_otp_after to future time so that user can be blocked
            """
            otp_window = settings.OTP_BLOCK_WINDOW_MIN
            time_ = timezone.now() + datetime.timedelta(minutes=otp_window)
            self.is_valid = False
            self.can_send_otp_after = time_
        self.save()
        return self.remaining_attempts

    def can_use_otp(self):
        if timezone.now() < self.can_send_otp_after:
            time_remaining = int((self.can_send_otp_after - timezone.now()).total_seconds() // 60)
            if time_remaining <=0:
                time_remaining = 1
            raise AssertionError(
                'You can use OTP feature after {} minute{}'.format(time_remaining,
                    's' if time_remaining>1 else ''))

    @classmethod
    def set_otp(cls, user_id, expiry_time):
        """
        This method can be used to set new otp and change status to active.
        This should be used in case want to generate new otp.
        Args:
            user_id: the id of user for which we need to generate otp.
            expiry_time: time(in seconds) after which otp expires
        Response:
             new otp
        """
        instance = cls.get_obj(user_id)

        new_code = random.randint(1111, 9999)
        expires_on = timezone.now() + datetime.timedelta(seconds=expiry_time)
        if instance is not None:
            # check is user is blocked
            instance.can_use_otp()

            # case when getting otp first time.
            instance.code = new_code
            instance.is_valid = True
            instance.remaining_attempts = settings.OTP_REMAINING_ATTEMPTS
            instance.expires_on = expires_on
            instance.save()
            return new_code
        cls.objects.create(user_id=user_id, code=new_code, expires_on=expires_on,
                           remaining_attempts=settings.OTP_REMAINING_ATTEMPTS)
        return new_code

    @classmethod
    def get_obj(cls, user_id):
        """
        This method is used for getting otp object for a user id
        :params user_id
        Response: object or None
        """
        try:
            return cls.objects.get(user_id=user_id)
        except cls.DoesNotExist:
            return None

    @classmethod
    def validate_otp(cls, user_id, code):
        """
        This method is used to validate otp for a given user_id
        Args:
            user_id: id for user
            code: otp code to match
        Response:
            Boolean: True/False
        """
        obj = cls.get_obj(user_id)
        obj.can_use_otp()
        response_code = 0
        if not (obj.is_valid_otp(code) and obj.code == int(code)):
            response_code = -1 #otp is invalid, attempts will be reduced
            remaining_attempts = obj.update_attempts()
            return False, remaining_attempts, response_code
        if not (obj.is_valid and timezone.now() <= obj.expires_on):
            response_code = -2# otp has expired
            remaining_attempts = obj.update_attempts()
            return False, remaining_attempts, response_code
        obj.is_valid = False
        obj.remaining_attempts = 5
        obj.save()
        return True, obj.remaining_attempts, response_code
