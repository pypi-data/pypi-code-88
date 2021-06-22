"""Declares :class:`TemplateService`."""
import functools
import operator

import django.template.loader


class TemplateService:
    """Provides an interface to render templates using the Django
    template framework.
    """
    default_prefix = None

    def __init__(self, prefix=None):
        self.prefix = prefix or self.default_prefix

    def abspath(self, template_name):
        """Return a list holding the full paths to `template_name`."""
        template_names = []
        if isinstance(template_name, (list, tuple)):
            return functools.reduce(operator.add,
                [self.abspath(x) for x in template_name], [])

        if self.prefix:
            template_names.append(self._prefix_template_name(template_name))
        template_names.append(template_name)
        return template_names

    def get_template(self, template_name, using=None):
        """Load the given template and return a renderable :class:`Template`
        object.
        """
        return self._select_template(self.abspath(template_name), using=using)

    def render_to_string(self, template_name, ctx=None, request=None, using=None):
        """Renders the template `template_name` to a string."""
        template = self.get_template(template_name, using=using)
        return template.render(ctx, request)

    def _select_template(self, template_names, using=None):
        return django.template.loader.select_template(
            template_names, using=using)

    def _prefix_template_name(self, template_name):
        assert self.prefix
        return str.rstrip(self.prefix, '/') + '/'\
            + str.lstrip(template_name, '/')
