import os

class PathProxy:
    """
    path define here
    """
    app_path = r"d:\\FastCNN\\"
    project_path = app_path + r"Projects\\"
    def getConfigPath():
        return PathProxy.app_path + r"Config\Config.json"
    
    def getProjectDir(projectname):
        return os.path.join(PathProxy.project_path , projectname )+"\\"
    
    def getSettingPath(projectname):
        return PathProxy.getProjectDir(projectname) + 'Setting.json'
    
    def getProjectTrainDir(projectname):
        return PathProxy.getProjectDir(projectname) + "train" + "\\"
    
    def getProjectTestDir(projectname):
        return PathProxy.getProjectDir(projectname) + "test" + "\\"
    
    def getClassDir(projectname,classname):
        return PathProxy.getProjectDir(projectname) + classname + "\\"
        
    def getModelDir(projectname):
        return os.path.join(PathProxy.getProjectDir(projectname) , "models\\")
    
    def getModelTagDir(projectname,tag):
        return os.path.join(PathProxy.getModelDir(projectname) , tag)
        
    def getModelParamPath(projectname,tag):
        return os.path.join(PathProxy.getModelTagDir(projectname,tag) , 'Param.json')
        
    def getProjectNames():
        return os.listdir(PathProxy.project_path)
    
    def getProjectTags(projectname):
        return os.listdir(os.path.join(PathProxy.project_path,projectname,"models"))
    
    def getTrainLogPath(projectname,tag):
        return os.path.join(PathProxy.getModelTagDir(projectname,tag) , 'tpv.csv')
    
    def getSaverPath(projectname,tag):
        return os.path.join(PathProxy.getModelTagDir(projectname,tag) , "ckpt","save.ckpt")
    
    """
    method here
    """
    def mkdir(dir):
        if os.path.exists(dir):
            return
        os.makedirs(dir)
        pass