from typing import Dict
from .abstract import AbstractInterface
import json

class ProblemsInterface(AbstractInterface):
    create_fields = ['title', 'description', 'max_cpu_time', 'max_real_time', 'max_memory', 'author', 'testcases']
    retrieve_fields = ['id', 'title', 'description', 'max_cpu_time', 'max_real_time', 'max_memory', 'author', 'testcases']
    update_fields = ['description', 'max_cpu_time', 'max_real_time', 'max_memory', 'testcases']
    table_name = 'judge.PROBLEMS'

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
