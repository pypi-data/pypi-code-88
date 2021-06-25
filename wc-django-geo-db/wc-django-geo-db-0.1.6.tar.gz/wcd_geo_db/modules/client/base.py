from functools import cached_property
from wcd_geo_db.conf import Settings


__all__ = 'Client', 'NestedClient'


class Client:
    settings: Settings

    def __init__(self, *_, **kw):
        settings = kw.get('settings', None)

        assert settings is not None, 'Settings required to use client.'

        self.settings = settings
        self.kw = kw


class NestedClient(Client):
    parent: Client

    def __init__(self, *_, parent = None, **kw):
        assert parent is not None, 'Nested client must have a parent relation.'

        super().__init__(**kw)

        self.parent = parent

    @classmethod
    def as_property(cls, **kw) -> 'NestedClient':
        return cached_property(lambda self: cls(parent=self, **{**self.kw, **kw}))
