import traceback

from IPython.core.display import display, update_display
from IPython.display import HTML
from flown.utils import merge_html

def notebook_api(func):
    def wrapper(*args, restricted: bool = False, display_id: str = None, **kwargs):
        # print(f"args = {args}")
        # print(f"restricted = {restricted}")
        # print(f"display_id = {display_id}")
        # print(f"kwargs = {kwargs}")
        # print(f"func = {func}")

        if restricted:
            display_id = None
        elif display_id is None:
            # print(f"not restricted mode , and display_id is None")
            # print(f"display loading.html ...")
            display_handler = display(HTML(merge_html('_loading.html')), display_id=True)
            display_id = display_handler.display_id

        try:
            content_html_str = func(*args, restricted=restricted, display_id=display_id, **kwargs)
            content_html = HTML(content_html_str)
        except Exception as e:
            st = traceback.format_exc()
            content_html = HTML(f"<pre>{st}</pre>")

        if display_id:
            # print(f'update display...')
            update_display(obj=content_html,
                           display_id=display_id)
        else:
            # print(f'display new...')
            # print(f'html = {content_html_str}')
            display(content_html, display_id=True)

    return wrapper

