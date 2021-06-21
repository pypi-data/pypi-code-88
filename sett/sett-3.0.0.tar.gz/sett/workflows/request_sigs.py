from typing import Sequence

from .upload_keys import upload_keys
from ..core.crypt import verify_key_length, search_pub_key
from ..core.error import UserError
from ..utils.log import create_logger
from ..utils.config import Config


logger = create_logger(__name__)


def request_sigs(key_ids: Sequence[str], *, config=Config):
    """Requests signatures"""
    if config.offline:
        raise UserError("Requesting key signature is not possible in offline mode.")
    keys = frozenset(search_pub_key(k, config.gpg_store, sigs=False) for k in key_ids)
    for key in keys:
        verify_key_length(key)
    for key in keys:
        upload_keys((key.fingerprint,), config=config)
        logger.info("Sending a request for '%s'", key.key_id)
        config.portal_api.request_key_signature(key.key_id)
