from flask_restful import Resource
from flask import request
from FastCNN.prx.GongDaProxy import predictSingle
from FastCNN.prx.PathProxy import PathProxy

class FastCNNApi(Resource):
    
    
    def getStatus():
        rtn = {'success':False}
        
        
        rtn['success'] = True
        return rtn
    
    def getProjectNames():
        rtn = {'success':False}
        
        data = PathProxy.getProjectNames()
        rtn['data'] = data
        
        rtn['success'] = True
        return rtn
    
    def getProjectTags():
        rtn = {'success':False}
        
        data = PathProxy.getProjectTags("GongDa")
        rtn['data'] = data
        rtn['success'] = True
        
        return rtn
    
    def testPicture():
        rtn = {'success':False}
        imagepath = request.form.get("imagepath")
        if not imagepath:
            rtn["error"] = "imagepath is nesserary"
            return rtn
        
        modeltag = request.form.get("modeltag")
        if not modeltag:
            rtn["error"] = "imagepath is nesserary"
            return rtn
        try:
            data = predictSingle(imagepath,modeltag)
        except Exception as err:
            rtn['data'] = str(err)
            return rtn
        rtn['data'] = data
        rtn['success'] = True
        return rtn
    
    def post(self):
        _cmd = request.form.get('cmd')
        
        if _cmd == "getProjectNames":
            return FastCNNApi.getProjectNames()
        
        if _cmd == "getProjectTags":
            return FastCNNApi.getProjectTags()
        
        if _cmd == "testPicture":
            return FastCNNApi.testPicture()
