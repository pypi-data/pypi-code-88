import typing

class AbstractResult:
    def shots(self) -> typing.Counter[str]:
        """Get shots."""
        raise NotImplementedError()
