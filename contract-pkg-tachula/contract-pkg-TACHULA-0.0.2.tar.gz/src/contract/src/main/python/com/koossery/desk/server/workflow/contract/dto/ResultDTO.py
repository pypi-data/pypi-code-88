class ResultDTO():

    def __init__(self,toolID, workflowID,accuracy,results):

        self.toolID = toolID
        self.workflowID = workflowID
        self.accuracy = accuracy
        self.results=results

    def getToolID(self):
        return self.toolID

    def getWorkflowID(self):
        return self.workflowID

    def getAccuracy(self):
        return self.Accuracy

    def getResults(self):
        return self.results
