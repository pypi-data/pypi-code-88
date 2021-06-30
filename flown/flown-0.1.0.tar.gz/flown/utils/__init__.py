import jinja2
from IPython.core.display import DisplayHandle

from flown.utils import s3util

jinja_env = jinja2.Environment(loader=jinja2.PackageLoader('flown', 'template'))


def merge_html(template_name: str, params: dict = None, display_id: str = None):
    params = params or {}
    template = jinja_env.get_template(template_name)
    template_param = {
        'display_id': display_id,
        **params
    }
    return template.render(template_param)


def to_browsable_url(artifact_location: str, is_obj: bool):
    if artifact_location.startswith('s3:/'):
        return s3util.s3uri_to_console_url(s3uri=artifact_location, is_obj=is_obj)
    elif artifact_location.startswith('file:/'):
        return artifact_location
    else:
        return artifact_location
