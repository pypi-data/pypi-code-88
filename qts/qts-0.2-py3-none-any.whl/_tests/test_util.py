import typing

import attr

import qts.util


@attr.mutable
class Execable:
    call_count: int = 0

    def exec(self) -> int:
        self.call_count += 1
        return 0

    exec_ = exec


def test_exec() -> None:
    execable = Execable()

    assert execable.call_count == 0

    qts.util.exec(execable=execable)

    assert execable.call_count == 1
