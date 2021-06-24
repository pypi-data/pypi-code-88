import logging
from typing import Any, Callable, Dict, Optional, Sequence, Tuple, TypeVar, TypedDict

from django.db.models import Q, QuerySet

from .registry import CodeSeekerRegistry


__all__ = (
    'CodeSeek',
    'CodeSeekSeq',
    'CodesFilter',

    'EMPTY_Q',
    'cmp_AND',
    'cmp_OR',

    'seek_codes_Q',

    'CodeSeekerQuerySet',
)

logger = logging.getLogger(__name__)

QT = TypeVar('QT', bound='CodeSeekerQuerySet')
CodeSeek = Tuple[str, Any]
CodeSeekSeq = Sequence[CodeSeek]


class CodesFilter(TypedDict):
    codes: CodeSeekSeq
    registry: CodeSeekerRegistry
    cmp: Optional[Callable]
    warning_context: Optional[str]


EMPTY_Q = Q()


def cmp_AND(a: Q, b: Q):
    return a & b


def cmp_OR(a: Q, b: Q):
    return a | b


def seek_codes_Q(
    registry: CodeSeekerRegistry,
    codes: CodeSeekSeq,
    cmp: Callable = cmp_AND,
    warning_context: Optional[str] = None
) -> Q:
    q = EMPTY_Q

    for code, value in codes:
        if code not in registry:
            logger.warning(
                f'[CODE-SEEKING-FILTER] No such code "{code}"'
                +
                (
                    f'in {warning_context}.'
                    if warning_context is not None
                    else
                    '.'
                )
            )
            continue

        q = cmp(q, registry[code].Q(value))

    return q


class CodeSeekerQuerySet(QuerySet):
    def seek_codes(
        self,
        registry: CodeSeekerRegistry,
        codes: CodeSeekSeq,
        cmp: Callable = cmp_OR,
        warning_context: str = None
    ) -> QuerySet:
        q = seek_codes_Q(
            registry, codes, cmp=cmp, warning_context=warning_context
        )

        return self.filter(q) if q is not EMPTY_Q else self

    def general_filter(
        self: QT,
        codes_filter: Optional[CodesFilter] = None,
        **kw
    ) -> QT:
        q = super().general_filter(**kw)

        if codes_filter is not None and codes_filter.get('codes') is not None:
            q = q.seek_codes(**codes_filter)

        return q