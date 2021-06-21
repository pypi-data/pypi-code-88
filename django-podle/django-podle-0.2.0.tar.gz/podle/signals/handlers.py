import logging

from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver

from ..models import Dictionary
from ..podle import PodleHelper

logger = logging.getLogger(__name__)


@receiver(pre_save, sender=Dictionary)
def create_or_update_dictionary_word(sender, instance, *args, **kwargs):
    response = PodleHelper().create_or_update_word(
        {"value": instance.pronunciation, "raw": instance.word}
    )
    if "added" not in response:
        logger.error(response)
        raise Exception(response)

    logger.info(response)


@receiver(pre_delete, sender=Dictionary)
def delete_dictionary_word(sender, instance, *args, **kwargs):
    response = PodleHelper().delete_word(instance.word)
    if "deleted" not in response:
        logger.error(response)
        raise Exception(response)

    logger.info(response)
