from re import search as regular_expression_search


class Context:
    required_context = None
    default_context = {
        "namespace": "default",
        "image_tag": "latest",
        "port": 80,
    }

    def __init__(self, **kwargs):
        self.context = kwargs
        self.cleaned_data = self.default_context
        self.full_clean()

    def full_clean(self):
        self._assert_required_values()
        self._clean_values()

    def _assert_required_values(self):
        if isinstance(self.required_context, (list, tuple)):
            for key in self.required_context:
                if not self.context.get(key):
                    raise ValueError("The value of %s is required" % key)

    def _clean_values(self):
        for key, value in self.context.items():
            self.cleaned_data[key] = value
            if hasattr(self, 'clean_%s' % key):
                value = getattr(self, 'clean_%s' % key)()
                self.cleaned_data[key] = value

    def validate_ingress_name(self, value):
        if not value or regular_expression_search('^[0-9\-]|[^a-z0-9\-]|\-$', value):
            return False
        return True

    def clean_namespace(self):
        value = self.cleaned_data["namespace"]
        if self.validate_ingress_name(value):
            return value
        raise ValueError("Invalid namespace: %s" % value)

    def clean_app_name(self):
        value = self.cleaned_data["app_name"]
        if self.validate_ingress_name(value):
            return value
        raise ValueError("Invalid app_name: %s" % value)
