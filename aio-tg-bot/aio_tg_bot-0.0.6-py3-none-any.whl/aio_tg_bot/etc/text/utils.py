import jinja2
from aiogram.types import Message

from aio_tg_bot.etc.conf import settings
from aio_tg_bot.utils import module_loading, functional


async def render(template, context=None):
    message = functional.get_current_message()

    if context is None:
        context = {}

    _context = get_context(message)
    _context.update(context)

    template = jinja2.Template(template, enable_async=True, trim_blocks=True)
    return await template.render_async(_context)


def get_context(message):
    context = {}

    for context_processor in settings.TEMPLATES[0]["OPTIONS"]["context_processors"]:
        context_processor = module_loading.import_string(context_processor)

        _context = context_processor(message)
        if isinstance(_context, dict):
            context.update(_context)

    return context
