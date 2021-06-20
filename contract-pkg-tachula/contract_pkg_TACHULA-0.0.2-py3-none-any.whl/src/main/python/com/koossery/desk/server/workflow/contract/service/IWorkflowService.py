from ..dto.ResultDTO import ResultDTO
from ..exceptions.WorkflowServerException import WorkflowSeverException


class IWorkflowService:

    def find(toolID: str) -> []:
        raise WorkflowSeverException
        pass

    def run(toolID: str, workflowID: str, ImageID) -> ResultDTO:
        raise WorkflowSeverException
        pass
