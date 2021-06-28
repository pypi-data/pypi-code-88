from djangoldp.serializers import LDPSerializer
from djangoldp.views import LDPViewSet
from djangoldp.pagination import LDPPagination


class LDPNotificationsPagination(LDPPagination):
    default_limit = 80


class LDPNotificationsViewSet(LDPViewSet):
    '''overridden LDPViewSet to force pagination'''
    pagination_class = LDPNotificationsPagination
    depth = 0
