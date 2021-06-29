from cloudrail.knowledge.context.azure.webapp.constants import FtpsState


class SiteConfig:
    """
        Attributes:
            http2_enabled: Indication if http2 protocol should be enabled or not.
            minimum_tls_version: The minimum supported TLS version for the function app.
            ftps_state: State of FTP / FTPS service for the function app.
    """
    def __init__(self, ftps_state: FtpsState, http2_enabled: bool, minimum_tls_version: str) -> None:
        super().__init__()
        self.ftps_state: FtpsState = ftps_state
        self.http2_enabled: bool = http2_enabled
        self.minimum_tls_version: str = minimum_tls_version
