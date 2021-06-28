from typing import Sequence
from smtplib import SMTPException
import logging

from django.conf import settings
from django.core.mail import EmailMessage

from django_drf_utils.exceptions import ServiceUnavailable

logger = logging.getLogger(__name__)


def sendmail(subject: str, body: str, recipients: Sequence[str], **kwargs):
    if not recipients:
        return
    try:
        EmailMessage(
            subject=(
                settings.CONFIG.email and settings.CONFIG.email.subject_prefix or ""
            )
            + subject,
            body=body,
            from_email=settings.CONFIG.email and settings.CONFIG.email.from_address,
            to=recipients,
            **kwargs,
        ).send(fail_silently=False)
    except SMTPException as e:
        logger.error(
            "Failed to send email notification `{subject}` "
            "SMTP server might not be available or credentials are invalid. "
            "Exception: %s",
            e,
        )
        raise ServiceUnavailable() from e
