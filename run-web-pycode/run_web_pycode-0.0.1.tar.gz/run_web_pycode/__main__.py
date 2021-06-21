#!/usr/bin/python3
# encoding: utf-8
""" run_web_pycode 's entry_points"""
import fire

from run_web_pycode.core import read_proxy, run_remote_script, set_proxy


def entry_point() -> None:  # pragma: no cover
    """
    默认函数 触发fire包
    https://github.com/google/python-fire
    """
    fire.core.Display = lambda lines, out: print(*lines, file=out)
    fire.Fire(
        {
            "version": version,
            "run": run_remote_script,
            "set_proxy": set_proxy,
            "read_proxy": read_proxy,
        }
    )


def ipython() -> None:  # pragma: no cover
    """打开ipython命令"""
    from IPython import embed

    embed()


def version() -> str:
    """show version"""
    import run_web_pycode

    return run_web_pycode.__version__


if __name__ == "__main__":
    entry_point()
