from jinja2 import FileSystemLoader, Environment

from k8s import settings


class Template:
    templates_dir = settings.BASE_DIR / "k8s/templates/"
    template_name = None

    def __init__(self, **kwargs):
        self.template_name = kwargs.get('template_name', self.template_name)

    def get_template_name(self):
        if self.template_name is None:
            raise ValueError(
                "%s requires a definition of 'template_name'." % self.__class__.__name__)
        else:
            return self.template_name

    def get_template(self):
        if not hasattr(self, "environment"):
            loader = FileSystemLoader(searchpath=self.templates_dir)
            self.environment = Environment(loader=loader)
        return self.environment.get_template(self.get_template_name())

    def render(self, context=None):
        if context is None:
            context = {}
        self.rendered_template = self.get_template().render(context)
        return self.rendered_template

    def print_rendered_template(self):
        if settings.DEBUG and self.rendered_template:
            print("-" * 80)
            print(self.rendered_template)
            print("-" * 80)
        else:
            print("rendered_template not available!")
