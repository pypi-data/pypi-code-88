from copy import deepcopy
from json import dumps
from typing import TYPE_CHECKING, Any, AnyStr, Dict, Iterable, Optional

if TYPE_CHECKING:
    from ruleau.adapter import ApiAdapter
    from ruleau.process import Process
    from ruleau.rule import Rule


class DependentResults:
    def __init__(
        self,
        case_id: AnyStr,
        dependents: Iterable["Rule"],
        payload: Dict[AnyStr, Any],
        process: "Process",
        api_adapter: Optional["ApiAdapter"] = None,
        lazy: bool = False,
    ):
        self.case_id: AnyStr = case_id
        self.dependents = {dep.__name__: dep for dep in dependents}
        self.payload: Dict[AnyStr, Any] = deepcopy(payload)
        self.api_adapter = api_adapter
        self.results: Dict[AnyStr, Any] = {}
        self.process = process

        if not lazy:
            for depend in dependents:
                self.run(depend.__name__)

    def run(self, name):
        """
        Run and store the result of a rule dependency
        :param name:
        :return:
        """

        if name not in self.dependents:
            raise AttributeError(
                f"Result for rule '{name}' not available, as it was not "
                f"declared as a dependency. "
                f"depends_on={dumps(list(self.dependents.keys()))}"
            )
        # If the result of rule execution is not set, run & cache it
        if name not in self.results:
            self.results[name] = self.dependents[name].execute(
                self.case_id,
                self.payload,
                self.process,
                self.api_adapter,
            )
        # Return the rule execution result
        return self.results[name]

    def __getattr__(self, name):
        # Get the attribute otherwise, run the dependency
        return getattr(super(), name, self.run(name))

    def __iter__(self):
        # Iterate through the dependencies
        for dep in self.dependents:
            yield getattr(self, dep)
