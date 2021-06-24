from typing import Any
from typing import Dict
from typing import Iterable
from typing import Tuple

from dict_tools import data

__func_alias__ = {"ctx_": "ctx"}


async def run(
    hub,
    path: str,
    args: Tuple[Any],
    kwargs: Dict[str, Any],
    acct_file: str = None,
    acct_key: str = None,
    acct_profile: str = "default",
):
    args = [a for a in args]

    if not path.startswith("exec."):
        path = f"exec.{path}"

    func = getattr(hub, path)
    params = func.signature.parameters

    if "ctx" in params:
        ctx = await hub.idem.ex.ctx(path, acct_file, acct_key, acct_profile)
        args.insert(0, ctx)

    ret = func(*args, **kwargs)
    return await hub.pop.loop.unwrap(ret)


async def ctx_(
    hub,
    path: str,
    acct_file: str = None,
    acct_key: str = None,
    acct_profile: str = "default",
):
    """
    :param hub:
    :param path:
    :param acct_file:
    :param acct_key:
    :param acct_profile:
    :return:
    """
    ctx = data.NamespaceDict()

    first = path[path.index(".") + 1 :]
    sname = first[: first.index(".")]
    acct_paths = (f"exec.{sname}.ACCT", f"states.{sname}.ACCT")

    if acct_file and acct_key:
        await hub.acct.init.unlock(acct_file, acct_key)

    subs = set()
    for name in acct_paths:
        if hasattr(hub, name):
            sub = getattr(hub, name)
            if isinstance(sub, Iterable) and sub:
                subs.update(set(sub))

    ctx.acct = await hub.acct.init.gather(subs, acct_profile)

    return ctx


async def single(hub, path: str, *args, **kwargs):
    acct_file = hub.OPT.acct.acct_file
    acct_key = hub.OPT.acct.acct_key
    acct_profile = hub.OPT.acct.get("acct_profile", hub.acct.DEFAULT)

    ret = await hub.idem.ex.run(
        path,
        args=args,
        kwargs=kwargs,
        acct_file=acct_file,
        acct_key=acct_key,
        acct_profile=acct_profile,
    )
    return ret
