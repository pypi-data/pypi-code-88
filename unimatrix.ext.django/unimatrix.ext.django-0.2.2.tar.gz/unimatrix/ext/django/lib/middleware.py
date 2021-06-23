"""Middleware to report application status to the infrastructure."""
import logging
import os

from django.http import HttpResponse
from django.http import JsonResponse


class HealthCheckMiddleware:
    """Intercepts ``GET`` requests on ``/.well-known/probe/live``
    and ``/.well-known/probe/ready`` to report application health.
    """
    logger = logging.getLogger("probe")

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = None
        if request.method == "GET":
            if request.path == "/.well-known/health/ready":
                response = self.ready(request)
            elif request.path == "/.well-known/health/live":
                response = self.live(request)
            elif request.path == '/.well-known/metadata':
                response = self.metadata(request)
            elif request.path == '/.well-known/commit':
                response = self.commit(request)
        return response or self.get_response(request)

    def commit(self, request):
        """Return the commit from which the current runtime was built."""
        return HttpResponse(os.getenv('VCS_COMMIT_HASH') or 'noop',
            content_type="text/plain")

    def live(self, request):
        """Respond with ``200 OK``."""
        self.logger.info("Received liveness probe from %s",
            request.META['REMOTE_ADDR'])
        return HttpResponse("OK")

    def metadata(self, request):
        """Return a datastructure with information about the current
        application.
        """
        dto = {
            'commit': os.getenv('VCS_COMMIT_HASH')
        }
        return JsonResponse(dto)

    def ready(self, request):
        """Respond with ``200 OK`` if all services are operational."""
        self.logger.info("Received readyness probe from %s",
            request.META['REMOTE_ADDR'])
        return HttpResponse("OK")
