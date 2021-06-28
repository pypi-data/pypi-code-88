from pathlib import Path

import alteia

from alteia_cli import config


def alteia_sdk(credential_path: Path = config.DEFAULT_CREDENTIAL_PATH, *,
               profile: str = config.DEFAULT_PROFILE) -> alteia.SDK:
    credentials = config.get_credentials(
        credential_path=credential_path,
        profile=profile
    )
    if not credentials:
        credentials = config.setup(credential_path=credential_path)

    return alteia.SDK(
            user=credentials.username,
            password=credentials.password,
            url=credentials.url,
            proxy_url=credentials.proxy_url,
        )
