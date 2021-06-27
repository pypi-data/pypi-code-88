from datetime import datetime, timedelta, timezone

from django.conf import settings
from django.db.models import F
from django.conf import settings
from rest_framework.exceptions import ValidationError

from two_factor_auth.models import TwoFactorAuthenticationSession

registration_questions_count = getattr(settings, "REGISTRATION_QUESTIONS_COUNT", 3)
registration_min_answer_count = getattr(
    settings, "USER_REGISTRATION_MIN_ANSWER_COUNT", 2
)
retry_in_seconds = getattr(
    settings, "ANSWER_ATTEMPTS_RETRY_LIFETIME", timedelta(hours=1)
)
invalid_attempt_limit = getattr(settings, "INVALID_ATTEMPTS_LIMIT", 1)


def update_2fa_session(user_id, invalid_attempt=False):
    if invalid_attempt:
        TwoFactorAuthenticationSession.objects.filter(user_id=user_id).update(
            last_answer_attempt=datetime.now(),
            invalid_answer_attempts=F("invalid_answer_attempts") + 1,
        )


def check_2fa_login_attempt(user_id):
    msg = dict()
    try:
        session, created = TwoFactorAuthenticationSession.objects.get_or_create(
            user_id=user_id,
            defaults={
                "last_answer_attempt": datetime.now(),
                "invalid_answer_attempts": 0,
            },
        )

        if session.invalid_answer_attempts >= invalid_attempt_limit:
            if (
                datetime.now(timezone.utc) - session.last_answer_attempt
                < retry_in_seconds
            ):  # noqa
                rem = (
                    session.last_answer_attempt
                    + retry_in_seconds
                    - datetime.now(timezone.utc)
                    + timedelta(minutes=0)
                )
                msg["error"] = f"Invalid Attempts Exceeded, Try After {rem}"
                raise ValidationError(msg, code="authorization")
            else:
                session.last_answer_attempt = datetime.now()
                session.invalid_answer_attempts = 0
                session.save()

    except TwoFactorAuthenticationSession.DoesNotExist:
        msg["error"] = "Invalid User"
        raise ValidationError(msg, code="authorization")
