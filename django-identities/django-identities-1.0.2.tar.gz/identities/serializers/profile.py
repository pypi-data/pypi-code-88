import logging

from rest_framework import serializers

from ..models import Profile


logger = logging.getLogger(__name__)


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        read_only_fields = ("affiliation", "affiliation_id")
        fields = read_only_fields + (
            "display_name",
            "display_id",
        )
