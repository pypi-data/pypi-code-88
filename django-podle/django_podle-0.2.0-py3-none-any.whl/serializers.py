from rest_framework import serializers


class NewsletterSerializer(serializers.Serializer):
    newsletter_url = serializers.CharField()

    def update(self, instance, validated_data):
        instance.audio_url = validated_data.get("newsletter_url", instance.audio_url)
        instance.save()
        return instance
