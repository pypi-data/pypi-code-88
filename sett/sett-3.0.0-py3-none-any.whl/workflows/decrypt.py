import os
import json

from functools import partial
from typing import List, Optional

from ..core.error import UserError
from ..core.archive import (
    check_package,
    extract,
    unpack_from_stream,
    METADATA_FILE,
    DATA_ARCHIVE,
    DATA_FILE_ENCRYPTED,
    CHECKSUM_FILE,
    extract_with_progress,
)
from ..core.crypt import (
    decrypt as core_decrypt,
    retrieve_refresh_and_validate_keys,
    fingerprint2keyid,
    verify_metadata_signature,
    gpg,
)
from ..core.filesystem import DeleteDirOnError, unique_filename
from ..core.checksum import (
    verify_checksums,
    compute_checksum_sha256,
    read_checksum_file,
)
from ..core.metadata import MetaData
from ..core.secret import Secret
from ..utils.log import create_logger, log_timing
from ..utils.progress import ProgressInterface, subprogress
from ..utils.config import Config


logger = create_logger(__name__)


@log_timing(logger)
def decrypt(
    files: List[str],
    *,
    passphrase: Optional[Secret] = None,
    output_dir: str,
    config: Config,
    decrypt_only: bool = False,
    dry_run: bool = False,
    progress: Optional[ProgressInterface] = None,
):
    """Decrypt and decompress an input .tar file."""

    logger.info(
        """Input summary:
    file(s) to decrypt: %s
    output_dir: %s
    dry_run: %s
""",
        "\n\t".join(files),
        output_dir,
        dry_run,
    )

    with logger.log_task("Input data check"):
        for archive_path in files:
            check_package(archive_path)

    if dry_run:
        logger.info("Dry run completed successfully")
        return

    for archive_file in files:
        # Reset progress for each tar file
        if progress is not None:
            progress.update(0.0)
        logger.info("Processing file %s", archive_file)
        decrypt_archive(
            archive_file,
            passphrase=passphrase,
            output_dir=output_dir,
            config=config,
            decrypt_only=decrypt_only,
            progress=progress,
        )
        logger.info("Data decryption completed successfully.")


def decrypt_archive(
    archive_file: str,
    passphrase: Optional[Secret],
    output_dir: str,
    config: Config,
    decrypt_only: bool = False,
    progress: Optional[ProgressInterface] = None,
):

    # To avoid overwriting files, each archive is unpacked in a directory
    # that has the same name as the archive file minus its extension.
    out_dir = unique_filename(
        os.path.splitext(os.path.join(output_dir, os.path.basename(archive_file)))[0]
    )

    with DeleteDirOnError(out_dir):
        with logger.log_task("Verifying signatures..."):
            verify_metadata_signature(
                tar_file=archive_file,
                gpg_store=config.gpg_store,
                signee_fingerprint=None,
                key_authority_fingerprint=config.key_authority_fingerprint,
                keyserver_url=config.keyserver_url,
                validate_key_origin=False,
            )

        with logger.log_task("Verifying encryption keys..."), extract(
            archive_file, DATA_FILE_ENCRYPTED
        ) as f_data:
            keys = retrieve_refresh_and_validate_keys(
                key_search_terms=gpg.extract_key_id(f_data),
                gpg_store=config.gpg_store,
                key_authority_fingerprint=config.key_authority_fingerprint,
                keyserver_url=config.keyserver_url,
            )
            logger.info(
                "Data encrypted for:\n%s",
                "\n".join(
                    f"User ID    : {key.uids[0]}\n" f"Fingerprint: {key.fingerprint}"
                    for key in keys
                ),
            )

        with logger.log_task("Verifying checksums..."), subprogress(
            progress, step_completion_increase=0.05
        ) as scaled_progress, extract_with_progress(
            archive_file, scaled_progress, METADATA_FILE, DATA_FILE_ENCRYPTED
        ) as (
            f_metadata,
            f_data,
        ):
            metadata = MetaData.from_dict(json.load(f_metadata))
            if metadata.checksum.lower() != compute_checksum_sha256(f_data):
                raise UserError(f"Checksum mismatch for {f_data.name}")

        with logger.log_task("Decrypting data..."), subprogress(
            progress, step_completion_increase=0.9
        ) as scaled_progress, extract_with_progress(
            archive_file, scaled_progress, DATA_FILE_ENCRYPTED
        ) as f_data:
            os.makedirs(out_dir, exist_ok=True)
            if decrypt_only:
                sender_fprs = core_decrypt(
                    source=f_data,
                    output=os.path.join(out_dir, DATA_ARCHIVE),
                    gpg_store=config.gpg_store,
                    passphrase=passphrase,
                )
            else:
                unpacked: List[str] = list()
                sender_fprs = core_decrypt(
                    source=f_data,
                    output=partial(unpack_from_stream, dest=out_dir, content=unpacked),
                    gpg_store=config.gpg_store,
                    passphrase=passphrase,
                )
                log_files(unpacked)
            sender_sig_keys = retrieve_refresh_and_validate_keys(
                key_search_terms=map(fingerprint2keyid, sender_fprs),
                gpg_store=config.gpg_store,
                key_authority_fingerprint=config.key_authority_fingerprint,
                keyserver_url=config.keyserver_url,
            )
            logger.info(
                "Data signed by:\n%s",
                "\n".join(
                    f"User ID    : {key.uids[0]}\n" f"Fingerprint: {key.fingerprint}"
                    for key in sender_sig_keys
                ),
            )

        with subprogress(progress, step_completion_increase=0.05) as scaled_progress:
            if not decrypt_only:
                with logger.log_task(
                    "Checksum verification of uncompressed data..."
                ), open(os.path.join(out_dir, CHECKSUM_FILE), "rb") as fout:
                    sha_checks = list(read_checksum_file(fout))
                    verify_checksums(sha_checks, out_dir)
            if scaled_progress is not None:
                scaled_progress.update(1.0)


def log_files(files: List[str]):
    max_files_to_list = 50
    d_n = len(files) - max_files_to_list
    logger.info(
        "List of extracted files: \n\t%s%s",
        "\n\t".join(files[:max_files_to_list]),
        ((f"\n\t and {d_n} more files " "- not listing them all.") if d_n > 0 else ""),
    )
