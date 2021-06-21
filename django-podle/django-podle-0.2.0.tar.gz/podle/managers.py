import logging

from django.contrib.contenttypes.models import ContentType
from django.db import models

from .podle import PodleHelper

logger = logging.getLogger(__name__)


class NewsletterManager(models.Manager):
    def create_or_update_newsletter(self, instance, json_content):
        content_type = ContentType.objects.get_for_model(instance._meta.model)
        object_id = instance.id

        try:
            newsletter = self.get(content_type=content_type, object_id=object_id)
        except self.model.DoesNotExist:
            response = PodleHelper().create_newsletter(json_content)
            logger.debug(response)
            newsletter_id = response["id"]
            return self.create(
                content_type=content_type, object_id=object_id, uuid=newsletter_id
            )

        # If we update the newsletter, it is best to reuse the newsletter uuid
        json_content["newsletterId"] = str(newsletter.uuid)
        PodleHelper().create_newsletter(json_content)
        return newsletter
