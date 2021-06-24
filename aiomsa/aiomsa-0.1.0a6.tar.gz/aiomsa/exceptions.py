#!/usr/bin/env python3
# Copyright 2004-present Facebook. All Rights Reserved.

from typing import Optional


class AioMsaError(Exception):
    """Base class for all *aiomsa* errors."""

    pass


class DuplicateRouteError(AioMsaError):
    """Raised if more than one route has the same method and path.

    Args:
        msg: The exception message.
    """

    def __init__(self, msg: str) -> None:
        super().__init__(msg)


class ClientError(AioMsaError):
    """Base class for all client errors."""

    pass


class E2ClientError(ClientError):  # pragma: no cover
    """Raised if an :class:`~.E2Client` operation fails.

    Args:
        msg: The exception message.
    """

    def __init__(self, msg: Optional[str] = None) -> None:
        if msg is None:
            msg = "E2Client failure"
        super().__init__(msg)
