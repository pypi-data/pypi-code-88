from django.urls import path

from .views import NewsletterWebhook


app_name = "podle"
urlpatterns = [
    path("webhook/", NewsletterWebhook.as_view(), name="webhook"),
]
