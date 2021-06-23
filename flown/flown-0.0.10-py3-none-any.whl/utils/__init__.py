import jinja2
from IPython.core.display import DisplayHandle

jinja_env = jinja2.Environment(loader=jinja2.PackageLoader('flown', 'template'))


def merge_html(template_name: str, params: dict = None, display_id: str = None):
    params = params or {}
    template = jinja_env.get_template(template_name)
    template_param = {
        'display_id': display_id,
        **params
    }
    return template.render(template_param)
