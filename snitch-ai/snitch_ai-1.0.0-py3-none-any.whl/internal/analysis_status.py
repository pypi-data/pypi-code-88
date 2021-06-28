from enum import Enum

class AnalysisState(Enum):
    UNKNOWN = 0
    RUNNING = 1
    COMPLETED = 2
    ERROR = 3


class AnalysisStatus:
    def __init__(self, state: AnalysisState, error: str):
        self.state = state
        self.error = error


    def __str__(self):
        value = f"State: {self.state}"
        if self.state == AnalysisState.ERROR:
            value += f": {self.error}"

        return value