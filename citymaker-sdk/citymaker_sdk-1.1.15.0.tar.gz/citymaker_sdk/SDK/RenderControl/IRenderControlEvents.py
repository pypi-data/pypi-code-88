import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.wsInit  as wsObj
from Utils.IRenderControlEventClass import *
import threading
import Utils.classmake as cmake
class IRenderControlEvents():
	Events ={
	"cName":"IRenderControlEvents",
	"onAsyncSearchFinished":  { "fn":None, "args": {"strId": {"t": "S"},"pCursor": {"t": "IFdeCursor"}}}, 
	"onBeforePresentationItemActivation":  { "fn":None, "args": {"presentationID": {"t": "S"},"step": {"t": "IPresentationStep"}}}, 
	"onCameraChanged":  { "fn":None, "args": {"isPositionChanged": {"t": "B"},"isRotationChanged": {"t": "B"}}}, 
	"onCameraFlyFinished":  { "fn":None, "args": {"type": {"t": "N"}}}, 
	"onCameraTourWaypointChanged":  { "fn":None, "args": {"index": {"t": "N"}}}, 
	"onCameraUndoRedoStatusChanged":  { "fn":None}, 
	"onDataSourceDisconnected":  { "fn":None, "args": {"dataSourceGuid": {"t": "S"},"connectionInfo": {"t": "S"}}}, 
	"onFeaturesMoving":  { "fn":None, "args": {"translate": {"t": "IVector3"}}}, 
	"onFrame":  { "fn":None, "args": {"frameIndex": {"t": "N"},"referencedTime": {"t": "N"}}}, 
	"onFullScreenChanged":  { "fn":None, "args": {"isFullScreen": {"t": "B"}}}, 
	"onInteractFocusChanged":  { "fn":None, "args": {"position": {"t": "IVector3"}}}, 
	"onKeyDown":  { "fn":None, "args": {"flags": {"t": "N"},"char": {"t": "N"}}}, 
	"onKeyUp":  { "fn":None, "args": {"flags": {"t": "N"},"char": {"t": "N"}}}, 
	"onLButtonDblClk":  { "fn":None, "args": {"flags": {"t": "N"},"x": {"t": "N"},"y": {"t": "N"}}}, 
	"onLButtonDown":  { "fn":None, "args": {"flags": {"t": "N"},"x": {"t": "N"},"y": {"t": "N"}}}, 
	"onLButtonUp":  { "fn":None, "args": {"flags": {"t": "N"},"x": {"t": "N"},"y": {"t": "N"}}}, 
	"onMButtonDblClk":  { "fn":None, "args": {"flags": {"t": "N"},"x": {"t": "N"},"y": {"t": "N"}}}, 
	"onMButtonDown":  { "fn":None, "args": {"flags": {"t": "N"},"x": {"t": "N"},"y": {"t": "N"}}}, 
	"onMButtonUp":  { "fn":None, "args": {"flags": {"t": "N"},"x": {"t": "N"},"y": {"t": "N"}}}, 
	"onMouseClick":  { "fn":None, "args": {"mouseButton": {"t": "gviUIMouseButtonType"},"x": {"t": "N"},"y": {"t": "N"}}}, 
	"onMouseClickSelect":  { "fn":None, "args": {"pickResult": {"t": "IPickResult"},"intersectPoint": {"t": "IPoint"},"mask": {"t": "gviModKeyMask"},"eventSender": {"t": "gviMouseSelectMode"}}}, 
	"onMouseDragSelect":  { "fn":None, "args": {"pickResults": {"t": "IPickResultCollection"},"mask": {"t": "gviModKeyMask"}}}, 
	"onMouseHover":  { "fn":None, "args": {"flags": {"t": "N"},"x": {"t": "N"},"y": {"t": "N"}}}, 
	"onMouseMove":  { "fn":None, "args": {"flags": {"t": "N"},"x": {"t": "N"},"y": {"t": "N"}}}, 
	"onMouseWheel":  { "fn":None, "args": {"flags": {"t": "N"},"delta": {"t": "N"},"x": {"t": "N"},"y": {"t": "N"}}}, 
	"onObjectEditFinish":  { "fn":None}, 
	"onObjectEditing":  { "fn":None, "args": {"geometry": {"t": "IGeometry"}}}, 
	"onPictureExportBegin":  { "fn":None, "args": {"numberOfWidth": {"t": "N"},"numberOfHeight": {"t": "N"}}}, 
	"onPictureExportEnd":  { "fn":None, "args": {"time": {"t": "N"},"isAborted": {"t": "B"},"picStream": {"t": "O"}}}, 
	"onPictureExporting":  { "fn":None, "args": {"index": {"t": "N"},"percentage": {"t": "N"}}}, 
	"onPresentationFlyToReachedDestination":  { "fn":None, "args": {"presentationID": {"t": "S"},"step": {"t": "IPresentationStep"}}}, 
	"onPresentationStatusChanged":  { "fn":None, "args": {"presentationID": {"t": "S"},"status": {"t": "gviPresentationStatus"}}}, 
	"onProjectChanged":  { "fn":None}, 
	"onRButtonDblClk":  { "fn":None, "args": {"flags": {"t": "N"},"x": {"t": "N"},"y": {"t": "N"}}}, 
	"onRButtonDown":  { "fn":None, "args": {"flags": {"t": "N"},"x": {"t": "N"},"y": {"t": "N"}}}, 
	"onRButtonUp":  { "fn":None, "args": {"flags": {"t": "N"},"x": {"t": "N"},"y": {"t": "N"}}}, 
	"onResPacking":  { "fn":None, "args": {"totalResNo": {"t": "N"},"curResIndex": {"t": "N"}}}, 
	"onTransformHelperBegin":  { "fn":None}, 
	"onTransformHelperBoxScaling":  { "fn":None, "args": {"center": {"t": "IVector3"},"scale": {"t": "IVector3"}}}, 
	"onTransformHelperEnd":  { "fn":None}, 
	"onTransformHelperMoving":  { "fn":None, "args": {"position": {"t": "IVector3"}}}, 
	"onTransformHelperRotating":  { "fn":None, "args": {"axis": {"t": "IVector3"},"angle": {"t": "N"}}}, 
	"onTransformHelperScaling":  { "fn":None, "args": {"scale": {"t": "IVector3"}}}, 
	"onUIWindowEvent":  { "fn":None, "args": {"eventArgs": {"t": "IUIEventArgs"},"eventType": {"t": "gviUIEventType"}}}, 
	"onVideoExportBegin":  { "fn":None, "args": {"totalTime": {"t": "N"}}}, 
	"onVideoExportEnd":  { "fn":None, "args": {"time": {"t": "N"},"isAborted": {"t": "B"}}}, 
	"onVideoExporting":  { "fn":None, "args": {"percentage": {"t": "N"}}} 
  }
	threads = []

	@property
	def onAsyncSearchFinished(self):
		return self.Events["onAsyncSearchFinished"]["fn"]

	@onAsyncSearchFinished.setter
	def onAsyncSearchFinished(self,fn):
		JsonData = {"api": "RenderControl.RcAsyncSearchFinished","EventName": ""}
		if type(fn).__name__ == "function":
			self.Events["onAsyncSearchFinished"]["fn"]= fn
			JsonData["EventName"] = "onAsyncSearchFinished"
		else:
			self.Events["onAsyncSearchFinished"]["fn"] = None
		wsObj.postMessage({ "propertyType":"onAsyncSearchFinished", "_HashCode": "" },None,JsonData,False)
		if fn:
			rcEvent=wsObj.getrcEvent()
			eventp1 = Event_onAsyncSearchFinished(rcEvent,fn,(self.Events["onAsyncSearchFinished"]["args"]),"onAsyncSearchFinished")
			eventp1.start()
	@property
	def onBeforePresentationItemActivation(self):
		return self.Events["onBeforePresentationItemActivation"]["fn"]

	@onBeforePresentationItemActivation.setter
	def onBeforePresentationItemActivation(self,fn):
		JsonData = {"api": "RenderControl.RcBeforePresentationItemActivation","EventName": ""}
		if type(fn).__name__ == "function":
			self.Events["onBeforePresentationItemActivation"]["fn"]= fn
			JsonData["EventName"] = "onBeforePresentationItemActivation"
		else:
			self.Events["onBeforePresentationItemActivation"]["fn"] = None
		wsObj.postMessage({ "propertyType":"onBeforePresentationItemActivation", "_HashCode": "" },None,JsonData,False)
		if fn:
			rcEvent=wsObj.getrcEvent()
			eventp1 = Event_onBeforePresentationItemActivation(rcEvent,fn,(self.Events["onBeforePresentationItemActivation"]["args"]),"onBeforePresentationItemActivation")
			eventp1.start()
	@property
	def onCameraChanged(self):
		return self.Events["onCameraChanged"]["fn"]

	@onCameraChanged.setter
	def onCameraChanged(self,fn):
		JsonData = {"api": "RenderControl.RcCameraChanged","EventName": ""}
		if type(fn).__name__ == "function":
			self.Events["onCameraChanged"]["fn"]= fn
			JsonData["EventName"] = "onCameraChanged"
		else:
			self.Events["onCameraChanged"]["fn"] = None
		wsObj.postMessage({ "propertyType":"onCameraChanged", "_HashCode": "" },None,JsonData,False)
		if fn:
			rcEvent=wsObj.getrcEvent()
			eventp1 = Event_onCameraChanged(rcEvent,fn,(self.Events["onCameraChanged"]["args"]),"onCameraChanged")
			eventp1.start()
	@property
	def onCameraFlyFinished(self):
		return self.Events["onCameraFlyFinished"]["fn"]

	@onCameraFlyFinished.setter
	def onCameraFlyFinished(self,fn):
		JsonData = {"api": "RenderControl.RcCameraFlyFinished","EventName": ""}
		if type(fn).__name__ == "function":
			self.Events["onCameraFlyFinished"]["fn"]= fn
			JsonData["EventName"] = "onCameraFlyFinished"
		else:
			self.Events["onCameraFlyFinished"]["fn"] = None
		wsObj.postMessage({ "propertyType":"onCameraFlyFinished", "_HashCode": "" },None,JsonData,False)
		if fn:
			rcEvent=wsObj.getrcEvent()
			eventp1 = Event_onCameraFlyFinished(rcEvent,fn,(self.Events["onCameraFlyFinished"]["args"]),"onCameraFlyFinished")
			eventp1.start()
	@property
	def onCameraTourWaypointChanged(self):
		return self.Events["onCameraTourWaypointChanged"]["fn"]

	@onCameraTourWaypointChanged.setter
	def onCameraTourWaypointChanged(self,fn):
		JsonData = {"api": "RenderControl.RcCameraTourWaypointChanged","EventName": ""}
		if type(fn).__name__ == "function":
			self.Events["onCameraTourWaypointChanged"]["fn"]= fn
			JsonData["EventName"] = "onCameraTourWaypointChanged"
		else:
			self.Events["onCameraTourWaypointChanged"]["fn"] = None
		wsObj.postMessage({ "propertyType":"onCameraTourWaypointChanged", "_HashCode": "" },None,JsonData,False)
		if fn:
			rcEvent=wsObj.getrcEvent()
			eventp1 = Event_onCameraTourWaypointChanged(rcEvent,fn,(self.Events["onCameraTourWaypointChanged"]["args"]),"onCameraTourWaypointChanged")
			eventp1.start()
	@property
	def onCameraUndoRedoStatusChanged(self):
		return self.Events["onCameraUndoRedoStatusChanged"]["fn"]

	@onCameraUndoRedoStatusChanged.setter
	def onCameraUndoRedoStatusChanged(self,fn):
		JsonData = {"api": "RenderControl.RcCameraUndoRedoStatusChanged","EventName": ""}
		if type(fn).__name__ == "function":
			self.Events["onCameraUndoRedoStatusChanged"]["fn"]= fn
			JsonData["EventName"] = "onCameraUndoRedoStatusChanged"
		else:
			self.Events["onCameraUndoRedoStatusChanged"]["fn"] = None
		wsObj.postMessage({ "propertyType":"onCameraUndoRedoStatusChanged", "_HashCode": "" },None,JsonData,False)
		rcEvent=wsObj.getrcEvent()
		eventp1 = Event_onCameraUndoRedoStatusChanged(rcEvent, fn, (), "onCameraUndoRedoStatusChanged")
		eventp1.start()
	@property
	def onDataSourceDisconnected(self):
		return self.Events["onDataSourceDisconnected"]["fn"]

	@onDataSourceDisconnected.setter
	def onDataSourceDisconnected(self,fn):
		JsonData = {"api": "RenderControl.RcDataSourceDisconnected","EventName": ""}
		if type(fn).__name__ == "function":
			self.Events["onDataSourceDisconnected"]["fn"]= fn
			JsonData["EventName"] = "onDataSourceDisconnected"
		else:
			self.Events["onDataSourceDisconnected"]["fn"] = None
		wsObj.postMessage({ "propertyType":"onDataSourceDisconnected", "_HashCode": "" },None,JsonData,False)
		if fn:
			rcEvent=wsObj.getrcEvent()
			eventp1 = Event_onDataSourceDisconnected(rcEvent,fn,(self.Events["onDataSourceDisconnected"]["args"]),"onDataSourceDisconnected")
			eventp1.start()
	@property
	def onFeaturesMoving(self):
		return self.Events["onFeaturesMoving"]["fn"]

	@onFeaturesMoving.setter
	def onFeaturesMoving(self,fn):
		JsonData = {"api": "RenderControl.RcFeaturesMoving","EventName": ""}
		if type(fn).__name__ == "function":
			self.Events["onFeaturesMoving"]["fn"]= fn
			JsonData["EventName"] = "onFeaturesMoving"
		else:
			self.Events["onFeaturesMoving"]["fn"] = None
		wsObj.postMessage({ "propertyType":"onFeaturesMoving", "_HashCode": "" },None,JsonData,False)
		if fn:
			rcEvent=wsObj.getrcEvent()
			eventp1 = Event_onFeaturesMoving(rcEvent,fn,(self.Events["onFeaturesMoving"]["args"]),"onFeaturesMoving")
			eventp1.start()
	@property
	def onFrame(self):
		return self.Events["onFrame"]["fn"]

	@onFrame.setter
	def onFrame(self,fn):
		JsonData = {"api": "RenderControl.RcFrame","EventName": ""}
		if type(fn).__name__ == "function":
			self.Events["onFrame"]["fn"]= fn
			JsonData["EventName"] = "onFrame"
		else:
			self.Events["onFrame"]["fn"] = None
		wsObj.postMessage({ "propertyType":"onFrame", "_HashCode": "" },None,JsonData,False)
		if fn:
			rcEvent=wsObj.getrcEvent()
			eventp1 = Event_onFrame(rcEvent,fn,(self.Events["onFrame"]["args"]),"onFrame")
			eventp1.start()
	@property
	def onFullScreenChanged(self):
		return self.Events["onFullScreenChanged"]["fn"]

	@onFullScreenChanged.setter
	def onFullScreenChanged(self,fn):
		JsonData = {"api": "RenderControl.RcFullScreenChanged","EventName": ""}
		if type(fn).__name__ == "function":
			self.Events["onFullScreenChanged"]["fn"]= fn
			JsonData["EventName"] = "onFullScreenChanged"
		else:
			self.Events["onFullScreenChanged"]["fn"] = None
		wsObj.postMessage({ "propertyType":"onFullScreenChanged", "_HashCode": "" },None,JsonData,False)
		if fn:
			rcEvent=wsObj.getrcEvent()
			eventp1 = Event_onFullScreenChanged(rcEvent,fn,(self.Events["onFullScreenChanged"]["args"]),"onFullScreenChanged")
			eventp1.start()
	@property
	def onInteractFocusChanged(self):
		return self.Events["onInteractFocusChanged"]["fn"]

	@onInteractFocusChanged.setter
	def onInteractFocusChanged(self,fn):
		JsonData = {"api": "RenderControl.RcInteractFocusChanged","EventName": ""}
		if type(fn).__name__ == "function":
			self.Events["onInteractFocusChanged"]["fn"]= fn
			JsonData["EventName"] = "onInteractFocusChanged"
		else:
			self.Events["onInteractFocusChanged"]["fn"] = None
		wsObj.postMessage({ "propertyType":"onInteractFocusChanged", "_HashCode": "" },None,JsonData,False)
		if fn:
			rcEvent=wsObj.getrcEvent()
			eventp1 = Event_onInteractFocusChanged(rcEvent,fn,(self.Events["onInteractFocusChanged"]["args"]),"onInteractFocusChanged")
			eventp1.start()
	@property
	def onKeyDown(self):
		return self.Events["onKeyDown"]["fn"]

	@onKeyDown.setter
	def onKeyDown(self,fn):
		JsonData = {"api": "RenderControl.RcKeyDown","EventName": ""}
		if type(fn).__name__ == "function":
			self.Events["onKeyDown"]["fn"]= fn
			JsonData["EventName"] = "onKeyDown"
		else:
			self.Events["onKeyDown"]["fn"] = None
		wsObj.postMessage({ "propertyType":"onKeyDown", "_HashCode": "" },None,JsonData,False)
		if fn:
			rcEvent=wsObj.getrcEvent()
			eventp1 = Event_onKeyDown(rcEvent,fn,(self.Events["onKeyDown"]["args"]),"onKeyDown")
			eventp1.start()
	@property
	def onKeyUp(self):
		return self.Events["onKeyUp"]["fn"]

	@onKeyUp.setter
	def onKeyUp(self,fn):
		JsonData = {"api": "RenderControl.RcKeyUp","EventName": ""}
		if type(fn).__name__ == "function":
			self.Events["onKeyUp"]["fn"]= fn
			JsonData["EventName"] = "onKeyUp"
		else:
			self.Events["onKeyUp"]["fn"] = None
		wsObj.postMessage({ "propertyType":"onKeyUp", "_HashCode": "" },None,JsonData,False)
		if fn:
			rcEvent=wsObj.getrcEvent()
			eventp1 = Event_onKeyUp(rcEvent,fn,(self.Events["onKeyUp"]["args"]),"onKeyUp")
			eventp1.start()
	@property
	def onLButtonDblClk(self):
		return self.Events["onLButtonDblClk"]["fn"]

	@onLButtonDblClk.setter
	def onLButtonDblClk(self,fn):
		JsonData = {"api": "RenderControl.RcLButtonDblClk","EventName": ""}
		if type(fn).__name__ == "function":
			self.Events["onLButtonDblClk"]["fn"]= fn
			JsonData["EventName"] = "onLButtonDblClk"
		else:
			self.Events["onLButtonDblClk"]["fn"] = None
		wsObj.postMessage({ "propertyType":"onLButtonDblClk", "_HashCode": "" },None,JsonData,False)
		if fn:
			rcEvent=wsObj.getrcEvent()
			eventp1 = Event_onLButtonDblClk(rcEvent,fn,(self.Events["onLButtonDblClk"]["args"]),"onLButtonDblClk")
			eventp1.start()
	@property
	def onLButtonDown(self):
		return self.Events["onLButtonDown"]["fn"]

	@onLButtonDown.setter
	def onLButtonDown(self,fn):
		JsonData = {"api": "RenderControl.RcLButtonDown","EventName": ""}
		if type(fn).__name__ == "function":
			self.Events["onLButtonDown"]["fn"]= fn
			JsonData["EventName"] = "onLButtonDown"
		else:
			self.Events["onLButtonDown"]["fn"] = None
		wsObj.postMessage({ "propertyType":"onLButtonDown", "_HashCode": "" },None,JsonData,False)
		if fn:
			rcEvent=wsObj.getrcEvent()
			eventp1 = Event_onLButtonDown(rcEvent,fn,(self.Events["onLButtonDown"]["args"]),"onLButtonDown")
			eventp1.start()
	@property
	def onLButtonUp(self):
		return self.Events["onLButtonUp"]["fn"]

	@onLButtonUp.setter
	def onLButtonUp(self,fn):
		JsonData = {"api": "RenderControl.RcLButtonUp","EventName": ""}
		if type(fn).__name__ == "function":
			self.Events["onLButtonUp"]["fn"]= fn
			JsonData["EventName"] = "onLButtonUp"
		else:
			self.Events["onLButtonUp"]["fn"] = None
		wsObj.postMessage({ "propertyType":"onLButtonUp", "_HashCode": "" },None,JsonData,False)
		if fn:
			rcEvent=wsObj.getrcEvent()
			eventp1 = Event_onLButtonUp(rcEvent,fn,(self.Events["onLButtonUp"]["args"]),"onLButtonUp")
			eventp1.start()
	@property
	def onMButtonDblClk(self):
		return self.Events["onMButtonDblClk"]["fn"]

	@onMButtonDblClk.setter
	def onMButtonDblClk(self,fn):
		JsonData = {"api": "RenderControl.RcMButtonDblClk","EventName": ""}
		if type(fn).__name__ == "function":
			self.Events["onMButtonDblClk"]["fn"]= fn
			JsonData["EventName"] = "onMButtonDblClk"
		else:
			self.Events["onMButtonDblClk"]["fn"] = None
		wsObj.postMessage({ "propertyType":"onMButtonDblClk", "_HashCode": "" },None,JsonData,False)
		if fn:
			rcEvent=wsObj.getrcEvent()
			eventp1 = Event_onMButtonDblClk(rcEvent,fn,(self.Events["onMButtonDblClk"]["args"]),"onMButtonDblClk")
			eventp1.start()
	@property
	def onMButtonDown(self):
		return self.Events["onMButtonDown"]["fn"]

	@onMButtonDown.setter
	def onMButtonDown(self,fn):
		JsonData = {"api": "RenderControl.RcMButtonDown","EventName": ""}
		if type(fn).__name__ == "function":
			self.Events["onMButtonDown"]["fn"]= fn
			JsonData["EventName"] = "onMButtonDown"
		else:
			self.Events["onMButtonDown"]["fn"] = None
		wsObj.postMessage({ "propertyType":"onMButtonDown", "_HashCode": "" },None,JsonData,False)
		if fn:
			rcEvent=wsObj.getrcEvent()
			eventp1 = Event_onMButtonDown(rcEvent,fn,(self.Events["onMButtonDown"]["args"]),"onMButtonDown")
			eventp1.start()
	@property
	def onMButtonUp(self):
		return self.Events["onMButtonUp"]["fn"]

	@onMButtonUp.setter
	def onMButtonUp(self,fn):
		JsonData = {"api": "RenderControl.RcMButtonUp","EventName": ""}
		if type(fn).__name__ == "function":
			self.Events["onMButtonUp"]["fn"]= fn
			JsonData["EventName"] = "onMButtonUp"
		else:
			self.Events["onMButtonUp"]["fn"] = None
		wsObj.postMessage({ "propertyType":"onMButtonUp", "_HashCode": "" },None,JsonData,False)
		if fn:
			rcEvent=wsObj.getrcEvent()
			eventp1 = Event_onMButtonUp(rcEvent,fn,(self.Events["onMButtonUp"]["args"]),"onMButtonUp")
			eventp1.start()
	@property
	def onMouseClick(self):
		return self.Events["onMouseClick"]["fn"]

	@onMouseClick.setter
	def onMouseClick(self,fn):
		JsonData = {"api": "RenderControl.RcMouseClick","EventName": ""}
		if type(fn).__name__ == "function":
			self.Events["onMouseClick"]["fn"]= fn
			JsonData["EventName"] = "onMouseClick"
		else:
			self.Events["onMouseClick"]["fn"] = None
		wsObj.postMessage({ "propertyType":"onMouseClick", "_HashCode": "" },None,JsonData,False)
		if fn:
			rcEvent=wsObj.getrcEvent()
			eventp1 = Event_onMouseClick(rcEvent,fn,(self.Events["onMouseClick"]["args"]),"onMouseClick")
			eventp1.start()
	@property
	def onMouseClickSelect(self):
		return self.Events["onMouseClickSelect"]["fn"]

	@onMouseClickSelect.setter
	def onMouseClickSelect(self,fn):
		JsonData = {"api": "RenderControl.RcMouseClickSelect","EventName": ""}
		if type(fn).__name__ == "function":
			self.Events["onMouseClickSelect"]["fn"]= fn
			JsonData["EventName"] = "onMouseClickSelect"
		else:
			self.Events["onMouseClickSelect"]["fn"] = None
			# threads.append(thread1)
		wsObj.postMessage({ "propertyType":"onMouseClickSelect", "_HashCode": "" },None,JsonData,False)
		if fn:
			rcEvent=wsObj.getrcEvent()
			eventp1 = Event_onMouseClickSelect(rcEvent,fn,(self.Events["onMouseClickSelect"]["args"]),"onMouseClickSelect")
			eventp1.start()
			# threads.append(eventp1)
		# else:
		# 	_async_raise(eventp1.ident, SystemExit)

	@property
	def onMouseDragSelect(self):
		return self.Events["onMouseDragSelect"]["fn"]

	@onMouseDragSelect.setter
	def onMouseDragSelect(self,fn):
		JsonData = {"api": "RenderControl.RcMouseDragSelect","EventName": ""}
		if type(fn).__name__ == "function":
			self.Events["onMouseDragSelect"]["fn"]= fn
			JsonData["EventName"] = "onMouseDragSelect"
		else:
			self.Events["onMouseDragSelect"]["fn"] = None
		wsObj.postMessage({ "propertyType":"onMouseDragSelect", "_HashCode": "" },None,JsonData,False)
		if fn:
			rcEvent=wsObj.getrcEvent()
			eventp1 = Event_onMouseDragSelect(rcEvent,fn,(self.Events["onMouseDragSelect"]["args"]),"onMouseDragSelect")
			eventp1.start()
	@property
	def onMouseHover(self):
		return self.Events["onMouseHover"]["fn"]

	@onMouseHover.setter
	def onMouseHover(self,fn):
		JsonData = {"api": "RenderControl.RcMouseHover","EventName": ""}
		if type(fn).__name__ == "function":
			self.Events["onMouseHover"]["fn"]= fn
			JsonData["EventName"] = "onMouseHover"
		else:
			self.Events["onMouseHover"]["fn"] = None
		wsObj.postMessage({ "propertyType":"onMouseHover", "_HashCode": "" },None,JsonData,False)
		if fn:
			rcEvent=wsObj.getrcEvent()
			eventp1 = Event_onMouseHover(rcEvent,fn,(self.Events["onMouseHover"]["args"]),"onMouseHover")
			eventp1.start()
	@property
	def onMouseMove(self):
		return self.Events["onMouseMove"]["fn"]

	@onMouseMove.setter
	def onMouseMove(self,fn):
		JsonData = {"api": "RenderControl.RcMouseMove","EventName": ""}
		if type(fn).__name__ == "function":
			self.Events["onMouseMove"]["fn"]= fn
			JsonData["EventName"] = "onMouseMove"
		else:
			self.Events["onMouseMove"]["fn"] = None
		wsObj.postMessage({ "propertyType":"onMouseMove", "_HashCode": "" },None,JsonData,False)
		if fn:
			rcEvent=wsObj.getrcEvent()
			eventp1 = Event_onMouseMove(rcEvent,fn,(self.Events["onMouseMove"]["args"]),"onMouseMove")
			eventp1.start()
	@property
	def onMouseWheel(self):
		return self.Events["onMouseWheel"]["fn"]

	@onMouseWheel.setter
	def onMouseWheel(self,fn):
		JsonData = {"api": "RenderControl.RcMouseWheel","EventName": ""}
		if type(fn).__name__ == "function":
			self.Events["onMouseWheel"]["fn"]= fn
			JsonData["EventName"] = "onMouseWheel"
		else:
			self.Events["onMouseWheel"]["fn"] = None
		wsObj.postMessage({ "propertyType":"onMouseWheel", "_HashCode": "" },None,JsonData,False)
		if fn:
			rcEvent=wsObj.getrcEvent()
			eventp1 = Event_onMouseWheel(rcEvent,fn,(self.Events["onMouseWheel"]["args"]),"onMouseWheel")
			eventp1.start()
	@property
	def onObjectEditFinish(self):
		return self.Events["onObjectEditFinish"]["fn"]

	@onObjectEditFinish.setter
	def onObjectEditFinish(self,fn):
		JsonData = {"api": "RenderControl.RcObjectEditFinish","EventName": ""}
		if type(fn).__name__ == "function":
			self.Events["onObjectEditFinish"]["fn"]= fn
			JsonData["EventName"] = "onObjectEditFinish"
		else:
			self.Events["onObjectEditFinish"]["fn"] = None
		wsObj.postMessage({ "propertyType":"onObjectEditFinish", "_HashCode": "" },None,JsonData,False)
		rcEvent=wsObj.getrcEvent()
		eventp1 = Event_onObjectEditFinish(rcEvent, fn, (), "onObjectEditFinish")
		eventp1.start()
	@property
	def onObjectEditing(self):
		return self.Events["onObjectEditing"]["fn"]

	@onObjectEditing.setter
	def onObjectEditing(self,fn):
		JsonData = {"api": "RenderControl.RcObjectEditing","EventName": ""}
		if type(fn).__name__ == "function":
			self.Events["onObjectEditing"]["fn"]= fn
			JsonData["EventName"] = "onObjectEditing"
		else:
			self.Events["onObjectEditing"]["fn"] = None
		wsObj.postMessage({ "propertyType":"onObjectEditing", "_HashCode": "" },None,JsonData,False)
		if fn:
			rcEvent=wsObj.getrcEvent()
			eventp1 = Event_onObjectEditing(rcEvent,fn,(self.Events["onObjectEditing"]["args"]),"onObjectEditing")
			eventp1.start()
	@property
	def onPictureExportBegin(self):
		return self.Events["onPictureExportBegin"]["fn"]

	@onPictureExportBegin.setter
	def onPictureExportBegin(self,fn):
		JsonData = {"api": "RenderControl.RcPictureExportBegin","EventName": ""}
		if type(fn).__name__ == "function":
			self.Events["onPictureExportBegin"]["fn"]= fn
			JsonData["EventName"] = "onPictureExportBegin"
		else:
			self.Events["onPictureExportBegin"]["fn"] = None
		wsObj.postMessage({ "propertyType":"onPictureExportBegin", "_HashCode": "" },None,JsonData,False)
		if fn:
			rcEvent=wsObj.getrcEvent()
			eventp1 = Event_onPictureExportBegin(rcEvent,fn,(self.Events["onPictureExportBegin"]["args"]),"onPictureExportBegin")
			eventp1.start()
	@property
	def onPictureExportEnd(self):
		return self.Events["onPictureExportEnd"]["fn"]

	@onPictureExportEnd.setter
	def onPictureExportEnd(self,fn):
		JsonData = {"api": "RenderControl.RcPictureExportEnd","EventName": ""}
		if type(fn).__name__ == "function":
			self.Events["onPictureExportEnd"]["fn"]= fn
			JsonData["EventName"] = "onPictureExportEnd"
		else:
			self.Events["onPictureExportEnd"]["fn"] = None
		wsObj.postMessage({ "propertyType":"onPictureExportEnd", "_HashCode": "" },None,JsonData,False)
		if fn:
			rcEvent=wsObj.getrcEvent()
			eventp1 = Event_onPictureExportEnd(rcEvent,fn,(self.Events["onPictureExportEnd"]["args"]),"onPictureExportEnd")
			eventp1.start()
	@property
	def onPictureExporting(self):
		return self.Events["onPictureExporting"]["fn"]

	@onPictureExporting.setter
	def onPictureExporting(self,fn):
		JsonData = {"api": "RenderControl.RcPictureExporting","EventName": ""}
		if type(fn).__name__ == "function":
			self.Events["onPictureExporting"]["fn"]= fn
			JsonData["EventName"] = "onPictureExporting"
		else:
			self.Events["onPictureExporting"]["fn"] = None
		wsObj.postMessage({ "propertyType":"onPictureExporting", "_HashCode": "" },None,JsonData,False)
		if fn:
			rcEvent=wsObj.getrcEvent()
			eventp1 = Event_onPictureExporting(rcEvent,fn,(self.Events["onPictureExporting"]["args"]),"onPictureExporting")
			eventp1.start()
	@property
	def onPresentationFlyToReachedDestination(self):
		return self.Events["onPresentationFlyToReachedDestination"]["fn"]

	@onPresentationFlyToReachedDestination.setter
	def onPresentationFlyToReachedDestination(self,fn):
		JsonData = {"api": "RenderControl.RcPresentationFlyToReachedDestination","EventName": ""}
		if type(fn).__name__ == "function":
			self.Events["onPresentationFlyToReachedDestination"]["fn"]= fn
			JsonData["EventName"] = "onPresentationFlyToReachedDestination"
		else:
			self.Events["onPresentationFlyToReachedDestination"]["fn"] = None
		wsObj.postMessage({ "propertyType":"onPresentationFlyToReachedDestination", "_HashCode": "" },None,JsonData,False)
		if fn:
			rcEvent=wsObj.getrcEvent()
			eventp1 = Event_onPresentationFlyToReachedDestination(rcEvent,fn,(self.Events["onPresentationFlyToReachedDestination"]["args"]),"onPresentationFlyToReachedDestination")
			eventp1.start()
	@property
	def onPresentationStatusChanged(self):
		return self.Events["onPresentationStatusChanged"]["fn"]

	@onPresentationStatusChanged.setter
	def onPresentationStatusChanged(self,fn):
		JsonData = {"api": "RenderControl.RcPresentationStatusChanged","EventName": ""}
		if type(fn).__name__ == "function":
			self.Events["onPresentationStatusChanged"]["fn"]= fn
			JsonData["EventName"] = "onPresentationStatusChanged"
		else:
			self.Events["onPresentationStatusChanged"]["fn"] = None
		wsObj.postMessage({ "propertyType":"onPresentationStatusChanged", "_HashCode": "" },None,JsonData,False)
		if fn:
			rcEvent=wsObj.getrcEvent()
			eventp1 = Event_onPresentationStatusChanged(rcEvent,fn,(self.Events["onPresentationStatusChanged"]["args"]),"onPresentationStatusChanged")
			eventp1.start()
	@property
	def onProjectChanged(self):
		return self.Events["onProjectChanged"]["fn"]

	@onProjectChanged.setter
	def onProjectChanged(self,fn):
		JsonData = {"api": "RenderControl.RcProjectChanged","EventName": ""}
		if type(fn).__name__ == "function":
			self.Events["onProjectChanged"]["fn"]= fn
			JsonData["EventName"] = "onProjectChanged"
		else:
			self.Events["onProjectChanged"]["fn"] = None
		wsObj.postMessage({ "propertyType":"onProjectChanged", "_HashCode": "" },None,JsonData,False)
		rcEvent=wsObj.getrcEvent()
		eventp1 = Event_onProjectChanged(rcEvent, fn, (), "onProjectChanged")
		eventp1.start()
	@property
	def onRButtonDblClk(self):
		return self.Events["onRButtonDblClk"]["fn"]

	@onRButtonDblClk.setter
	def onRButtonDblClk(self,fn):
		JsonData = {"api": "RenderControl.RcRButtonDblClk","EventName": ""}
		if type(fn).__name__ == "function":
			self.Events["onRButtonDblClk"]["fn"]= fn
			JsonData["EventName"] = "onRButtonDblClk"
		else:
			self.Events["onRButtonDblClk"]["fn"] = None
		wsObj.postMessage({ "propertyType":"onRButtonDblClk", "_HashCode": "" },None,JsonData,False)
		if fn:
			rcEvent=wsObj.getrcEvent()
			eventp1 = Event_onRButtonDblClk(rcEvent,fn,(self.Events["onRButtonDblClk"]["args"]),"onRButtonDblClk")
			eventp1.start()
	@property
	def onRButtonDown(self):
		return self.Events["onRButtonDown"]["fn"]

	@onRButtonDown.setter
	def onRButtonDown(self,fn):
		JsonData = {"api": "RenderControl.RcRButtonDown","EventName": ""}
		if type(fn).__name__ == "function":
			self.Events["onRButtonDown"]["fn"]= fn
			JsonData["EventName"] = "onRButtonDown"
		else:
			self.Events["onRButtonDown"]["fn"] = None
		wsObj.postMessage({ "propertyType":"onRButtonDown", "_HashCode": "" },None,JsonData,False)
		if fn:
			rcEvent=wsObj.getrcEvent()
			eventp1 = Event_onRButtonDown(rcEvent,fn,(self.Events["onRButtonDown"]["args"]),"onRButtonDown")
			eventp1.start()
	@property
	def onRButtonUp(self):
		return self.Events["onRButtonUp"]["fn"]

	@onRButtonUp.setter
	def onRButtonUp(self,fn):
		JsonData = {"api": "RenderControl.RcRButtonUp","EventName": ""}
		if type(fn).__name__ == "function":
			self.Events["onRButtonUp"]["fn"]= fn
			JsonData["EventName"] = "onRButtonUp"
		else:
			self.Events["onRButtonUp"]["fn"] = None
		wsObj.postMessage({ "propertyType":"onRButtonUp", "_HashCode": "" },None,JsonData,False)
		if fn:
			rcEvent=wsObj.getrcEvent()
			eventp1 = Event_onRButtonUp(rcEvent,fn,(self.Events["onRButtonUp"]["args"]),"onRButtonUp")
			eventp1.start()
	@property
	def onResPacking(self):
		return self.Events["onResPacking"]["fn"]

	@onResPacking.setter
	def onResPacking(self,fn):
		JsonData = {"api": "RenderControl.RcResPacking","EventName": ""}
		if type(fn).__name__ == "function":
			self.Events["onResPacking"]["fn"]= fn
			JsonData["EventName"] = "onResPacking"
		else:
			self.Events["onResPacking"]["fn"] = None
		wsObj.postMessage({ "propertyType":"onResPacking", "_HashCode": "" },None,JsonData,False)
		if fn:
			rcEvent=wsObj.getrcEvent()
			eventp1 = Event_onResPacking(rcEvent,fn,(self.Events["onResPacking"]["args"]),"onResPacking")
			eventp1.start()
	@property
	def onTransformHelperBegin(self):
		return self.Events["onTransformHelperBegin"]["fn"]

	@onTransformHelperBegin.setter
	def onTransformHelperBegin(self,fn):
		JsonData = {"api": "RenderControl.RcTransformHelperBegin","EventName": ""}
		if type(fn).__name__ == "function":
			self.Events["onTransformHelperBegin"]["fn"]= fn
			JsonData["EventName"] = "onTransformHelperBegin"
		else:
			self.Events["onTransformHelperBegin"]["fn"] = None
		wsObj.postMessage({ "propertyType":"onTransformHelperBegin", "_HashCode": "" },None,JsonData,False)
		rcEvent=wsObj.getrcEvent()
		eventp1 = Event_onTransformHelperBegin(rcEvent, fn, (), "onTransformHelperBegin")
		eventp1.start()
	@property
	def onTransformHelperBoxScaling(self):
		return self.Events["onTransformHelperBoxScaling"]["fn"]

	@onTransformHelperBoxScaling.setter
	def onTransformHelperBoxScaling(self,fn):
		JsonData = {"api": "RenderControl.RcTransformHelperBoxScaling","EventName": ""}
		if type(fn).__name__ == "function":
			self.Events["onTransformHelperBoxScaling"]["fn"]= fn
			JsonData["EventName"] = "onTransformHelperBoxScaling"
		else:
			self.Events["onTransformHelperBoxScaling"]["fn"] = None
		wsObj.postMessage({ "propertyType":"onTransformHelperBoxScaling", "_HashCode": "" },None,JsonData,False)
		if fn:
			rcEvent=wsObj.getrcEvent()
			eventp1 = Event_onTransformHelperBoxScaling(rcEvent,fn,(self.Events["onTransformHelperBoxScaling"]["args"]),"onTransformHelperBoxScaling")
			eventp1.start()
	@property
	def onTransformHelperEnd(self):
		return self.Events["onTransformHelperEnd"]["fn"]

	@onTransformHelperEnd.setter
	def onTransformHelperEnd(self,fn):
		JsonData = {"api": "RenderControl.RcTransformHelperEnd","EventName": ""}
		if type(fn).__name__ == "function":
			self.Events["onTransformHelperEnd"]["fn"]= fn
			JsonData["EventName"] = "onTransformHelperEnd"
		else:
			self.Events["onTransformHelperEnd"]["fn"] = None
		wsObj.postMessage({ "propertyType":"onTransformHelperEnd", "_HashCode": "" },None,JsonData,False)
		rcEvent=wsObj.getrcEvent()
		eventp1 = Event_onTransformHelperEnd(rcEvent, fn, (), "onTransformHelperEnd")
		eventp1.start()
	@property
	def onTransformHelperMoving(self):
		return self.Events["onTransformHelperMoving"]["fn"]

	@onTransformHelperMoving.setter
	def onTransformHelperMoving(self,fn):
		JsonData = {"api": "RenderControl.RcTransformHelperMoving","EventName": ""}
		if type(fn).__name__ == "function":
			self.Events["onTransformHelperMoving"]["fn"]= fn
			JsonData["EventName"] = "onTransformHelperMoving"
		else:
			self.Events["onTransformHelperMoving"]["fn"] = None
		wsObj.postMessage({ "propertyType":"onTransformHelperMoving", "_HashCode": "" },None,JsonData,False)
		if fn:
			rcEvent=wsObj.getrcEvent()
			eventp1 = Event_onTransformHelperMoving(rcEvent,fn,(self.Events["onTransformHelperMoving"]["args"]),"onTransformHelperMoving")
			eventp1.start()
	@property
	def onTransformHelperRotating(self):
		return self.Events["onTransformHelperRotating"]["fn"]

	@onTransformHelperRotating.setter
	def onTransformHelperRotating(self,fn):
		JsonData = {"api": "RenderControl.RcTransformHelperRotating","EventName": ""}
		if type(fn).__name__ == "function":
			self.Events["onTransformHelperRotating"]["fn"]= fn
			JsonData["EventName"] = "onTransformHelperRotating"
		else:
			self.Events["onTransformHelperRotating"]["fn"] = None
		wsObj.postMessage({ "propertyType":"onTransformHelperRotating", "_HashCode": "" },None,JsonData,False)
		if fn:
			rcEvent=wsObj.getrcEvent()
			eventp1 = Event_onTransformHelperRotating(rcEvent,fn,(self.Events["onTransformHelperRotating"]["args"]),"onTransformHelperRotating")
			eventp1.start()
	@property
	def onTransformHelperScaling(self):
		return self.Events["onTransformHelperScaling"]["fn"]

	@onTransformHelperScaling.setter
	def onTransformHelperScaling(self,fn):
		JsonData = {"api": "RenderControl.RcTransformHelperScaling","EventName": ""}
		if type(fn).__name__ == "function":
			self.Events["onTransformHelperScaling"]["fn"]= fn
			JsonData["EventName"] = "onTransformHelperScaling"
		else:
			self.Events["onTransformHelperScaling"]["fn"] = None
		wsObj.postMessage({ "propertyType":"onTransformHelperScaling", "_HashCode": "" },None,JsonData,False)
		if fn:
			rcEvent=wsObj.getrcEvent()
			eventp1 = Event_onTransformHelperScaling(rcEvent,fn,(self.Events["onTransformHelperScaling"]["args"]),"onTransformHelperScaling")
			eventp1.start()
	@property
	def onUIWindowEvent(self):
		return self.Events["onUIWindowEvent"]["fn"]

	@onUIWindowEvent.setter
	def onUIWindowEvent(self,fn):
		JsonData = {"api": "RenderControl.RcUIWindowEvent","EventName": ""}
		if type(fn).__name__ == "function":
			self.Events["onUIWindowEvent"]["fn"]= fn
			JsonData["EventName"] = "onUIWindowEvent"
		else:
			self.Events["onUIWindowEvent"]["fn"] = None
		wsObj.postMessage({ "propertyType":"onUIWindowEvent", "_HashCode": "" },None,JsonData,False)
		if fn:
			rcEvent=wsObj.getrcEvent()
			eventp1 = Event_onUIWindowEvent(rcEvent,fn,(self.Events["onUIWindowEvent"]["args"]),"onUIWindowEvent")
			eventp1.start()
	@property
	def onVideoExportBegin(self):
		return self.Events["onVideoExportBegin"]["fn"]

	@onVideoExportBegin.setter
	def onVideoExportBegin(self,fn):
		JsonData = {"api": "RenderControl.RcVideoExportBegin","EventName": ""}
		if type(fn).__name__ == "function":
			self.Events["onVideoExportBegin"]["fn"]= fn
			JsonData["EventName"] = "onVideoExportBegin"
		else:
			self.Events["onVideoExportBegin"]["fn"] = None
		wsObj.postMessage({ "propertyType":"onVideoExportBegin", "_HashCode": "" },None,JsonData,False)
		if fn:
			rcEvent=wsObj.getrcEvent()
			eventp1 = Event_onVideoExportBegin(rcEvent,fn,(self.Events["onVideoExportBegin"]["args"]),"onVideoExportBegin")
			eventp1.start()
	@property
	def onVideoExportEnd(self):
		return self.Events["onVideoExportEnd"]["fn"]

	@onVideoExportEnd.setter
	def onVideoExportEnd(self,fn):
		JsonData = {"api": "RenderControl.RcVideoExportEnd","EventName": ""}
		if type(fn).__name__ == "function":
			self.Events["onVideoExportEnd"]["fn"]= fn
			JsonData["EventName"] = "onVideoExportEnd"
		else:
			self.Events["onVideoExportEnd"]["fn"] = None
		wsObj.postMessage({ "propertyType":"onVideoExportEnd", "_HashCode": "" },None,JsonData,False)
		if fn:
			rcEvent=wsObj.getrcEvent()
			eventp1 = Event_onVideoExportEnd(rcEvent,fn,(self.Events["onVideoExportEnd"]["args"]),"onVideoExportEnd")
			eventp1.start()
	@property
	def onVideoExporting(self):
		return self.Events["onVideoExporting"]["fn"]

	@onVideoExporting.setter
	def onVideoExporting(self,fn):
		JsonData = {"api": "RenderControl.RcVideoExporting","EventName": ""}
		if type(fn).__name__ == "function":
			self.Events["onVideoExporting"]["fn"]= fn
			JsonData["EventName"] = "onVideoExporting"
		else:
			self.Events["onVideoExporting"]["fn"] = None
		wsObj.postMessage({ "propertyType":"onVideoExporting", "_HashCode": "" },None,JsonData,False)
		if fn:
			rcEvent=wsObj.getrcEvent()
			eventp1 = Event_onVideoExporting(rcEvent,fn,(self.Events["onVideoExporting"]["args"]),"onVideoExporting")
			eventp1.start()
