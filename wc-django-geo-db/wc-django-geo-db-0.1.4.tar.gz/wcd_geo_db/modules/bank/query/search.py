from typing import Optional, TypeVar

from .base import QuerySet


__all__ = 'SearchQuerySet',

QT = TypeVar('QT', bound='SearchQuerySet')


class SearchQuerySet(QuerySet):
    def search(self: QT, query: str) -> QT:
        return self

    def general_filter(
        self: QT,
        search_query: Optional[str] = None,
        **kw
    ) -> QT:
        q = super().general_filter(**kw)

        if search_query is not None:
            return q.search(query=search_query)

        return q
