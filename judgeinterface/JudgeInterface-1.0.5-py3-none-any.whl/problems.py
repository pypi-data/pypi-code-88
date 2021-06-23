from typing import Dict
from .abstract import AbstractInterface
import json

class ProblemsInterface(AbstractInterface):
    def __init__(self, cur) -> None:
        super().__init__(cur)
        self.create_fields = ['title', 'description', 'max_cpu_time', 'max_real_time', 'max_memory', 'author', 'testcases']
        self.retrieve_fields = ['id', 'title', 'description', 'max_cpu_time', 'max_real_time', 'max_memory', 'author', 'testcases']
        self.update_fields = ['description', 'max_cpu_time', 'max_real_time', 'max_memory', 'testcases']
        self.table_name = 'judge.PROBLEMS'

    def create(self, **data: Dict):
        if 'testcases' in data:
            testcases = data.get('testcases')
            data['testcases'] = json.dumps(testcases)
            
        return super().create(**data)

    def update(self, id: int, **data: Dict):
        if 'testcases' in data:
            testcases = data.get('testcases')
            data['testcases'] = json.dumps(testcases)
        
        return super().update(id, **data)
