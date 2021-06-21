from typing import List, Tuple, Dict, Optional
import json

from ..utils.config import Config
from ..utils.log import create_logger, log_timing
from ..utils.progress import ProgressInterface
from ..core.crypt import get_recipient_email, retrieve_refresh_and_validate_keys, gpg
from ..core.archive import check_package, extract, METADATA_FILE, DATA_FILE_ENCRYPTED
from ..core.metadata import load_metadata
from ..core.error import UserError
from ..protocols import Protocol


logger = create_logger(__name__)


@log_timing(logger)
def transfer(
    files: List[str],
    *,
    protocol: Protocol,
    config: Config,
    dry_run: bool = False,
    verify_dtr: Optional[bool] = None,
    progress: ProgressInterface = None,
):
    """Transfer file(s) to the selected recipient on the BiomedIT network."""

    logger.info(
        """Input summary:
    files to transfer: %s"
    dry run          : %s""",
        "\n\t".join(files),
        str(dry_run),
    )

    with logger.log_task("Input data check"):
        for archive_path in files:
            check_package(archive_path)

    files_by_recipient: Dict[Tuple[gpg.Key, ...], List[str]] = {}
    with logger.log_task("Extracting destination for each file to transfer"):
        for archive_path in files:
            logger.info("\t-> %s", archive_path)
            with extract(archive_path, METADATA_FILE, DATA_FILE_ENCRYPTED) as (
                metadata,
                encrypted_file,
            ):
                metadata = json.load(metadata)
                keys = tuple(
                    retrieve_refresh_and_validate_keys(
                        key_search_terms=gpg.extract_key_id(encrypted_file),
                        gpg_store=config.gpg_store,
                        key_authority_fingerprint=config.key_authority_fingerprint,
                        keyserver_url=config.keyserver_url,
                    )
                )
            metadata = load_metadata(metadata)
            if verify_dtr is None:
                verify_dtr = metadata.transfer_id is not None
            if verify_dtr:
                if metadata.transfer_id is None:
                    raise UserError(
                        "DTR (Data Transfer Request) ID is missing in file metadata."
                    )
                try:
                    project_code = config.portal_api.verify_transfer(
                        metadata=metadata, filename=archive_path
                    )
                    logger.info(
                        "DTR ID '%s' is valid for project '%s'",
                        metadata.transfer_id,
                        project_code,
                    )
                except RuntimeError as e:
                    raise UserError(format(e)) from e
            files_by_recipient.setdefault(keys, []).append(archive_path)

    if dry_run:
        logger.info("Dry run completed successfully")
        return

    for recipient_keys, r_files in files_by_recipient.items():
        emails = [get_recipient_email(k) for k in recipient_keys]
        if hasattr(protocol, "recipients"):
            setattr(protocol, "recipients", emails)
        if hasattr(protocol, "pkey_password_encoding"):
            setattr(protocol, "pkey_password_encoding", config.ssh_password_encoding)
        with logger.log_task(
            "Transferring files encrypted for " f"{', '.join(emails)}"
        ):
            protocol.upload(r_files, progress=progress)
