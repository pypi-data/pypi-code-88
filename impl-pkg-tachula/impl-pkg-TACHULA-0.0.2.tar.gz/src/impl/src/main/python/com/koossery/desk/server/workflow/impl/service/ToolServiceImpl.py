from src.contract.src.main import \
    ToolSeverException
from src.contract.src.main import IToolService
from ..sisv.WorkflowServerConstants import WorkflowServerConstants
import logging
logger = logging.getLogger('my_log')

class ToolServiceImpl(IToolService):
    def find(name) :
        if name is None:
            id="KOOSSERYDESKTOOLSVCO-001"
            message= WorkflowServerConstants.getMessage(id,WorkflowServerConstants.workflowServiceMessagePath)
            e = ToolSeverException(id,message)
            logger.error(e.__dict__)
            raise e

        return [{"credential": None,"lazyLoadArrayList":None,"propertiesModified":[],"id":"789","name":"Disease Banana","description":"GoodBye","images":[]},{"credential":None,"lazyLoadArrayList":None,"propertiesModified":[],"id":"123","name":"Disease Tomato","description":"Hello","images":[]}]
