from json.decoder import JSONDecodeError
from logging import getLogger
from typing import Optional

from requests.exceptions import RequestException

from ruleau.constants import OverrideLevel
from ruleau.exceptions import APIException
from ruleau.rule import Rule

logger = getLogger(__name__)
logger.propagate = True


def api_request(func):
    def _api_request(*args, **kwargs) -> Optional[dict]:
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.error(f"Exception occured: {e}")
            raise e

    return _api_request


def rule(
    rule_id,
    name,
    depends_on=None,
    override_level=OverrideLevel.ANY_OVERRIDE,
    lazy_dependencies=False,
):
    """Decorator to encapsulate a function into a rule"""
    depends_on = depends_on or []

    def _rule(func) -> Rule:
        return Rule(func, rule_id, name, depends_on, override_level, lazy_dependencies)

    return _rule
