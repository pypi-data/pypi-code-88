import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import threading
import Utils.classmake as cmake

class Event_onAsyncSearchFinished(threading.Thread):
	def __init__(self,e,func,args,name=""):
		self.e = e
		self.func=func
		super().__init__(target = func,name=name,args=args)
	def run(self):
		while True:
			self.e.wait()
			if hasattr(self.e, "recvData") and self.e.recvData is not None:
				viewmodel = self.e.recvData
				backData = json.loads(viewmodel).get("api")
				if self.name == "on" + backData:
					model = json.loads(viewmodel).get("Result")
					args = []
					if len(self._args) > 0:
						for key, arg in self._args.items():
							m = cmake.dict2obj(model.get(key[0].upper() + key[1:]), arg["t"])
							args.append(m)
					self.func(*args)
					self.e.recvData=None

class Event_onBeforePresentationItemActivation(threading.Thread):
	def __init__(self,e,func,args,name=""):
		self.e = e
		self.func=func
		super().__init__(target = func,name=name,args=args)
	def run(self):
		while True:
			self.e.wait()
			if hasattr(self.e, "recvData") and self.e.recvData is not None:
				viewmodel = self.e.recvData
				backData = json.loads(viewmodel).get("api")
				if self.name == "on" + backData:
					model = json.loads(viewmodel).get("Result")
					args = []
					if len(self._args) > 0:
						for key, arg in self._args.items():
							m = cmake.dict2obj(model.get(key[0].upper() + key[1:]), arg["t"])
							args.append(m)
					self.func(*args)
					self.e.recvData=None

class Event_onCameraChanged(threading.Thread):
	def __init__(self,e,func,args,name=""):
		self.e = e
		self.func=func
		super().__init__(target = func,name=name,args=args)
	def run(self):
		while True:
			self.e.wait()
			if hasattr(self.e, "recvData") and self.e.recvData is not None:
				viewmodel = self.e.recvData
				backData = json.loads(viewmodel).get("api")
				if self.name == "on" + backData:
					model = json.loads(viewmodel).get("Result")
					args = []
					if len(self._args) > 0:
						for key, arg in self._args.items():
							m = cmake.dict2obj(model.get(key[0].upper() + key[1:]), arg["t"])
							args.append(m)
					self.func(*args)
					self.e.recvData=None

class Event_onCameraFlyFinished(threading.Thread):
	def __init__(self,e,func,args,name=""):
		self.e = e
		self.func=func
		super().__init__(target = func,name=name,args=args)
	def run(self):
		while True:
			self.e.wait()
			if hasattr(self.e, "recvData") and self.e.recvData is not None:
				viewmodel = self.e.recvData
				backData = json.loads(viewmodel).get("api")
				if self.name == "on" + backData:
					model = json.loads(viewmodel).get("Result")
					args = []
					if len(self._args) > 0:
						for key, arg in self._args.items():
							m = cmake.dict2obj(model.get(key[0].upper() + key[1:]), arg["t"])
							args.append(m)
					self.func(*args)
					self.e.recvData=None

class Event_onCameraTourWaypointChanged(threading.Thread):
	def __init__(self,e,func,args,name=""):
		self.e = e
		self.func=func
		super().__init__(target = func,name=name,args=args)
	def run(self):
		while True:
			self.e.wait()
			if hasattr(self.e, "recvData") and self.e.recvData is not None:
				viewmodel = self.e.recvData
				backData = json.loads(viewmodel).get("api")
				if self.name == "on" + backData:
					model = json.loads(viewmodel).get("Result")
					args = []
					if len(self._args) > 0:
						for key, arg in self._args.items():
							m = cmake.dict2obj(model.get(key[0].upper() + key[1:]), arg["t"])
							args.append(m)
					self.func(*args)
					self.e.recvData=None

class Event_onCameraUndoRedoStatusChanged(threading.Thread):
	def __init__(self,e,func,args,name=""):
		self.e = e
		self.func=func
		super().__init__(target = func,name=name,args=args)
	def run(self):
		while True:
			self.e.wait()
			if hasattr(self.e, "recvData") and self.e.recvData is not None:
				viewmodel = self.e.recvData
				backData = json.loads(viewmodel).get("api")
				if self.name == "on" + backData:
					model = json.loads(viewmodel).get("Result")
					args = []
					if len(self._args) > 0:
						for key, arg in self._args.items():
							m = cmake.dict2obj(model.get(key[0].upper() + key[1:]), arg["t"])
							args.append(m)
					self.func(*args)
					self.e.recvData=None

class Event_onDataSourceDisconnected(threading.Thread):
	def __init__(self,e,func,args,name=""):
		self.e = e
		self.func=func
		super().__init__(target = func,name=name,args=args)
	def run(self):
		while True:
			self.e.wait()
			if hasattr(self.e, "recvData") and self.e.recvData is not None:
				viewmodel = self.e.recvData
				backData = json.loads(viewmodel).get("api")
				if self.name == "on" + backData:
					model = json.loads(viewmodel).get("Result")
					args = []
					if len(self._args) > 0:
						for key, arg in self._args.items():
							m = cmake.dict2obj(model.get(key[0].upper() + key[1:]), arg["t"])
							args.append(m)
					self.func(*args)
					self.e.recvData=None

class Event_onFeaturesMoving(threading.Thread):
	def __init__(self,e,func,args,name=""):
		self.e = e
		self.func=func
		super().__init__(target = func,name=name,args=args)
	def run(self):
		while True:
			self.e.wait()
			if hasattr(self.e, "recvData") and self.e.recvData is not None:
				viewmodel = self.e.recvData
				backData = json.loads(viewmodel).get("api")
				if self.name == "on" + backData:
					model = json.loads(viewmodel).get("Result")
					args = []
					if len(self._args) > 0:
						for key, arg in self._args.items():
							m = cmake.dict2obj(model.get(key[0].upper() + key[1:]), arg["t"])
							args.append(m)
					self.func(*args)
					self.e.recvData=None

class Event_onFrame(threading.Thread):
	def __init__(self,e,func,args,name=""):
		self.e = e
		self.func=func
		super().__init__(target = func,name=name,args=args)
	def run(self):
		while True:
			self.e.wait()
			if hasattr(self.e, "recvData") and self.e.recvData is not None:
				viewmodel = self.e.recvData
				backData = json.loads(viewmodel).get("api")
				if self.name == "on" + backData:
					model = json.loads(viewmodel).get("Result")
					args = []
					if len(self._args) > 0:
						for key, arg in self._args.items():
							m = cmake.dict2obj(model.get(key[0].upper() + key[1:]), arg["t"])
							args.append(m)
					self.func(*args)
					self.e.recvData=None

class Event_onFullScreenChanged(threading.Thread):
	def __init__(self,e,func,args,name=""):
		self.e = e
		self.func=func
		super().__init__(target = func,name=name,args=args)
	def run(self):
		while True:
			self.e.wait()
			if hasattr(self.e, "recvData") and self.e.recvData is not None:
				viewmodel = self.e.recvData
				backData = json.loads(viewmodel).get("api")
				if self.name == "on" + backData:
					model = json.loads(viewmodel).get("Result")
					args = []
					if len(self._args) > 0:
						for key, arg in self._args.items():
							m = cmake.dict2obj(model.get(key[0].upper() + key[1:]), arg["t"])
							args.append(m)
					self.func(*args)
					self.e.recvData=None

class Event_onInteractFocusChanged(threading.Thread):
	def __init__(self,e,func,args,name=""):
		self.e = e
		self.func=func
		super().__init__(target = func,name=name,args=args)
	def run(self):
		while True:
			self.e.wait()
			if hasattr(self.e, "recvData") and self.e.recvData is not None:
				viewmodel = self.e.recvData
				backData = json.loads(viewmodel).get("api")
				if self.name == "on" + backData:
					model = json.loads(viewmodel).get("Result")
					args = []
					if len(self._args) > 0:
						for key, arg in self._args.items():
							m = cmake.dict2obj(model.get(key[0].upper() + key[1:]), arg["t"])
							args.append(m)
					self.func(*args)
					self.e.recvData=None

class Event_onKeyDown(threading.Thread):
	def __init__(self,e,func,args,name=""):
		self.e = e
		self.func=func
		super().__init__(target = func,name=name,args=args)
	def run(self):
		while True:
			self.e.wait()
			if hasattr(self.e, "recvData") and self.e.recvData is not None:
				viewmodel = self.e.recvData
				backData = json.loads(viewmodel).get("api")
				if self.name == "on" + backData:
					model = json.loads(viewmodel).get("Result")
					args = []
					if len(self._args) > 0:
						for key, arg in self._args.items():
							m = cmake.dict2obj(model.get(key[0].upper() + key[1:]), arg["t"])
							args.append(m)
					self.func(*args)
					self.e.recvData=None

class Event_onKeyUp(threading.Thread):
	def __init__(self,e,func,args,name=""):
		self.e = e
		self.func=func
		super().__init__(target = func,name=name,args=args)
	def run(self):
		while True:
			self.e.wait()
			if hasattr(self.e, "recvData") and self.e.recvData is not None:
				viewmodel = self.e.recvData
				backData = json.loads(viewmodel).get("api")
				if self.name == "on" + backData:
					model = json.loads(viewmodel).get("Result")
					args = []
					if len(self._args) > 0:
						for key, arg in self._args.items():
							m = cmake.dict2obj(model.get(key[0].upper() + key[1:]), arg["t"])
							args.append(m)
					self.func(*args)
					self.e.recvData=None

class Event_onLButtonDblClk(threading.Thread):
	def __init__(self,e,func,args,name=""):
		self.e = e
		self.func=func
		super().__init__(target = func,name=name,args=args)
	def run(self):
		while True:
			self.e.wait()
			if hasattr(self.e, "recvData") and self.e.recvData is not None:
				viewmodel = self.e.recvData
				backData = json.loads(viewmodel).get("api")
				if self.name == "on" + backData:
					model = json.loads(viewmodel).get("Result")
					args = []
					if len(self._args) > 0:
						for key, arg in self._args.items():
							m = cmake.dict2obj(model.get(key[0].upper() + key[1:]), arg["t"])
							args.append(m)
					self.func(*args)
					self.e.recvData=None

class Event_onLButtonDown(threading.Thread):
	def __init__(self,e,func,args,name=""):
		self.e = e
		self.func=func
		super().__init__(target = func,name=name,args=args)
	def run(self):
		while True:
			self.e.wait()
			if hasattr(self.e, "recvData") and self.e.recvData is not None:
				viewmodel = self.e.recvData
				backData = json.loads(viewmodel).get("api")
				if self.name == "on" + backData:
					model = json.loads(viewmodel).get("Result")
					args = []
					if len(self._args) > 0:
						for key, arg in self._args.items():
							m = cmake.dict2obj(model.get(key[0].upper() + key[1:]), arg["t"])
							args.append(m)
					self.func(*args)
					self.e.recvData=None

class Event_onLButtonUp(threading.Thread):
	def __init__(self,e,func,args,name=""):
		self.e = e
		self.func=func
		super().__init__(target = func,name=name,args=args)
	def run(self):
		while True:
			self.e.wait()
			if hasattr(self.e, "recvData") and self.e.recvData is not None:
				viewmodel = self.e.recvData
				backData = json.loads(viewmodel).get("api")
				if self.name == "on" + backData:
					model = json.loads(viewmodel).get("Result")
					args = []
					if len(self._args) > 0:
						for key, arg in self._args.items():
							m = cmake.dict2obj(model.get(key[0].upper() + key[1:]), arg["t"])
							args.append(m)
					self.func(*args)
					self.e.recvData=None

class Event_onMButtonDblClk(threading.Thread):
	def __init__(self,e,func,args,name=""):
		self.e = e
		self.func=func
		super().__init__(target = func,name=name,args=args)
	def run(self):
		while True:
			self.e.wait()
			if hasattr(self.e, "recvData") and self.e.recvData is not None:
				viewmodel = self.e.recvData
				backData = json.loads(viewmodel).get("api")
				if self.name == "on" + backData:
					model = json.loads(viewmodel).get("Result")
					args = []
					if len(self._args) > 0:
						for key, arg in self._args.items():
							m = cmake.dict2obj(model.get(key[0].upper() + key[1:]), arg["t"])
							args.append(m)
					self.func(*args)
					self.e.recvData=None

class Event_onMButtonDown(threading.Thread):
	def __init__(self,e,func,args,name=""):
		self.e = e
		self.func=func
		super().__init__(target = func,name=name,args=args)
	def run(self):
		while True:
			self.e.wait()
			if hasattr(self.e, "recvData") and self.e.recvData is not None:
				viewmodel = self.e.recvData
				backData = json.loads(viewmodel).get("api")
				if self.name == "on" + backData:
					model = json.loads(viewmodel).get("Result")
					args = []
					if len(self._args) > 0:
						for key, arg in self._args.items():
							m = cmake.dict2obj(model.get(key[0].upper() + key[1:]), arg["t"])
							args.append(m)
					self.func(*args)
					self.e.recvData=None

class Event_onMButtonUp(threading.Thread):
	def __init__(self,e,func,args,name=""):
		self.e = e
		self.func=func
		super().__init__(target = func,name=name,args=args)
	def run(self):
		while True:
			self.e.wait()
			if hasattr(self.e, "recvData") and self.e.recvData is not None:
				viewmodel = self.e.recvData
				backData = json.loads(viewmodel).get("api")
				if self.name == "on" + backData:
					model = json.loads(viewmodel).get("Result")
					args = []
					if len(self._args) > 0:
						for key, arg in self._args.items():
							m = cmake.dict2obj(model.get(key[0].upper() + key[1:]), arg["t"])
							args.append(m)
					self.func(*args)
					self.e.recvData=None

class Event_onMouseClick(threading.Thread):
	def __init__(self,e,func,args,name=""):
		self.e = e
		self.func=func
		super().__init__(target = func,name=name,args=args)
	def run(self):
		while True:
			self.e.wait()
			if hasattr(self.e, "recvData") and self.e.recvData is not None:
				viewmodel = self.e.recvData
				backData = json.loads(viewmodel).get("api")
				if self.name == "on" + backData:
					model = json.loads(viewmodel).get("Result")
					args = []
					if len(self._args) > 0:
						for key, arg in self._args.items():
							m = cmake.dict2obj(model.get(key[0].upper() + key[1:]), arg["t"])
							args.append(m)
					self.func(*args)
					self.e.recvData=None

class Event_onMouseClickSelect(threading.Thread):
	def __init__(self,e,func,args,name=""):
		self.e = e
		self.func=func
		super().__init__(target = func,name=name,args=args)
	def run(self):
		while True:
			self.e.wait()
			if hasattr(self.e, "recvData") and self.e.recvData is not None:
				viewmodel = self.e.recvData
				backData = viewmodel["api"]
				if self.name == "on" + backData:
					model = viewmodel["Result"]
					args = []
					if len(self._args) > 0:
						for key, arg in self._args.items():
							m = cmake.dict2obj(model.get(key[0].upper() + key[1:]), arg["t"])
							args.append(m)
					self.func(*args)
					self.e.recvData=None

class Event_onMouseDragSelect(threading.Thread):
	def __init__(self,e,func,args,name=""):
		self.e = e
		self.func=func
		super().__init__(target = func,name=name,args=args)
	def run(self):
		while True:
			self.e.wait()
			if hasattr(self.e, "recvData") and self.e.recvData is not None:
				viewmodel = self.e.recvData
				backData = json.loads(viewmodel).get("api")
				if self.name == "on" + backData:
					model = json.loads(viewmodel).get("Result")
					args = []
					if len(self._args) > 0:
						for key, arg in self._args.items():
							m = cmake.dict2obj(model.get(key[0].upper() + key[1:]), arg["t"])
							args.append(m)
					self.func(*args)
					self.e.recvData=None

class Event_onMouseHover(threading.Thread):
	def __init__(self,e,func,args,name=""):
		self.e = e
		self.func=func
		super().__init__(target = func,name=name,args=args)
	def run(self):
		while True:
			self.e.wait()
			if hasattr(self.e, "recvData") and self.e.recvData is not None:
				viewmodel = self.e.recvData
				backData = json.loads(viewmodel).get("api")
				if self.name == "on" + backData:
					model = json.loads(viewmodel).get("Result")
					args = []
					if len(self._args) > 0:
						for key, arg in self._args.items():
							m = cmake.dict2obj(model.get(key[0].upper() + key[1:]), arg["t"])
							args.append(m)
					self.func(*args)
					self.e.recvData=None

class Event_onMouseMove(threading.Thread):
	def __init__(self,e,func,args,name=""):
		self.e = e
		self.func=func
		super().__init__(target = func,name=name,args=args)
	def run(self):
		while True:
			self.e.wait()
			if hasattr(self.e, "recvData") and self.e.recvData is not None:
				viewmodel = self.e.recvData
				backData = json.loads(viewmodel).get("api")
				if self.name == "on" + backData:
					model = json.loads(viewmodel).get("Result")
					args = []
					if len(self._args) > 0:
						for key, arg in self._args.items():
							m = cmake.dict2obj(model.get(key[0].upper() + key[1:]), arg["t"])
							args.append(m)
					self.func(*args)
					self.e.recvData=None

class Event_onMouseWheel(threading.Thread):
	def __init__(self,e,func,args,name=""):
		self.e = e
		self.func=func
		super().__init__(target = func,name=name,args=args)
	def run(self):
		while True:
			self.e.wait()
			if hasattr(self.e, "recvData") and self.e.recvData is not None:
				viewmodel = self.e.recvData
				backData = json.loads(viewmodel).get("api")
				if self.name == "on" + backData:
					model = json.loads(viewmodel).get("Result")
					args = []
					if len(self._args) > 0:
						for key, arg in self._args.items():
							m = cmake.dict2obj(model.get(key[0].upper() + key[1:]), arg["t"])
							args.append(m)
					self.func(*args)
					self.e.recvData=None

class Event_onObjectEditFinish(threading.Thread):
	def __init__(self,e,func,args,name=""):
		self.e = e
		self.func=func
		super().__init__(target = func,name=name,args=args)
	def run(self):
		while True:
			self.e.wait()
			if hasattr(self.e, "recvData") and self.e.recvData is not None:
				viewmodel = self.e.recvData
				backData = json.loads(viewmodel).get("api")
				if self.name == "on" + backData:
					model = json.loads(viewmodel).get("Result")
					args = []
					if len(self._args) > 0:
						for key, arg in self._args.items():
							m = cmake.dict2obj(model.get(key[0].upper() + key[1:]), arg["t"])
							args.append(m)
					self.func(*args)
					self.e.recvData=None

class Event_onObjectEditing(threading.Thread):
	def __init__(self,e,func,args,name=""):
		self.e = e
		self.func=func
		super().__init__(target = func,name=name,args=args)
	def run(self):
		while True:
			self.e.wait()
			if hasattr(self.e, "recvData") and self.e.recvData is not None:
				viewmodel = self.e.recvData
				backData = json.loads(viewmodel).get("api")
				if self.name == "on" + backData:
					model = json.loads(viewmodel).get("Result")
					args = []
					if len(self._args) > 0:
						for key, arg in self._args.items():
							m = cmake.dict2obj(model.get(key[0].upper() + key[1:]), arg["t"])
							args.append(m)
					self.func(*args)
					self.e.recvData=None

class Event_onPictureExportBegin(threading.Thread):
	def __init__(self,e,func,args,name=""):
		self.e = e
		self.func=func
		super().__init__(target = func,name=name,args=args)
	def run(self):
		while True:
			self.e.wait()
			if hasattr(self.e, "recvData") and self.e.recvData is not None:
				viewmodel = self.e.recvData
				backData = json.loads(viewmodel).get("api")
				if self.name == "on" + backData:
					model = json.loads(viewmodel).get("Result")
					args = []
					if len(self._args) > 0:
						for key, arg in self._args.items():
							m = cmake.dict2obj(model.get(key[0].upper() + key[1:]), arg["t"])
							args.append(m)
					self.func(*args)
					self.e.recvData=None

class Event_onPictureExportEnd(threading.Thread):
	def __init__(self,e,func,args,name=""):
		self.e = e
		self.func=func
		super().__init__(target = func,name=name,args=args)
	def run(self):
		while True:
			self.e.wait()
			if hasattr(self.e, "recvData") and self.e.recvData is not None:
				viewmodel = self.e.recvData
				backData = json.loads(viewmodel).get("api")
				if self.name == "on" + backData:
					model = json.loads(viewmodel).get("Result")
					args = []
					if len(self._args) > 0:
						for key, arg in self._args.items():
							m = cmake.dict2obj(model.get(key[0].upper() + key[1:]), arg["t"])
							args.append(m)
					self.func(*args)
					self.e.recvData=None

class Event_onPictureExporting(threading.Thread):
	def __init__(self,e,func,args,name=""):
		self.e = e
		self.func=func
		super().__init__(target = func,name=name,args=args)
	def run(self):
		while True:
			self.e.wait()
			if hasattr(self.e, "recvData") and self.e.recvData is not None:
				viewmodel = self.e.recvData
				backData = json.loads(viewmodel).get("api")
				if self.name == "on" + backData:
					model = json.loads(viewmodel).get("Result")
					args = []
					if len(self._args) > 0:
						for key, arg in self._args.items():
							m = cmake.dict2obj(model.get(key[0].upper() + key[1:]), arg["t"])
							args.append(m)
					self.func(*args)
					self.e.recvData=None

class Event_onPresentationFlyToReachedDestination(threading.Thread):
	def __init__(self,e,func,args,name=""):
		self.e = e
		self.func=func
		super().__init__(target = func,name=name,args=args)
	def run(self):
		while True:
			self.e.wait()
			if hasattr(self.e, "recvData") and self.e.recvData is not None:
				viewmodel = self.e.recvData
				backData = json.loads(viewmodel).get("api")
				if self.name == "on" + backData:
					model = json.loads(viewmodel).get("Result")
					args = []
					if len(self._args) > 0:
						for key, arg in self._args.items():
							m = cmake.dict2obj(model.get(key[0].upper() + key[1:]), arg["t"])
							args.append(m)
					self.func(*args)
					self.e.recvData=None

class Event_onPresentationStatusChanged(threading.Thread):
	def __init__(self,e,func,args,name=""):
		self.e = e
		self.func=func
		super().__init__(target = func,name=name,args=args)
	def run(self):
		while True:
			self.e.wait()
			if hasattr(self.e, "recvData") and self.e.recvData is not None:
				viewmodel = self.e.recvData
				backData = json.loads(viewmodel).get("api")
				if self.name == "on" + backData:
					model = json.loads(viewmodel).get("Result")
					args = []
					if len(self._args) > 0:
						for key, arg in self._args.items():
							m = cmake.dict2obj(model.get(key[0].upper() + key[1:]), arg["t"])
							args.append(m)
					self.func(*args)
					self.e.recvData=None

class Event_onProjectChanged(threading.Thread):
	def __init__(self,e,func,args,name=""):
		self.e = e
		self.func=func
		super().__init__(target = func,name=name,args=args)
	def run(self):
		while True:
			self.e.wait()
			if hasattr(self.e, "recvData") and self.e.recvData is not None:
				viewmodel = self.e.recvData
				backData = json.loads(viewmodel).get("api")
				if self.name == "on" + backData:
					model = json.loads(viewmodel).get("Result")
					args = []
					if len(self._args) > 0:
						for key, arg in self._args.items():
							m = cmake.dict2obj(model.get(key[0].upper() + key[1:]), arg["t"])
							args.append(m)
					self.func(*args)
					self.e.recvData=None

class Event_onRButtonDblClk(threading.Thread):
	def __init__(self,e,func,args,name=""):
		self.e = e
		self.func=func
		super().__init__(target = func,name=name,args=args)
	def run(self):
		while True:
			self.e.wait()
			if hasattr(self.e, "recvData") and self.e.recvData is not None:
				viewmodel = self.e.recvData
				backData = json.loads(viewmodel).get("api")
				if self.name == "on" + backData:
					model = json.loads(viewmodel).get("Result")
					args = []
					if len(self._args) > 0:
						for key, arg in self._args.items():
							m = cmake.dict2obj(model.get(key[0].upper() + key[1:]), arg["t"])
							args.append(m)
					self.func(*args)
					self.e.recvData=None

class Event_onRButtonDown(threading.Thread):
	def __init__(self,e,func,args,name=""):
		self.e = e
		self.func=func
		super().__init__(target = func,name=name,args=args)
	def run(self):
		while True:
			self.e.wait()
			if hasattr(self.e, "recvData") and self.e.recvData is not None:
				viewmodel = self.e.recvData
				backData = json.loads(viewmodel).get("api")
				if self.name == "on" + backData:
					model = json.loads(viewmodel).get("Result")
					args = []
					if len(self._args) > 0:
						for key, arg in self._args.items():
							m = cmake.dict2obj(model.get(key[0].upper() + key[1:]), arg["t"])
							args.append(m)
					self.func(*args)
					self.e.recvData=None

class Event_onRButtonUp(threading.Thread):
	def __init__(self,e,func,args,name=""):
		self.e = e
		self.func=func
		super().__init__(target = func,name=name,args=args)
	def run(self):
		while True:
			self.e.wait()
			if hasattr(self.e, "recvData") and self.e.recvData is not None:
				viewmodel = self.e.recvData
				backData = json.loads(viewmodel).get("api")
				if self.name == "on" + backData:
					model = json.loads(viewmodel).get("Result")
					args = []
					if len(self._args) > 0:
						for key, arg in self._args.items():
							m = cmake.dict2obj(model.get(key[0].upper() + key[1:]), arg["t"])
							args.append(m)
					self.func(*args)
					self.e.recvData=None

class Event_onResPacking(threading.Thread):
	def __init__(self,e,func,args,name=""):
		self.e = e
		self.func=func
		super().__init__(target = func,name=name,args=args)
	def run(self):
		while True:
			self.e.wait()
			if hasattr(self.e, "recvData") and self.e.recvData is not None:
				viewmodel = self.e.recvData
				backData = json.loads(viewmodel).get("api")
				if self.name == "on" + backData:
					model = json.loads(viewmodel).get("Result")
					args = []
					if len(self._args) > 0:
						for key, arg in self._args.items():
							m = cmake.dict2obj(model.get(key[0].upper() + key[1:]), arg["t"])
							args.append(m)
					self.func(*args)
					self.e.recvData=None

class Event_onTransformHelperBegin(threading.Thread):
	def __init__(self,e,func,args,name=""):
		self.e = e
		self.func=func
		super().__init__(target = func,name=name,args=args)
	def run(self):
		while True:
			self.e.wait()
			if hasattr(self.e, "recvData") and self.e.recvData is not None:
				viewmodel = self.e.recvData
				backData = json.loads(viewmodel).get("api")
				if self.name == "on" + backData:
					model = json.loads(viewmodel).get("Result")
					args = []
					if len(self._args) > 0:
						for key, arg in self._args.items():
							m = cmake.dict2obj(model.get(key[0].upper() + key[1:]), arg["t"])
							args.append(m)
					self.func(*args)
					self.e.recvData=None

class Event_onTransformHelperBoxScaling(threading.Thread):
	def __init__(self,e,func,args,name=""):
		self.e = e
		self.func=func
		super().__init__(target = func,name=name,args=args)
	def run(self):
		while True:
			self.e.wait()
			if hasattr(self.e, "recvData") and self.e.recvData is not None:
				viewmodel = self.e.recvData
				backData = json.loads(viewmodel).get("api")
				if self.name == "on" + backData:
					model = json.loads(viewmodel).get("Result")
					args = []
					if len(self._args) > 0:
						for key, arg in self._args.items():
							m = cmake.dict2obj(model.get(key[0].upper() + key[1:]), arg["t"])
							args.append(m)
					self.func(*args)
					self.e.recvData=None

class Event_onTransformHelperEnd(threading.Thread):
	def __init__(self,e,func,args,name=""):
		self.e = e
		self.func=func
		super().__init__(target = func,name=name,args=args)
	def run(self):
		while True:
			self.e.wait()
			if hasattr(self.e, "recvData") and self.e.recvData is not None:
				viewmodel = self.e.recvData
				backData = json.loads(viewmodel).get("api")
				if self.name == "on" + backData:
					model = json.loads(viewmodel).get("Result")
					args = []
					if len(self._args) > 0:
						for key, arg in self._args.items():
							m = cmake.dict2obj(model.get(key[0].upper() + key[1:]), arg["t"])
							args.append(m)
					self.func(*args)
					self.e.recvData=None

class Event_onTransformHelperMoving(threading.Thread):
	def __init__(self,e,func,args,name=""):
		self.e = e
		self.func=func
		super().__init__(target = func,name=name,args=args)
	def run(self):
		while True:
			self.e.wait()
			if hasattr(self.e, "recvData") and self.e.recvData is not None:
				viewmodel = self.e.recvData
				backData = json.loads(viewmodel).get("api")
				if self.name == "on" + backData:
					model = json.loads(viewmodel).get("Result")
					args = []
					if len(self._args) > 0:
						for key, arg in self._args.items():
							m = cmake.dict2obj(model.get(key[0].upper() + key[1:]), arg["t"])
							args.append(m)
					self.func(*args)
					self.e.recvData=None

class Event_onTransformHelperRotating(threading.Thread):
	def __init__(self,e,func,args,name=""):
		self.e = e
		self.func=func
		super().__init__(target = func,name=name,args=args)
	def run(self):
		while True:
			self.e.wait()
			if hasattr(self.e, "recvData") and self.e.recvData is not None:
				viewmodel = self.e.recvData
				backData = json.loads(viewmodel).get("api")
				if self.name == "on" + backData:
					model = json.loads(viewmodel).get("Result")
					args = []
					if len(self._args) > 0:
						for key, arg in self._args.items():
							m = cmake.dict2obj(model.get(key[0].upper() + key[1:]), arg["t"])
							args.append(m)
					self.func(*args)
					self.e.recvData=None

class Event_onTransformHelperScaling(threading.Thread):
	def __init__(self,e,func,args,name=""):
		self.e = e
		self.func=func
		super().__init__(target = func,name=name,args=args)
	def run(self):
		while True:
			self.e.wait()
			if hasattr(self.e, "recvData") and self.e.recvData is not None:
				viewmodel = self.e.recvData
				backData = json.loads(viewmodel).get("api")
				if self.name == "on" + backData:
					model = json.loads(viewmodel).get("Result")
					args = []
					if len(self._args) > 0:
						for key, arg in self._args.items():
							m = cmake.dict2obj(model.get(key[0].upper() + key[1:]), arg["t"])
							args.append(m)
					self.func(*args)
					self.e.recvData=None

class Event_onUIWindowEvent(threading.Thread):
	def __init__(self,e,func,args,name=""):
		self.e = e
		self.func=func
		super().__init__(target = func,name=name,args=args)
	def run(self):
		while True:
			self.e.wait()
			if hasattr(self.e, "recvData") and self.e.recvData is not None:
				viewmodel = self.e.recvData
				backData = json.loads(viewmodel).get("api")
				if self.name == "on" + backData:
					model = json.loads(viewmodel).get("Result")
					args = []
					if len(self._args) > 0:
						for key, arg in self._args.items():
							m = cmake.dict2obj(model.get(key[0].upper() + key[1:]), arg["t"])
							args.append(m)
					self.func(*args)
					self.e.recvData=None

class Event_onVideoExportBegin(threading.Thread):
	def __init__(self,e,func,args,name=""):
		self.e = e
		self.func=func
		super().__init__(target = func,name=name,args=args)
	def run(self):
		while True:
			self.e.wait()
			if hasattr(self.e, "recvData") and self.e.recvData is not None:
				viewmodel = self.e.recvData
				backData = json.loads(viewmodel).get("api")
				if self.name == "on" + backData:
					model = json.loads(viewmodel).get("Result")
					args = []
					if len(self._args) > 0:
						for key, arg in self._args.items():
							m = cmake.dict2obj(model.get(key[0].upper() + key[1:]), arg["t"])
							args.append(m)
					self.func(*args)
					self.e.recvData=None

class Event_onVideoExportEnd(threading.Thread):
	def __init__(self,e,func,args,name=""):
		self.e = e
		self.func=func
		super().__init__(target = func,name=name,args=args)
	def run(self):
		while True:
			self.e.wait()
			if hasattr(self.e, "recvData") and self.e.recvData is not None:
				viewmodel = self.e.recvData
				backData = json.loads(viewmodel).get("api")
				if self.name == "on" + backData:
					model = json.loads(viewmodel).get("Result")
					args = []
					if len(self._args) > 0:
						for key, arg in self._args.items():
							m = cmake.dict2obj(model.get(key[0].upper() + key[1:]), arg["t"])
							args.append(m)
					self.func(*args)
					self.e.recvData=None

class Event_onVideoExporting(threading.Thread):
	def __init__(self,e,func,args,name=""):
		self.e = e
		self.func=func
		super().__init__(target = func,name=name,args=args)
	def run(self):
		while True:
			self.e.wait()
			if hasattr(self.e, "recvData") and self.e.recvData is not None:
				viewmodel = self.e.recvData
				backData = json.loads(viewmodel).get("api")
				if self.name == "on" + backData:
					model = json.loads(viewmodel).get("Result")
					args = []
					if len(self._args) > 0:
						for key, arg in self._args.items():
							m = cmake.dict2obj(model.get(key[0].upper() + key[1:]), arg["t"])
							args.append(m)
					self.func(*args)
					self.e.recvData=None
