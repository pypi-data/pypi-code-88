"""Declares :class:`EmailService`."""
import ioc
from django.core.mail import send_mail
from django.conf import settings


class EmailService:
    """Provides an interface to send transactional emails."""

    def send(self, sender, subject, recipients, text, html):
        """Sends an email to the specified recipients."""
        if sender is None:
            sender = settings.DEFAULT_FROM_EMAIL
        return send_mail(subject, text, sender, recipients,
            html_message=html)

    @ioc.inject('template', 'TemplateService')
    def send_from_templates(self, sender, subject, recipients, text, html,
        ctx, template):
        """Sends an email to the specified recipients using templates."""
        if not text and not html:
            raise ValueError("Specify at least one of `text`, `html`.")
        if text:
            text = template.render_to_string(text, ctx)
        if html:
            html = template.render_to_string(html, ctx)
        return self.send(sender, subject, recipients, text, html)
