from django.urls import path

from .views_api import members_view

app_name = 'loducode_utils'
urlpatterns = [
    path('slack/members/', members_view, name='members_view'),
]