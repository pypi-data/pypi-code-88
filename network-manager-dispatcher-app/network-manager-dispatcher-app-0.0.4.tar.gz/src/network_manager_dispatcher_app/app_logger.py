from abc import ABC, abstractclassmethod
from io import IOBase

class IAppLogger(ABC):
    @abstractclassmethod
    def log_state(self, state):
        pass

    @abstractclassmethod
    def log_info(self, data):
        pass

    @abstractclassmethod    
    def log_error(self, data):
        pass

    @abstractclassmethod
    def close(self):
        pass

class AppLogger(IAppLogger):
    def __init__(self, file: IOBase, start: str) -> None:
        self.file = file 
        self.logstart = start

    def log_state(self, state):
        print(f"{self.logstart} Connection state '{state}' dispatched.", file=self.file, flush=True)

    def log_info(self, data):
        print(data, file=self.file, flush=True)

    def log_error(self, data):
        print(f'Error: {data}', file=self.file, flush=True)

    def close(self):
        self.file.close()
