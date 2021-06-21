import logging

from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .signals import audio_file
from .models import Newsletter
from .serializers import NewsletterSerializer

logger = logging.getLogger(__name__)


@method_decorator(csrf_exempt, name="dispatch")
class NewsletterWebhook(APIView):
    serializer_class = NewsletterSerializer

    def post(self, request, *args, **kwargs):
        newsletter_id = request.data.get("id", None)
        newsletter = get_object_or_404(Newsletter, uuid=newsletter_id)
        serializer = self.serializer_class(newsletter, data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info(
                f"Audio file url saved successfully for newsletter {newsletter.uuid}"
            )
            audio_file.send(
                sender=Newsletter,
                success=True,
                audio_url=serializer.validated_data["newsletter_url"],
                newsletter=newsletter,
            )
            return Response(data={"success": True}, status=status.HTTP_200_OK)

        audio_file.send(sender=Newsletter, success=False, errors=serializer.errors)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
