@dataclass
class Instance:
    """Tycho instance attributes."""

    name: str
    docs: str
    aid: str
    sid: str
    fqsid: str
    workspace_name: str
    creation_time: str
    cpus: float
    gpus: int
    memory: float
    host: InitVar[str]
    username: InitVar[str]
    url: str = field(init=False)
    status: str = field(init=False)
    protocol: InitVar[str] = os.environ.get("ACCOUNT_DEFAULT_HTTP_PROTOCOL", "http")
