"""Dockie error package initialization module"""
from .base_exceptions import (
    DockieError,
    DockieBadRequestError,
    DockiePermissionDeniedError,
    DockieResourceNotFoundError,
    DockieResourceConflictError,
    DockieBadGatewayError,
    DockieNotAllowedError,
    DockieNotImplementedError
)


__all__ = [
    'DockieError',
    'DockieBadRequestError',
    'DockiePermissionDeniedError',
    'DockieResourceNotFoundError',
    'DockieResourceConflictError',
    'DockieBadGatewayError',
    'DockieNotAllowedError',
    'DockieNotImplementedError'
]
