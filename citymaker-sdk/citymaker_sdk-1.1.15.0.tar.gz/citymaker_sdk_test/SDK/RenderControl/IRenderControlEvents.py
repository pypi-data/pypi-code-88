import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.SocketApiServe as socketApi
import Utils.classmake as CM
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
	#def __init__(self,args):
		#CM.AddRenderEventCB(self.Events)
		#CM.AddRenderEvent(self, self.Events)
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
		r=socketApi.postMessage({ "propertyType":"onAsyncSearchFinished", "_HashCode": "" },None,JsonData)
		CM.AddRenderEventCB(fn,"onAsyncSearchFinished",self.Events["onAsyncSearchFinished"]["args"])
		socketApi.start()
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
		r=socketApi.postMessage({ "propertyType":"onBeforePresentationItemActivation", "_HashCode": "" },None,JsonData)
		CM.AddRenderEventCB(fn,"onBeforePresentationItemActivation",self.Events["onBeforePresentationItemActivation"]["args"])
		socketApi.start()
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
		r=socketApi.postMessage({ "propertyType":"onCameraChanged", "_HashCode": "" },None,JsonData)
		CM.AddRenderEventCB(fn,"onCameraChanged",self.Events["onCameraChanged"]["args"])
		socketApi.start()
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
		r=socketApi.postMessage({ "propertyType":"onCameraFlyFinished", "_HashCode": "" },None,JsonData)
		CM.AddRenderEventCB(fn,"onCameraFlyFinished",self.Events["onCameraFlyFinished"]["args"])
		socketApi.start()
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
		r=socketApi.postMessage({ "propertyType":"onCameraTourWaypointChanged", "_HashCode": "" },None,JsonData)
		CM.AddRenderEventCB(fn,"onCameraTourWaypointChanged",self.Events["onCameraTourWaypointChanged"]["args"])
		socketApi.start()
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
		r=socketApi.postMessage({ "propertyType":"onCameraUndoRedoStatusChanged", "_HashCode": "" },None,JsonData)
		AddRenderEventCB(fn)
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
		r=socketApi.postMessage({ "propertyType":"onDataSourceDisconnected", "_HashCode": "" },None,JsonData)
		CM.AddRenderEventCB(fn,"onDataSourceDisconnected",self.Events["onDataSourceDisconnected"]["args"])
		socketApi.start()
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
		r=socketApi.postMessage({ "propertyType":"onFeaturesMoving", "_HashCode": "" },None,JsonData)
		CM.AddRenderEventCB(fn,"onFeaturesMoving",self.Events["onFeaturesMoving"]["args"])
		socketApi.start()
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
		r=socketApi.postMessage({ "propertyType":"onFrame", "_HashCode": "" },None,JsonData)
		CM.AddRenderEventCB(fn,"onFrame",self.Events["onFrame"]["args"])
		socketApi.start()
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
		r=socketApi.postMessage({ "propertyType":"onFullScreenChanged", "_HashCode": "" },None,JsonData)
		CM.AddRenderEventCB(fn,"onFullScreenChanged",self.Events["onFullScreenChanged"]["args"])
		socketApi.start()
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
		r=socketApi.postMessage({ "propertyType":"onInteractFocusChanged", "_HashCode": "" },None,JsonData)
		CM.AddRenderEventCB(fn,"onInteractFocusChanged",self.Events["onInteractFocusChanged"]["args"])
		socketApi.start()
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
		r=socketApi.postMessage({ "propertyType":"onKeyDown", "_HashCode": "" },None,JsonData)
		CM.AddRenderEventCB(fn,"onKeyDown",self.Events["onKeyDown"]["args"])
		socketApi.start()
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
		r=socketApi.postMessage({ "propertyType":"onKeyUp", "_HashCode": "" },None,JsonData)
		CM.AddRenderEventCB(fn,"onKeyUp",self.Events["onKeyUp"]["args"])
		socketApi.start()
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
		r=socketApi.postMessage({ "propertyType":"onLButtonDblClk", "_HashCode": "" },None,JsonData)
		CM.AddRenderEventCB(fn,"onLButtonDblClk",self.Events["onLButtonDblClk"]["args"])
		socketApi.start()
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
		r=socketApi.postMessage({ "propertyType":"onLButtonDown", "_HashCode": "" },None,JsonData)
		CM.AddRenderEventCB(fn,"onLButtonDown",self.Events["onLButtonDown"]["args"])
		socketApi.start()
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
		r=socketApi.postMessage({ "propertyType":"onLButtonUp", "_HashCode": "" },None,JsonData)
		CM.AddRenderEventCB(fn,"onLButtonUp",self.Events["onLButtonUp"]["args"])
		socketApi.start()
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
		r=socketApi.postMessage({ "propertyType":"onMButtonDblClk", "_HashCode": "" },None,JsonData)
		CM.AddRenderEventCB(fn,"onMButtonDblClk",self.Events["onMButtonDblClk"]["args"])
		socketApi.start()
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
		r=socketApi.postMessage({ "propertyType":"onMButtonDown", "_HashCode": "" },None,JsonData)
		CM.AddRenderEventCB(fn,"onMButtonDown",self.Events["onMButtonDown"]["args"])
		socketApi.start()
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
		r=socketApi.postMessage({ "propertyType":"onMButtonUp", "_HashCode": "" },None,JsonData)
		CM.AddRenderEventCB(fn,"onMButtonUp",self.Events["onMButtonUp"]["args"])
		socketApi.start()
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
		r=socketApi.postMessage({ "propertyType":"onMouseClick", "_HashCode": "" },None,JsonData)
		CM.AddRenderEventCB(fn,"onMouseClick",self.Events["onMouseClick"]["args"])
		socketApi.start()
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
		r=socketApi.postMessage({ "propertyType":"onMouseClickSelect", "_HashCode": "" },None,JsonData)
		CM.AddRenderEventCB(fn,"onMouseClickSelect",self.Events["onMouseClickSelect"]["args"])
		socketApi.start()
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
		r=socketApi.postMessage({ "propertyType":"onMouseDragSelect", "_HashCode": "" },None,JsonData)
		CM.AddRenderEventCB(fn,"onMouseDragSelect",self.Events["onMouseDragSelect"]["args"])
		socketApi.start()
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
		r=socketApi.postMessage({ "propertyType":"onMouseHover", "_HashCode": "" },None,JsonData)
		CM.AddRenderEventCB(fn,"onMouseHover",self.Events["onMouseHover"]["args"])
		socketApi.start()
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
		r=socketApi.postMessage({ "propertyType":"onMouseMove", "_HashCode": "" },None,JsonData)
		CM.AddRenderEventCB(fn,"onMouseMove",self.Events["onMouseMove"]["args"])
		socketApi.start()
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
		r=socketApi.postMessage({ "propertyType":"onMouseWheel", "_HashCode": "" },None,JsonData)
		CM.AddRenderEventCB(fn,"onMouseWheel",self.Events["onMouseWheel"]["args"])
		socketApi.start()
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
		r=socketApi.postMessage({ "propertyType":"onObjectEditFinish", "_HashCode": "" },None,JsonData)
		AddRenderEventCB(fn)
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
		r=socketApi.postMessage({ "propertyType":"onObjectEditing", "_HashCode": "" },None,JsonData)
		CM.AddRenderEventCB(fn,"onObjectEditing",self.Events["onObjectEditing"]["args"])
		socketApi.start()
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
		r=socketApi.postMessage({ "propertyType":"onPictureExportBegin", "_HashCode": "" },None,JsonData)
		CM.AddRenderEventCB(fn,"onPictureExportBegin",self.Events["onPictureExportBegin"]["args"])
		socketApi.start()
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
		r=socketApi.postMessage({ "propertyType":"onPictureExportEnd", "_HashCode": "" },None,JsonData)
		CM.AddRenderEventCB(fn,"onPictureExportEnd",self.Events["onPictureExportEnd"]["args"])
		socketApi.start()
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
		r=socketApi.postMessage({ "propertyType":"onPictureExporting", "_HashCode": "" },None,JsonData)
		CM.AddRenderEventCB(fn,"onPictureExporting",self.Events["onPictureExporting"]["args"])
		socketApi.start()
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
		r=socketApi.postMessage({ "propertyType":"onPresentationFlyToReachedDestination", "_HashCode": "" },None,JsonData)
		CM.AddRenderEventCB(fn,"onPresentationFlyToReachedDestination",self.Events["onPresentationFlyToReachedDestination"]["args"])
		socketApi.start()
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
		r=socketApi.postMessage({ "propertyType":"onPresentationStatusChanged", "_HashCode": "" },None,JsonData)
		CM.AddRenderEventCB(fn,"onPresentationStatusChanged",self.Events["onPresentationStatusChanged"]["args"])
		socketApi.start()
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
		r=socketApi.postMessage({ "propertyType":"onProjectChanged", "_HashCode": "" },None,JsonData)
		AddRenderEventCB(fn)
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
		r=socketApi.postMessage({ "propertyType":"onRButtonDblClk", "_HashCode": "" },None,JsonData)
		CM.AddRenderEventCB(fn,"onRButtonDblClk",self.Events["onRButtonDblClk"]["args"])
		socketApi.start()
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
		r=socketApi.postMessage({ "propertyType":"onRButtonDown", "_HashCode": "" },None,JsonData)
		CM.AddRenderEventCB(fn,"onRButtonDown",self.Events["onRButtonDown"]["args"])
		socketApi.start()
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
		r=socketApi.postMessage({ "propertyType":"onRButtonUp", "_HashCode": "" },None,JsonData)
		CM.AddRenderEventCB(fn,"onRButtonUp",self.Events["onRButtonUp"]["args"])
		socketApi.start()
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
		r=socketApi.postMessage({ "propertyType":"onResPacking", "_HashCode": "" },None,JsonData)
		CM.AddRenderEventCB(fn,"onResPacking",self.Events["onResPacking"]["args"])
		socketApi.start()
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
		r=socketApi.postMessage({ "propertyType":"onTransformHelperBegin", "_HashCode": "" },None,JsonData)
		AddRenderEventCB(fn)
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
		r=socketApi.postMessage({ "propertyType":"onTransformHelperBoxScaling", "_HashCode": "" },None,JsonData)
		CM.AddRenderEventCB(fn,"onTransformHelperBoxScaling",self.Events["onTransformHelperBoxScaling"]["args"])
		socketApi.start()
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
		r=socketApi.postMessage({ "propertyType":"onTransformHelperEnd", "_HashCode": "" },None,JsonData)
		AddRenderEventCB(fn)
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
		r=socketApi.postMessage({ "propertyType":"onTransformHelperMoving", "_HashCode": "" },None,JsonData)
		CM.AddRenderEventCB(fn,"onTransformHelperMoving",self.Events["onTransformHelperMoving"]["args"])
		socketApi.start()
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
		r=socketApi.postMessage({ "propertyType":"onTransformHelperRotating", "_HashCode": "" },None,JsonData)
		CM.AddRenderEventCB(fn,"onTransformHelperRotating",self.Events["onTransformHelperRotating"]["args"])
		socketApi.start()
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
		r=socketApi.postMessage({ "propertyType":"onTransformHelperScaling", "_HashCode": "" },None,JsonData)
		CM.AddRenderEventCB(fn,"onTransformHelperScaling",self.Events["onTransformHelperScaling"]["args"])
		socketApi.start()
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
		r=socketApi.postMessage({ "propertyType":"onUIWindowEvent", "_HashCode": "" },None,JsonData)
		CM.AddRenderEventCB(fn,"onUIWindowEvent",self.Events["onUIWindowEvent"]["args"])
		socketApi.start()
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
		r=socketApi.postMessage({ "propertyType":"onVideoExportBegin", "_HashCode": "" },None,JsonData)
		CM.AddRenderEventCB(fn,"onVideoExportBegin",self.Events["onVideoExportBegin"]["args"])
		socketApi.start()
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
		r=socketApi.postMessage({ "propertyType":"onVideoExportEnd", "_HashCode": "" },None,JsonData)
		CM.AddRenderEventCB(fn,"onVideoExportEnd",self.Events["onVideoExportEnd"]["args"])
		socketApi.start()
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
		r=socketApi.postMessage({ "propertyType":"onVideoExporting", "_HashCode": "" },None,JsonData)
		CM.AddRenderEventCB(fn,"onVideoExporting",self.Events["onVideoExporting"]["args"])
		socketApi.start()
