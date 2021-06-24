import io
import platform
import os
import re
import tempfile
import shutil
from typing import (
    Optional,
    List,
    Tuple,
    Iterator,
    Iterable,
    Union,
    Sequence,
    Any,
    Type,
    IO,
    Dict,
    ContextManager,
    Callable,
)
from urllib.parse import quote
import urllib.request

from dataclasses import dataclass, fields as dataclass_fields

from .parser import compile_grammar
from .deserialize import deserialize
from .cmd import (
    cmd_devnull,
    cmd_pipe,
    cmd_pipe_stdout,
    expect,
    GPGError,
    stderr_lookahead,
)
from .model import (
    Uid,
    KeyType,
    Key,
    SubKey,
    TrustModel,
    SignatureValidity,
    CompressAlgo,
    ColonRecordBase,
    Signature,
    RevocationSignature,
)

from .keyserver import post, build_host, download_key


def parse_data_class(T: type, args: Sequence[Any]):
    fields = (f.metadata.get("deserialize", f.type) for f in dataclass_fields(T))
    return T(*(deserialize(f_type)(arg) for f_type, arg in zip(fields, args)))


unimplemented_col_rec_ids = (
    "crt",  # X.509 certificate
    "crs",  # X.509 certificate and secret key available
    "uat",  # User attribute (same as user id except for field 10).
    "rvs",  # Revocation signature (standalone) [since 2.2.9]
    "pkd",  # Public key data [*]
    "grp",  # Keygrip
    "rvk",  # Revocation key
    "tfs",  # TOFU statistics [*]
    "tru",  # Trust database information [*]
    "spk",  # Signature subpacket [*]
    "cfg",  # Configuration data [*]
)

col_rec_types = {}


def col_rec_type(identifier):
    def decorator(cls):
        col_rec_types[identifier] = cls
        return cls

    return decorator


def extract_key_fields(rec):
    fields = (
        "validity",
        "key_length",
        "pub_key_algorithm",
        "key_id",
        "creation_date",
        "expiration_date",
        "owner_trust",
        "key_capabilities",
        "origin",
    )
    return {
        key: val
        for key, val in ((f, getattr(rec, f, None)) for f in fields)
        if val is not None
    }


@col_rec_type("sec")
class ColonRecordSec(ColonRecordBase):
    """Secret key"""

    def into(self):
        return Factory(key_type=KeyType.secret, **extract_key_fields(self))


@col_rec_type("pub")
class ColonRecordPub(ColonRecordBase):
    """Public key"""

    def into(self):
        return Factory(key_type=KeyType.public, **extract_key_fields(self))


@col_rec_type("sub")
class ColonRecordSub(ColonRecordBase):
    """Subkey (secondary key)"""

    def into(self):
        return SubKeyFactory(key_type=KeyType.public, **extract_key_fields(self))


@col_rec_type("ssb")
class ColonRecordSsb(ColonRecordBase):
    """Subkey (secondary key)"""

    def into(self):
        return SubKeyFactory(key_type=KeyType.secret, **extract_key_fields(self))


@col_rec_type("uid")
class ColonRecordUid(ColonRecordBase):
    """User id"""

    def into(self):
        return Uid.from_str(self.user_id)


@col_rec_type("fpr")
class ColonRecordFpr(ColonRecordBase):
    """Fingerprint"""

    def into(self):
        if self.user_id is None:
            raise ValueError("Field 'user_id' missing in record")
        return self.user_id


@col_rec_type("sig")
@dataclass
class ColonRecordSig(ColonRecordBase):
    """Signature"""

    # Here we ignore the change of type in the field. This type is
    # for parsing only.
    validity: Optional[SignatureValidity]  # type: ignore

    def into_dict(self):
        uid = Uid.from_str(self.user_id)
        return dict(
            issuer_uid=uid,
            issuer_key_id=self.key_id,
            issuer_fingerprint=self.issuer,
            creation_date=self.creation_date,
            expiration_date=self.expiration_date,
            signature_class=self.signature_class,
            validity=self.validity,
        )

    def into(self):
        return Signature(**self.into_dict())


@col_rec_type("rev")
@dataclass
class ColonRecordRev(ColonRecordSig):
    """Revocation Signature"""

    def into(self):
        sig = self.into_dict()
        sig_class = sig.pop("signature_class")
        try:
            sig_class, revocation_reason = sig_class.split(",")
        except ValueError:
            revocation_reason = None
        return RevocationSignature(
            comment=self.comment,
            signature_class=sig_class,
            reason=revocation_reason,
            **sig,
        )


def lex_colon(payload: IO[bytes]) -> Iterator:
    """Tokenizes the output of a call to the gpg command to list keys (payload)
    one line at a time. Works for both commands to list public or secret keys.
    Example of payload:
        tru::1:1574434353:0:3:1:5
        pub:u:4096:1:12477DE52DAD86CC:1574434343:::u:::escaESCA:
        fpr:::::::::621A2A449F234A0E9246CF8212477DE52DAD86CC:
        uid:u::::1574434343::9F08B014A8964D2FCA0B04A7B11CF5FDFD12DF13::bob <bob@example.com>:
        sig:!::1:34168F55EE0DCAD7:1574434343::::Alice <alice@redqueen.org>:13x::AAA7E2A101EBFA70943DC88534168F55EE0DCAD7:::8:
        sub:u:4096:1:CFAF4D7B40DAF86B:1574434343::::::esa:
        fpr:::::::::39D91E3C8C9C2C0677F1A74BCFAF4D7B40DAF86B:

    :param payload: stream of bytes corresponding to the output of the gpg
        command.
    :return: generator of "token" that are either a "Factory" object or string.
    :raises ValueError:
    """
    # Loop through the output of the GPG command one line at a time.
    for rec in payload:
        rec = rec.rstrip(b"\n")
        if not rec:
            continue

        # Split line by ':' separator. The first element of the line is the
        # "type of record" (e.g. pub = public key, sub = sub key)
        record_type, *args = map(
            lambda s: s if s else None, rec.decode("utf-8", "replace").split(":")
        )
        args = args[: len(dataclass_fields(ColonRecordBase))]
        if record_type in unimplemented_col_rec_ids:
            continue
        try:
            token = parse_data_class(col_rec_types[record_type], args).into()
        except BaseException as e:
            raise ValueError(
                f"Error while parsing row of type {record_type}"
                f"\n{format(e)}"
                f"\ncolumns: {args}"
            ) from e
        if token is not None:
            yield token


class Factory:
    type_: Type[SubKey] = Key

    def __init__(self, origin: Optional[str] = None, **kwargs):
        self.kwargs = kwargs
        if origin:
            origin = origin.replace("\\x3a", ":").lstrip("0123456789 ")
            self.kwargs["origin"] = origin or None

    def append(self, key, val):
        self.kwargs[key] = self.kwargs.get(key, ()) + (val,)
        return self

    def append_subkey(self, val):
        if self.kwargs["key_type"] != val.key_type:
            raise ValueError(f"Wrong sub key type '{val.key_type}'")
        return self.append("sub_keys", val)

    def set(self, key, val):
        if key in self.kwargs:
            raise ValueError(f"Key '{key}' already set")
        self.kwargs[key] = val
        return self

    def build(self):
        try:
            return self.type_(**self.kwargs)
        except (TypeError, ValueError) as e:
            raise type(e)(e.args[0].replace("__init__", self.type_.__name__))


class SubKeyFactory(Factory):
    type_ = SubKey


# Factory, type : rule how to transform subsequences of tokens
# into reduced token sequences. For example, in:
#  -> (Factory, str): lambda fac, fpr: [fac.set("fingerprint", fpr)]
# the rule (lambda function) defines how to add the string (fingerprint) to
# the Factory (i.e. the main key object).
key_parser = compile_grammar(
    {
        ((Factory, SubKeyFactory), Uid): lambda fac, uid: [fac.append("uids", uid)],
        ((Factory, SubKeyFactory), str): lambda fac, fpr: [fac.set("fingerprint", fpr)],
        ((Factory, SubKeyFactory), (Signature, RevocationSignature)): lambda fac, sig: [
            fac.append("signatures", sig)
        ],
        (Factory, SubKey): lambda fac, sub: [fac.append_subkey(sub)],
        ((Factory, SubKeyFactory), list): lambda fac, lst: [fac.build(), lst],
        (SubKeyFactory, SubKey): lambda fac, key: [fac.build(), key],
        (Key, list): lambda key, lst: [[key] + lst],
    },
    list,
)


def parse_keys(payload: IO[bytes]):
    return key_parser(list(lex_colon(payload)) + [[]])


GPG_DEFAULT_DIR_BY_OS: Dict[str, Tuple[str, ...]] = {
    "Linux": (".gnupg",),
    "Darwin": (".gnupg",),
    "Windows": ("AppData", "Roaming", "gnupg"),
}


def get_default_gnupg_home_dir() -> str:
    """Default path of the directory where GnuPG stores the user's keyrings.
    The location of this directory is platform dependent.
    """
    return os.path.join(
        os.path.expanduser("~"), *GPG_DEFAULT_DIR_BY_OS[platform.system()]
    )


def get_gnupg_binary(gnupg_binary: Optional[str] = None) -> str:
    """Test whether the provided gnupg_binary (name of the GnuPG binary or
    its absolute path) is found in the user's PATH.
    If no input is provided for gnupg_binary, the function defaults to
    testing whether there are binaries named 'gpg' or 'gpg2' in the user's
    PATH.
    """
    binaries_to_test = (gnupg_binary,) if gnupg_binary else ("gpg", "gpg2")
    for bin_name in binaries_to_test:
        try:
            cmd_devnull((bin_name, "--version"))
            return bin_name
        except FileNotFoundError:
            continue

    raise FileNotFoundError(
        f"GnuPG executable [{', '.join(binaries_to_test)}] not found. "
        "Please make sure that the GnuPG binary is found in your PATH."
    )


class GPGStore:
    """Main class providing the functionality of gpg-lite.

    The main class of the library is the representation of a GnuPG 'home'
    directory that contains the user's keyrings.

    :param gnupg_home_dir: 'home' directory of GnuPG, where keyrings are stored
        on the user's machine. On Linux systems, this is typically ~/.gnupg.
        If set to None (default value), the default GnuPG directory is used.
    :param gnupg_binary: name or full path of the GnuPG binary to use. If not
        specified, the user's PATH is searched for a binary named either
        'gpg' or 'gpg2', and an error is raised if none of these in found in
        the PATH.
    """

    def __init__(
        self, gnupg_home_dir: Optional[str] = None, gnupg_binary: Optional[str] = None
    ):
        self._gnupg_home_dir = gnupg_home_dir
        self._gpg_bin = get_gnupg_binary(gnupg_binary)
        self._version = self.version()
        self._pw_args_t: Tuple[str, ...] = ("--passphrase-fd", "0")
        if self._version >= (2, 2, 0):
            self._pw_args_t = ("--pinentry-mode", "loopback") + self._pw_args_t
        else:
            # Specific to older versions of gpg: the --batch option must be
            # added in order for the --passphrase-fd option to be used.
            self._pw_args_t = ("--batch",) + self._pw_args_t

    def _pw_args(self, pw):
        return self._pw_args_t if pw is not None else ()

    @property
    def gnupg_binary(self):
        return shutil.which(self._gpg_bin)

    @property
    def gnupg_home_dir(self):
        return self._gnupg_home_dir or get_default_gnupg_home_dir()

    @property
    def _base_args(self):
        args = (self._gpg_bin,)
        if self._gnupg_home_dir is not None:
            args += ("--homedir", self._gnupg_home_dir)
        return args

    def default_key(self) -> Optional[str]:
        config_file = os.path.join(self.gnupg_home_dir, "gpg.conf")
        try:
            with open(config_file) as f_cfg:
                default_key = next(
                    line for line in f_cfg if line.startswith("default-key ")
                )
            return default_key.split(" ")[1].rstrip("\r\n")
        except (FileNotFoundError, StopIteration):
            try:
                return self.list_sec_keys()[0].fingerprint
            except IndexError:
                return None

    def list_pub_keys(
        self, search_terms: Optional[Iterable[str]] = None, sigs: bool = False
    ) -> List[Key]:
        """Retrieve public keys from the local keyring that are matching
        one of the search_terms in their key fingerprint, key ID or user ID.

        If no search_terms is passed, all keys are returned.
        Keys are not returned in any particular order.
        If sigs is True, matching keys are returned with their signatures.
        """

        return self._list_keys(
            option="--list-public-keys", search_terms=search_terms, sigs=sigs
        )

    def list_sec_keys(self, search_terms: Optional[Iterable[str]] = None) -> List[Key]:
        """Retrieve secret/private keys from the local keyring that are matching
        one of the search_terms in their key fingerprint, key ID or user ID.

        If no search_terms is passed, all keys are returned.
        Keys are not returned in any particular order.
        If sigs is True, matching keys are returned with their signatures.
        """

        return self._list_keys(option="--list-secret-keys", search_terms=search_terms)

    def _list_keys(
        self,
        option: str,
        search_terms: Optional[Iterable[str]] = None,
        sigs: bool = False,
    ) -> List[Key]:
        """Returns keys from the local keyring that match one of the
        search_terms. The 'options' argument allows to search for either public
        or secret/private keys.
        Important: keys are not returned in the same order as the search_terms.

        :param option: argument to pass to gpg, e.g. "--list-public-keys" to
            list the public keys in the user's keyring.
        :param search_terms: key name, key ID or fingerprint to search for. If
            an empty list is passed, no key is returned. If keys is None, all
            keys in the keyring are returned.
        :param sigs: if True, show signatures appended on keys.
        :return: list of keys matching the search criteria.
        :raise GPGError:
        """
        if search_terms is None:
            search_terms = ()
        else:
            search_terms = tuple(search_terms)
            if not search_terms:
                return []
        # Add arguments that are always required for gpg to produce the
        # correct output. Note that for gpg versions < 2.1, the
        # --with-fingerprint option is required to be passed twice. If passed
        # only once the fingerprint of the subkeys are not printed.
        args: Tuple[str, ...] = (
            option,
            "--fingerprint",
            "--fingerprint",
            "--with-colons",
        )
        if sigs:
            args += ("--with-sig-check",)
        args += search_terms
        try:
            with cmd_pipe(self._base_args + args) as proc:
                return parse_keys(proc.stdout)
        except GPGError as e:
            if "error reading key" in str(e).lower():
                return []
            raise

    def encrypt(
        self,
        source: Optional[Union[bytes, io.FileIO, Callable]],
        recipients: List[str],
        output: Optional[Union[io.FileIO, Callable]],
        sign: Optional[str] = None,
        passphrase: Optional[str] = None,
        trust_model: TrustModel = TrustModel.pgp,
        compress_algo: Optional[CompressAlgo] = None,
        compress_level: Optional[int] = None,
    ):
        """Encrypt data with the public PGP key of recipients.

        Both source and output can be file like objects or callables
        processing streams.

        :param source: data to encrypt. Read directly from a file object
            or write the data to the stream in a callable.
        :param recipients: gpg key fingerprints.
        :param output: encrypted data. Write directly to a file object
            or pass the stream to a callable.
        :param sign: fingerprint of private key with which the data should be
            signed. If None, the encrypted file is not signed.
        :param passphrase: passphrase of the private key to be used to sign
            the data. Only needed if a value was passed to the sign argument.
            If the private key has no passphrase (bad practice), an empty
            string should be passed as passphrase.
        :param trust_model: trust model to be followed by gpg.
        :param compress_algo: algorithm to use for data compression.
            If not provided the default algorithm defined by gpg is used.
        :param compress_level: data compression algorithm level.
            An integer value between 0 (no compression) and
            9 (maximum compression). If not provided the default level
            defined by gpg is used.
        :raises ValueError:
        """

        # Generate list of recipients for the encrypted file.
        args: Tuple[str, ...] = sum((("--recipient", rcp) for rcp in recipients), ())
        args += ("--no-tty", "--trust-model", trust_model.name, "--encrypt")
        if sign is not None:
            if passphrase is None:
                raise ValueError("Passphrase for private key is missing")
            args += ("--sign", "--local-user", sign)

        if compress_algo is not None:
            args += ("--compress-algo", compress_algo.value)

        if compress_level is not None:
            if (
                not isinstance(compress_level, int)
                or compress_level < 0
                or compress_level > 9
            ):
                raise ValueError(
                    "Invalid compression level. The value must "
                    "be an integer between 0 and 9."
                )
            args += ("--compress-level", str(compress_level))

        with cmd_pipe(
            self._base_args + self._pw_args(passphrase) + args,
            src=source,
            stdout=output,
            passphrase=passphrase,
        ):
            pass

    def decrypt(
        self,
        source: Union[io.FileIO, Callable],
        output: Union[io.FileIO, Callable],
        passphrase: Optional[str] = None,
        trust_model: TrustModel = TrustModel.pgp,
    ) -> List[str]:
        """Decrypt data and, if present, retrieve the signature appended to
        the encrypted file.

        :param source: data to decrypt. Read directly from a file object
            or write the data to the stream in a callable.
        :param output: decrypted data. Write directly to a file object
            or pass the stream to a callable.
        :param passphrase: passphrase of the private key to be used to decrypt
            the data.
        :param trust_model: trust model to be followed by gpg.
        :return: fingerprint or keyid of the signee's key.
        """

        # Note: the '--keyid-format', 'long' argument is only needed for
        # backwards compatibility with gpg versions < 2.1.0
        args = (
            "--batch",
            "--no-tty",
            "--status-fd",
            "2",
            "--trust-model",
            trust_model.name,
            "--decrypt",
        )
        maybe_stdout = {}
        if output is not None:
            maybe_stdout["stdout"] = output
        with cmd_pipe(
            self._base_args + self._pw_args(passphrase) + args,  # type: ignore
            **maybe_stdout,
            src=source,
            passphrase=passphrase,
        ) as proc:
            while True:
                if proc.poll() is not None:
                    break
            gpg_out = stderr_lookahead(proc)
            return capture_fpr(gpg_out)

    def gen_key(
        self,
        full_name: str,
        email: str,
        passphrase: str,
        key_length: int = 4096,
        key_type: str = "RSA",
    ) -> str:
        """Create a new public/private PGP key pair.

        :param full_name: user name to be used in the key user ID.
        :param email: email to be used in the key user ID.
        :param passphrase: passphrase (password) that will be requested when
            using the private key.
        :param key_length: bit-length of the key to be generated. Generally
            speaking, longer keys are stronger (more difficult to break). For
            "RSA" keys the recommended length is currently 2048 or 4096. Keys
            shorter than 2048 bits should not be used any longer.
        :param key_type: "RSA" (default) or "DSA". It is strongly recommended
            to use "RSA", as these key types are more secure.
        :return: fingerprint of the newly generated key.
        """
        args = ("--batch", "--status-fd", "1", "--gen-key")
        with cmd_pipe(
            self._base_args + args,
            src=f"""
%echo Generating a basic OpenPGP key
Key-Type: {key_type}
Key-Length: {key_length}
Subkey-Type: {key_type}
Subkey-Length: {key_length}
Name-Real: {full_name}
Name-Email: {email}
Expire-Date: 0
Passphrase: {passphrase}
%commit
%echo done
""".encode(),
        ) as proc:
            l = next(
                line for line in proc.stdout if line.startswith(b"[GNUPG:] KEY_CREATED")
            )
            return l.rstrip(b"\r\n").split(b" ")[-1].decode("utf-8", "replace")

    def send_keys(
        self, *fingerprints: str, keyserver: str, url_opener=urllib.request.urlopen
    ):
        """Upload keys from the user's local keyring to a keyserver.

        Following https://tools.ietf.org/html/draft-shaw-openpgp-hkp-00#page-6,
        Section 4
        """
        data = self.export(*fingerprints)
        post(
            build_host(keyserver) + "/pks/add",
            b"keytext=" + quote(data).encode(),
            url_opener=url_opener,
        )

    def recv_keys(self, *fingerprints: str, keyserver: str, **kwargs):
        """Download keys from a keyserver to the user's local keyring."""
        for fingerprint in fingerprints:
            with download_key(
                keyserver=keyserver, fingerprint=fingerprint, **kwargs
            ) as key:
                self.import_file(key.read())

    def delete_pub_keys(self, *fingerprints: str) -> None:
        """Delete one or more public keys with the specified fingerprints from
        the local keyring.

        Note that public keys can only be deleted if there is not matching
        secret key.
        """
        self._delete_keys(*fingerprints, public_key=True)

    def delete_sec_keys(self, *fingerprints: str) -> None:
        """Delete one or more secrte/private keys with the specified
        fingerprints from the local keyring.
        WARNING: deleted secret keys cannot be recovered or re-generated. Tread
        carefully.
        """
        self._delete_keys(*fingerprints, public_key=False)

    def _delete_keys(self, *fingerprints: str, public_key: bool = True) -> None:
        cmd_devnull(
            self._base_args
            + (
                "--batch",
                "--yes",
                "--delete-keys" if public_key else "--delete-secret-keys",
            )
            + fingerprints
        )

    def import_file(
        self, source: Union[bytes, IO[bytes]], *, passphrase: Optional[str] = None
    ):
        cmd_devnull(
            self._base_args + self._pw_args(passphrase) + ("--import", "--batch", "-"),
            src=source,
            passphrase=passphrase,
        )

    def export(self, *fingerprints: str, armor: bool = True) -> bytes:
        cmd = (
            self._base_args
            + ("--export",)
            + (("--armor",) if armor else ())
            + fingerprints
        )
        with cmd_pipe_stdout(cmd) as stream:
            return stream.read()

    def version(self):
        with cmd_pipe(self._base_args + ("--version",)) as proc:
            return tuple(
                map(
                    int,
                    proc.stdout.readline().rstrip(b"\n").split(b" ")[-1].split(b"."),
                )
            )

    def gen_revoke(self, fingerprint: str, passphrase) -> bytes:
        """Generate a revocation certificate for a PGP key with the specified
        fingerprint.
        """
        args = (
            self._base_args
            + self._pw_args(passphrase)
            + (
                "--no-tty",
                "--status-fd",
                "2",
                "--command-fd",
                "0",
                "--gen-revoke",
                fingerprint,
            )
        )
        with expect(args) as proc:
            try:
                proc.put(passphrase.encode() + b"\n")
                proc.expect(b"[GNUPG:] GET_BOOL gen_revoke.okay\n")
                proc.put(b"y\n")
                proc.expect(b"[GNUPG:] GET_LINE ask_revocation_reason.code\n")
                proc.put(b"0\n")
                proc.expect(b"[GNUPG:] GET_LINE ask_revocation_reason.text\n")
                proc.put(b"\n")
                proc.expect(b"[GNUPG:] GET_BOOL ask_revocation_reason.okay\n")
                proc.put(b"y\n")
            except ValueError as e:
                raise GPGError("Failed to generate a revocation certificate") from e
            return proc.stdout.read()

    def revoke_key(
        self,
        fingerprint: str,
        revocation_certif: Optional[Union[bytes, IO[bytes]]] = None,
        passphrase: Optional[str] = None,
        keyserver: Optional[str] = None,
    ) -> None:
        """Revoke a PGP key, optionally pushing it to a keyserver.

        Key revocation can be done by using a pre-existing revocation
        certificate (best practice is to generate such a certificate when a
        new key is generated, so it can be revoked if the password or secret
        key is lost).
        Alternatively, a key can also be revoked by passing the password of the
        key to revoke. Note that this only works if the matching secret key is
        present in the user's keyring.

        :param fingerprint: fingerprint of the key to revoke.
        :param revocation_certif: revocation certificate associated to the key.
        :param passphrase: password associated to the key to revoke. The
            password is only needed if no value is passed for revocation_certif.
        :param keyserver: URL of keyserver. This argument is optional. If
            provided, then the revoked key is pushed to the specified keyserver.
        """
        if not revocation_certif:
            revocation_certif = self.gen_revoke(fingerprint, passphrase)
        self.import_file(revocation_certif)
        if keyserver is not None:
            self.send_keys(fingerprint, keyserver=keyserver)

    def detach_sig(
        self,
        src: Union[bytes, IO[bytes]],
        passphrase: str,
        signee: Optional[str] = None,
    ) -> ContextManager:
        """Generate a detached signature for a given input.

        :param src: binary data for which a signature should be generated.
        :param passphrase: passphrase of the private key that is being used to
            sign the key.
        :param signee: fingerprint, key ID or user ID of the PGP key to be used
            to sign the data. If None, the default PGP key in the user's local
            keyring is used.
        :return: a context manager for a buffered reader.
        """
        return cmd_pipe_stdout(
            self._base_args
            + self._pw_args(passphrase)
            + (("--local-user", signee) if signee is not None else ())
            + ("--detach-sig", "-"),
            src=src,
            passphrase=passphrase,
        )

    def verify_detached_sig(
        self, src: Optional[Union[bytes, io.FileIO]], sig: bytes
    ) -> str:
        """Verify and retrieve the PGP signature made to a file in detached
        signature mode - i.e. the signed file and the signature are in separate
        files.

        :param src: file that was signed.
        :param sig: detached signature file.
        :return: fingerprint or key ID of the signee's key.
        :raises GPGError:
        """
        with tempfile.NamedTemporaryFile(delete=False) as f:
            try:
                f.write(sig)
                f.close()
                # Note: the '--keyid-format', 'long' argument is only needed for
                # backwards compatibility with gpg versions < 2.1.0
                with cmd_pipe(
                    self._base_args + ("--status-fd", "2", "--verify", f.name, "-"),
                    src=src,
                ) as proc:
                    gpg_out = stderr_lookahead(proc)
                    fingerprints = capture_fpr(gpg_out)

                    try:
                        (fingerprint,) = fingerprints
                    except ValueError as e:
                        raise GPGError(
                            f"{'More than one' if fingerprints else 'No'} "
                            "fingerprint found in input data:\n"
                            + gpg_out.decode("utf-8", "replace")
                        ) from e
                    return fingerprint
            finally:
                os.remove(f.name)


def capture_fpr(b: bytes) -> List[str]:
    """Extract fingerprint from a standard output of gpg that looks like:
    [GNUPG:] NEWSIG
    gpg: Signature made Tue 10 Mar 2020 11:29:27 CET
    gpg:                using RSA key 3B3EB1983FAA63C1B05E072D066E042415D8FD9C
    [GNUPG:] KEY_CONSIDERED 3B3EB1983FAA63C1B05E072D066E042415D8FD9C 0
    [GNUPG:] SIG_ID PaAuiNMUyUDRMsctXpV+7rX+0CI 2020-03-10 1583836167
    [GNUPG:] KEY_CONSIDERED 3B3EB1983FAA63C1B05E072D066E042415D8FD9C 0
    [GNUPG:] GOODSIG 066E042415D8FD9C Chuck Norris <chucknorris@roundhouse.gov>
    gpg: Good signature from "Chuck Norris <chucknorris@roundhouse.gov>" [unknown]
    [GNUPG:] VALIDSIG 3B3EB1983FAA63C1B05E072D066E042415D8FD9C 2020-03-10 1583836167

    :param b: gpg stdout in binary form.
    :return: either a 40-char long fingerprint.
    """
    return [
        m.group(1).decode("utf-8", "replace")
        for m in re.finditer(rb"\[GNUPG:\] VALIDSIG ([0-9A-F]{40})", b)
    ]
