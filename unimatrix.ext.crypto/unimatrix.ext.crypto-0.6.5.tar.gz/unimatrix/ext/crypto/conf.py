"""Provides the interface to configure the :mod:`unimatrix.ext.crypto`
package at runtime.
"""
import asyncio

import ioc.loader
from unimatrix.lib import meta
from unimatrix.lib.datastructures import ImmutableDTO


@meta.allow_sync
async def configure(**config):
    """Configure the :mod:`unimatrix.ext.crypto` package."""
    config = ImmutableDTO.fromdict(config)

    # Run all loaders if they are configured.
    futures = []
    for loader_config in (config.get('loaders') or []):
        Loader = ioc.loader.import_symbol(loader_config.loader)
        instance = Loader(
            loader_config.options,
            public_only=loader_config.get('public_only', False)
        )
        futures.append(instance.load())

    if futures:
        await asyncio.gather(*futures)
