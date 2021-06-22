import json
from django.http import HttpResponse
from django.conf import settings
from django.http import JsonResponse
from oauth2_provider.models import AccessToken

class TrimMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_view(self, request, view_fun, view_args, view_kwargs):

        if request.method == "POST":
            try:
                request_body = json.loads(request.body)
            except:
                request_body = {}
            for key in request_body:
                try:
                    request_body[key] = request_body[key].strip()
                except:
                    request_body[key] = request_body[key]
            if request_body:
                request._body = bytes(json.dumps(request_body), "utf-8")

class MaintenanceModeMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    # Check if client IP is allowed
    def process_view(self, request, view_fun, view_args, view_kwargs):
        try:
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                ip = x_forwarded_for.split(',')[0]
            else:
                ip = request.META.get('REMOTE_ADDR')

            IS_MAINTENANCE_MODE = False
            MAINTENANCE_IPS = []
            try:
                IS_MAINTENANCE_MODE = settings.IS_MAINTENANCE_MODE
            except:
                pass

            try:
                MAINTENANCE_IPS = settings.MAINTENANCE_IPS
            except:
                pass

            SHOW_MAINTANCE_INVALID_IP = False
            try:
                SHOW_MAINTANCE_INVALID_IP = settings.SHOW_MAINTANCE_INVALID_IP
            except:
                pass

            message = 'Site under maintenance. '
            if SHOW_MAINTANCE_INVALID_IP:
                message += '  -- invalid IP -'  +str(ip)

            if IS_MAINTENANCE_MODE and ip not in MAINTENANCE_IPS:
                return JsonResponse({'status': False, 'code': 503, 'data':[], 'message':[message] }, status=503)
        except:
            pass
    

METHOD_LIST = {
    "list": "view_",
    "retrieve": "view_",
    "create": "add_",
    "partial_update": "change_",
    "delete": "delete_",
    "change_status": "change_",
    "bulk_delete": "add_",
}

SKIP_ENDPOINT = ["logout", "login", "revoke_token", "token"]

class UserRolePermission(object):
    def __init__(self, get_response):
        self.get_response = get_response
        self.debug_helper = {}

    def __call__(self, request):
        return self.get_response(request)

    def process_view(self, request, view_func, view_args, view_kwargs):
        SKIP_THIS = False
        try:
            SKIP_ENDPOINT += settings.SKIP_ENDPOINT
        except:
            pass

        try:
            requestURL = request.build_absolute_uri("?").split("/")[:-1][-1]
            if requestURL in SKIP_ENDPOINT:
                SKIP_THIS = True
        except:
            pass

        if not SKIP_THIS:
            permission = ""
            
            try:
                SETTINGS_METHOD = settings.ALLOWED_METHOD_PERMISSIONS
                METHOD_LIST.update(SETTINGS_METHOD)
            except:
                pass

            try:
                show_permission_error = settings.SHOW_PERMISSION_ERROR
            except:
                show_permission_error = False

            str_method = ''
            try:
                str_method = view_func.__dict__.get("actions").get(str(request.method).lower())
                permission = (
                    METHOD_LIST.get(str_method)
                    + view_func.__module__.split(".")[-1]
                )

            except:
                pass

            token = request.META.get("HTTP_AUTHORIZATION", None)
            if token:
                token = token.split(" ")[1]

            token_obj = AccessToken.objects.filter(token=token).select_related("user").first()
            if token_obj:
                if permission == "":
                    
                    message = 'Permission not matched.'

                    if show_permission_error:
                        message += ' invalid permission -> ' + str_method

                    return JsonResponse(
                        {
                            "message": [message],
                            "code": 400,
                            "success": False,
                            "data": {},
                        },
                        status=400,
                    )
                try:
                    request_user = token_obj.user.role.permissions.filter(codename=permission)
                except:
                    request_user = token_obj.user.group.permissions.filter(codename=permission)

                if not request_user:
                    message = "You don't have access to perform this action."

                    if show_permission_error:
                        message += ' invalid permission -> ' + str_method

                    return JsonResponse(
                        {
                            "message": [message],
                            "code": 403,
                            "success": False,
                            "data": {},
                        },
                        status=403,
                    )
