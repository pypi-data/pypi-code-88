class GuardedException(Exception):
    def __init__(self, line: str, message: str) -> None:
        self.line = line
        self.message = message

    def __str__(self) -> str:
        return f'Error on line {self.line}: {self.message}'