""" Tracing Middleware """

# Python
import threading

# Models
from .models import Rule


def load_rules():
    try:
        object_list = Rule.objects.filter(is_active=True).values(
            "content_type__model", "check_create", "check_edit", "check_delete"
        )
        rules = {
            obj.get("content_type__model"): {
                "check_create": obj.get("check_create"),
                "check_edit": obj.get("check_edit"),
                "check_delete": obj.get("check_delete"),
            }
            for obj in object_list
        }
    except:
        rules = {}
    print(f"Se cargaron {len(rules)} reglas.")
    return rules


class TracingMiddleware:
    thread_local = threading.local()
    rules = load_rules()

    def __init__(self, get_response):
        self.get_response = get_response

    @classmethod
    def set_data(cls, data):
        cls.thread_local.data = data

    @classmethod
    def get_data(cls):
        if hasattr(cls.thread_local, "data"):
            return cls.thread_local.data

    @classmethod
    def set_user(cls, user):
        cls.thread_local.user = user

    @classmethod
    def get_user(cls):
        if hasattr(cls.thread_local, "user"):
            return cls.thread_local.user

    @classmethod
    def reload_rules(cls):
        cls.rules = load_rules()

    @classmethod
    def get_rule_by_classname(cls, classname):
        if classname.lower() in cls.rules:
            return cls.rules.get(classname.lower())

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called
        self.thread_local.user = request.user

        if request.method == "POST":
            self.thread_local.data = request.POST.dict()
        response = self.get_response(request)
        return response
