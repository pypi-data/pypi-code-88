from ..dto.ToolDTO import ToolDTO
from ..exceptions.ToolServerException import ToolSeverException


class IToolService:

    def find(self, name:str) -> []:
        raise ToolSeverException
        pass
