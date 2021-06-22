# Builtin modules
from __future__ import annotations
import os, traceback, unittest, signal as _signal
from threading import Timer, Event
from time import monotonic, sleep
from typing import Callable, Dict, Any, Iterator, Iterable, Optional, Union
# Local modules
# Program
class KillSignal(Exception): pass

class SignalIterator(Iterator):
	__slots__ = ("event", "it", "checkDelay", "lastCheck")
	def __init__(self, event:Event, it:Iterable, checkDelay:float=1.0):
		self.event:Event = event
		self.it:Iterator = it.__iter__()
		self.checkDelay:float = checkDelay
		self.lastCheck:float = monotonic()
	def __iter__(self) -> Iterator:
		return self
	def __next__(self) -> Any:
		m:float = monotonic()
		if m-self.lastCheck > self.checkDelay:
			self.lastCheck = m
			if self.event.is_set():
				raise KillSignal
		return self.it.__next__()

class BaseSignal:
	_force:bool
	@classmethod
	def check(self) -> bool:
		if not isinstance(Signal._handler, Signal):
			return False
		return Signal._handler._check(self._force)
	@classmethod
	def checkSoft(self) -> bool:
		if not isinstance(Signal._handler, Signal):
			return False
		return Signal._handler._check(False)
	@classmethod
	def checkHard(self) -> bool:
		if not isinstance(Signal._handler, Signal):
			return False
		return Signal._handler._check(True)
	@classmethod
	def sleep(self, seconds:Union[int, float], raiseOnKill:bool=False) -> None:
		if not isinstance(Signal._handler, Signal):
			return sleep(seconds)
		return Signal._handler._sleep(seconds, raiseOnKill, self._force)
	@classmethod
	def signalSoftKill(self, *args, **kwargs) -> None:
		if isinstance(Signal._handler, Signal):
			return Signal._handler._signalSoftKill(*args, **kwargs)
	@classmethod
	def signalHardKill(self, *args, **kwargs) -> None:
		if isinstance(Signal._handler, Signal):
			return Signal._handler._signalHardKill(*args, **kwargs)
	@classmethod
	def iter(self, it:Iterable, checkDelay:float=1.0) -> Iterable:
		if not isinstance(Signal._handler, Signal):
			return it
		return Signal._handler._iter(it, checkDelay, self._force)
	@classmethod
	def softKill(self) -> None:
		if isinstance(Signal._handler, Signal):
			return Signal._handler._softKill()
	@classmethod
	def hardKill(self) -> None:
		if isinstance(Signal._handler, Signal):
			return Signal._handler._hardKill()
	@classmethod
	def reset(self) -> None:
		if isinstance(Signal._handler, Signal):
			return Signal._handler._reset()
	@classmethod
	def getSoftSignal(self) -> Any:
		return SoftSignal
	@classmethod
	def getHardSignal(self) -> Any:
		return HardSignal
	@classmethod
	def isActivated(self) -> bool:
		return isinstance(Signal._handler, Signal)

class SoftSignal(BaseSignal):
	_force:bool = False

class HardSignal(BaseSignal):
	_force:bool = True

class Signal(HardSignal):
	eSoft:Event
	eHard:Event
	_handler:Optional[Signal] = None
	def __init__(self, softKillFn:Optional[Callable]=None, hardKillFn:Optional[Callable]=None,
	forceKillCounterFn:Optional[Callable]=None, forceCounter:int=10):
		self.softKillFn:Optional[Callable] = softKillFn
		self.hardKillFn:Optional[Callable] = hardKillFn
		self.forceKillCounterFn:Optional[Callable] = forceKillCounterFn
		self.counter:int = 0
		self.forceCounter:int = forceCounter
		self.eSoft = Event()
		self.eHard = Event()
		Signal._handler = self
		self._activate()
	def __getstate__(self) -> Dict[str, Any]:
		return {
			"softKillFn":self.softKillFn,
			"hardKillFn":self.hardKillFn,
			"forceCounter":self.forceCounter,
			"forceKillCounterFn":self.forceKillCounterFn,
			"eSoft":self.eSoft,
			"eHard":self.eHard,
		}
	def __setstate__(self, states:Dict[str, Any]) -> None:
		self.softKillFn = states["softKillFn"]
		self.hardKillFn = states["hardKillFn"]
		self.forceCounter = states["forceCounter"]
		self.forceKillCounterFn = states["forceKillCounterFn"]
		self.eSoft = states["eSoft"]
		self.eHard = states["eHard"]
		self._activate()
	def _activate(self) -> None:
		_signal.signal(_signal.SIGINT, Signal.signalSoftKill)
		_signal.signal(_signal.SIGTERM, Signal.signalHardKill)
	def _check(self, force:bool=True) -> bool:
		if force:
			return self.eHard.is_set()
		return self.eSoft.is_set()
	def _sleep(self, seconds:Union[int, float], raiseOnKill:bool=False, force:bool=True) -> None:
		if (self.eHard if force else self.eSoft).wait(float(seconds)) and raiseOnKill:
			raise KillSignal
	def _iter(self, it:Iterable, checkDelay:float=1.0, force:bool=True) -> Iterator:
		return SignalIterator(self.eHard if force else self.eSoft, it, checkDelay)
	def _signalSoftKill(self, *args, **kwargs) -> None:
		self._softKill()
		if not self.eHard.is_set():
			self.counter += 1
			if callable(self.forceKillCounterFn):
				try:
					self.forceKillCounterFn(self.counter, self.forceCounter)
				except:
					traceback.print_exc()
			if self.counter >= self.forceCounter:
				self._hardKill()
	def _signalHardKill(self, *args, **kwargs) -> None:
		self._softKill()
		self._hardKill()
	def _softKill(self) -> None:
		if not self.eSoft.is_set():
			self.eSoft.set()
			if callable(self.softKillFn):
				try:
					self.softKillFn()
				except:
					traceback.print_exc()
	def _hardKill(self) -> None:
		if not self.eHard.is_set():
			self.eHard.set()
			if callable(self.hardKillFn):
				try:
					self.hardKillFn()
				except:
					traceback.print_exc()
	def _reset(self) -> None:
		self.eSoft.clear()
		self.eHard.clear()
		self.counter = 0

class SignalTest(unittest.TestCase):
	rootSignal:Signal
	@classmethod
	def setUpClass(self) -> None:
		self.rootSignal = Signal()
	def tearDown(self) -> None:
		self.rootSignal.reset()
	def killmeTimer(self) -> None:
		def suicide():
			os.kill(os.getpid(), _signal.SIGINT)
		Timer(1, suicide).start()
	def test_sleep(self) -> None:
		t:float = monotonic()
		self.rootSignal.sleep(2)
		self.assertGreater(monotonic()-t, 2.0)
	def test_sleepRaise(self) -> None:
		self.killmeTimer()
		with self.assertRaises(KillSignal):
			self.rootSignal.getSoftSignal().sleep(2, raiseOnKill=True)
	def test_iter(self) -> None:
		s:list = list(range(5))
		d:list = []
		i:int
		signal:SoftSignal = self.rootSignal.getSoftSignal()
		self.killmeTimer()
		with self.assertRaises(KillSignal):
			for i in s:
				signal.sleep(0.5, raiseOnKill=True)
				d.append(i)
	def test_hardkill(self) -> None:
		self.killmeTimer()
		sleep(0.1)
		self.killmeTimer()
		sleep(0.1)
		self.killmeTimer()
		sleep(0.1)
		self.rootSignal.forceCounter = 3
		with self.assertRaises(KillSignal):
			self.rootSignal.sleep(10, raiseOnKill=True)
		self.rootSignal.forceCounter = 10
