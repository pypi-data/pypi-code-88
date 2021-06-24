import re
from enum import Enum, auto
from typing import Optional, AbstractSet, Tuple, List

from dataclasses import dataclass, fields as dataclass_fields, field


@dataclass(frozen=True)
class Uid:
    """GPG User ID representation.

    The GPG user ID format can contain a user's name and/or email address in
    the following formats:
     - Alice (Alice's test PGP key) <alice@example.com>
     - Alice
     - alice@example.com
    """

    full_name: Optional[str]
    email: Optional[str]

    def __post_init__(self):
        if self.full_name is None and self.email is None:
            raise ValueError("Both 'full_name' and 'email' cannot be None.")

    def __repr__(self):
        if self.full_name is not None and self.email is not None:
            return f"{self.full_name} <{self.email}>"
        return self.full_name or self.email

    @staticmethod
    def from_str(s):
        if s is None or s[0] == "[" and s[-1] == "]":
            # Something like "[User ID not found]" (can be translated into other languages)
            return None
        if re.search(r" <\S+>", s) is not None:
            return Uid(*s.rstrip(">").split(" <"))
        if "@" in s:
            return Uid(full_name=None, email=s)
        return Uid(full_name=s, email=None)


class KeyType(Enum):
    """Representation of the GPG key type. Only two type of keys exist:
    public and secret (often also referred to as 'private')"""

    public = auto()
    secret = auto()


class TrustModel(Enum):
    pgp = "pgp"
    classic = "classic"
    tofu = "tofu"  # Trust on first use.
    tofu_pgp = "tofu+pgp"
    direct = "direct"
    always = "always"
    auto = "auto"


class Validity(Enum):
    unknown_new = "o"  # Unknown (this key is new to the system)
    invalid = "i"  # The key is invalid (e.g. missing self-signature)
    disabled = "d"  # The key has been disabled
    #               # (deprecated - use the 'D' in field 12 instead)
    revoked = "r"  # The key has been revoked
    expired = "e"  # The key has expired
    unknown = "-"  # Unknown validity (i.e. no value assigned)
    undefined = "q"  # Undefined validity.  '-' and 'q' may safely be
    #                # treated as the same value for most purposes
    not_valid = "n"  # The key is not valid
    marginal_valid = "m"  # The key is marginally valid.
    fully_valid = "f"  # The key is fully valid
    ultimately_valid = "u"  # The key is ultimately valid. This often means
    #                       # that the secret key is available, but any key
    #                       # may be marked as ultimately valid.
    well_known_private_part = "w"  # The key has a well known private part.
    special_validity = "s"  # The key has special validity.  This means
    #                       # that it might be self-signed and
    #                       # expected to be used in the STEED system.


class SignatureValidity(Enum):
    good = "!"
    bad = "-"
    no_public_key = "?"
    error = "%"


class CompressAlgo(Enum):
    ZLIB = "zlib"
    ZIP = "zip"
    BZIP2 = "bzip2"
    NONE = "uncompressed"


key_capabilities = {}


def key_capability(key: str):
    def decorator(cls):
        wrapped = dataclass(frozen=True)(cls)
        for variant in {key, key.upper()}:
            key_capabilities[variant] = wrapped(variant.isupper())
        return wrapped

    return decorator


@dataclass(frozen=True)
class KeyCapabilityBase:
    global_: bool


class KeyCapability:
    @key_capability("e")
    class Encrypt(KeyCapabilityBase):
        pass

    @key_capability("s")
    class Sign(KeyCapabilityBase):
        pass

    @key_capability("c")
    class Certify(KeyCapabilityBase):
        pass

    @key_capability("a")
    class Authentication(KeyCapabilityBase):
        pass

    @key_capability("?")
    class Unknown(KeyCapabilityBase):
        pass

    @key_capability("D")
    class Disabled(KeyCapabilityBase):
        pass


@dataclass(frozen=True)
class Signature:
    """Representation of a signature on a public key.

    When signature's hash algorithm is SHA-1 (and not SHA-256), the signature
    has no fingerprint.
    """

    issuer_uid: Optional[Uid]
    issuer_key_id: str
    issuer_fingerprint: Optional[str]
    signature_class: str
    validity: SignatureValidity
    creation_date: str
    expiration_date: Optional[str] = None


@dataclass(frozen=True)
class RevocationSignature(Signature):
    reason: Optional[str] = None
    comment: Optional[str] = None


@dataclass(frozen=True)
class SubKey:
    key_id: str
    key_type: KeyType
    fingerprint: str
    key_length: int
    pub_key_algorithm: int
    creation_date: str
    validity: Validity = Validity.unknown
    expiration_date: Optional[str] = None
    key_capabilities: AbstractSet[KeyCapabilityBase] = frozenset()
    signatures: Tuple[Signature, ...] = ()

    @property
    def valid_signatures(self) -> List[Signature]:
        """Return a list of signatures on a public key that are verified and
        non-revoked.
        """

        revoked_sigs = {
            s.issuer_fingerprint or s.issuer_key_id
            for s in self.signatures
            if isinstance(s, RevocationSignature)
            and s.validity == SignatureValidity.good
        }
        return [
            s
            for s in self.signatures
            if s.issuer_fingerprint not in revoked_sigs
            and s.issuer_key_id not in revoked_sigs
            and s.validity == SignatureValidity.good
        ]


@dataclass(frozen=True)
class Key(SubKey):
    uids: Tuple[Uid, ...] = field(default=(), metadata=dict(required=True))
    owner_trust: str = "-"
    sub_keys: Tuple[SubKey, ...] = ()
    origin: Optional[str] = None

    def __post_init__(self):
        """Raise error if there is any required field with no value."""
        missing_fields = [
            f.name
            for f in dataclass_fields(type(self))
            if f.metadata.get("required", False) and not getattr(self, f.name)
        ]
        if missing_fields:
            l = len(missing_fields)
            plural = "s" if l > 1 else ""
            fields = ", ".join(f"'{f}'" for f in missing_fields)
            raise TypeError(f"__init__ missing {l} required argument{plural}: {fields}")


@dataclass(frozen=True)
class KeyInfo:
    uid: Uid
    fingerprint: str
    key_algorithm: int
    key_length: int
    creation_date: str
    expiration_date: Optional[str]


def parse_key_capabilities(s: Optional[str]):
    if s is None:
        return frozenset()
    return frozenset(key_capabilities[c] for c in s)


@dataclass
class ColonRecordBase:
    """According to [gnupg.git]/doc/DETAILS"""

    validity: Optional[Validity] = None  # 2
    key_length: Optional[int] = None  # 3
    pub_key_algorithm: Optional[int] = None
    key_id: Optional[str] = None  # 5
    creation_date: Optional[str] = None
    expiration_date: Optional[str] = None
    cert_S_N_uid_hash_trust_signature_info: Optional[str] = None
    owner_trust: Optional[str] = None
    user_id: Optional[str] = None  # 10
    signature_class: Optional[str] = None
    key_capabilities: AbstractSet[KeyCapabilityBase] = field(
        default=frozenset(), metadata=dict(deserialize=parse_key_capabilities)
    )
    issuer: Optional[str] = None  # 13: Issuer certificate fingerprint or other info.
    flag: Optional[str] = None
    token_S_N: Optional[str] = None  # 15
    hash_algorithm: Optional[int] = None  # 16: Hash algorithm. 2 = SHA-1, 8 = SHA-256
    curve_name: Optional[str] = None
    compliance_flags: Optional[str] = None
    last_update: Optional[str] = None
    origin: Optional[str] = None  # 20
    comment: Optional[str] = None

    def into(self):
        return self
