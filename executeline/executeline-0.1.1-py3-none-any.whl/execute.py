###########################################
__author__ = "ToorajJahangiri"
__email__ = "Toorajjahangiri@gmail.com"
###########################################

# IMPORTS
from typing import Callable, Union, Generator, Iterable, Iterator

class Signal:
    """[Simple Signal Class]
    """

    def __init__(self) -> None:
        """[Signal Class]
        """
        self.__target = None

    def connect(self, target: Callable) -> None:
        """[Connected to Callable Object]

        Args:
            target (Callable): [Connected To Target]
        """
        if isinstance(target, Callable):
            self.__target = target

    def emit(self, *args, **kwargs) -> object:
        """[Emit Signal]

        Returns:
            object: [exec -> target(*args, **kwargs)]
        """
        if self.__target is not None:
            return self.__target(*args, **kwargs)

class ExeLine:
    """[Call 'Callable' Type Object in Line One by One]
    [Method 'run']
        Emitted Signal:
            [tuple]: (Line_index, Name_id, Object.__name__, Return Value)
            Connect 'Return_Connect' To your Manager
    [iter]
        Yields:
            [tuple]: (Line_index, Name_id, Object.__name__, Return Value)
    """
    __RUNNING: bool = False

    __RETSIG: Signal = Signal()
    Return_Connect: Signal.connect = __RETSIG.connect

    def __init__(self, run: bool = True) -> None:
        """[Initialize]

        Args:
            run (bool, optional): [Run as soon as 'data' is entered]. Defaults to True.
        """
        self.__run = run
        self.__pocket: list = []
        self.to_line: Callable = self.append_pocket

    def append_pocket(self, name_id: Union[str, bytes], func: Callable, arg: tuple = (), kwarg: dict = {}) -> None:
        """[Append Callable Object To Execute Pocket]
            if Run is True run after appending

        Args:
            name_id (Union[str, bytes]): [Name or Id]
            func (Callable): [Prog For Execute]
            arg (tuple, optional): [Prog Args]. Defaults to ().
            kwarg (dict, optional): [Prog Kwargs]. Defaults to {}.
        """
        self.__pocket.append((name_id, func, arg, kwarg))
        if not self.__RUNNING and self.__run:
            self.run()

    def line(self) -> list[tuple[int, Union[str, bytes]]]:
        """[Pocket Line View]

        Returns:
            list[tuple[int, Union[str, bytes]]]: [Line Index, Name Id]
            if 'pocket' is empty return empty list '[]'
        """
        if len(self.__pocket) > 0:
            return [(idx, name[0]) for idx, name in enumerate(self.__pocket)]
        return []

    def __in_line(self) -> Generator:
        """[Generator Yield One By One For Execute Prog]

        Yields:
            Generator [Tuple]: (Pocket_Index, (name_id, func, args, kwargs))
        """
        for idx, ex in enumerate(self.__pocket):
            yield idx, ex
        self.__pocket.clear()

    def __iter__(self) -> Iterator:
        """[Iterator Execute]

        Yields:
            Iterator [Tuple]: (Line_index, Name_id, Object.__name__, Return Value)
        """
        self.__RUNNING = True
        ex_line: Iterable = self.__in_line()
        for idx, func in ex_line:
            name, ex, arg, kwa = func
            args = arg if len(arg) > 0 else None
            kwargs = kwa if len(kwa) > 0 else None
            
            if args is None and kwargs is None:
                yield (idx, name, type(ex).__name__, ex())
                continue
            
            elif args is not None and kwargs is None:
                yield (idx, name, type(ex).__name__, ex(*args))
                continue
            
            elif kwargs is not None and args is None:
                yield (idx, name, type(ex).__name__, ex(**kwargs))
                continue
            
            elif args is not None and kwargs is not None:
                yield (idx, name, type(ex).__name__, ex(*args, **kwargs))
                continue
        
        self.__RUNNING = False
        self.__iter__()

    def run(self) -> None:
        """[Run Executer]
        This Method Return None But Emitted Signal Return
        Connect  Return Signal to Your Manager With Return_Connect
        """
        for rt in self.__iter__():
            self.__RETSIG.emit(*rt)
        if len(self.__pocket) > 0:
            self.run()

