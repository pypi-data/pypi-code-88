import sys
from loguru import logger
from typing import List


def check_context(ctx, require: List[str]):
    valid = True
    for r in require:
        if r not in ctx.obj or ctx.obj.get(r, None) is None:
            valid = False
            logger.error(f'Missing parameter: {r}')
    if not valid:
        sys.exit(1)