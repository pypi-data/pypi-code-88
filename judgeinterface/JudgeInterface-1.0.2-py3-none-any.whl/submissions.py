import json
from typing import Dict
from .abstract import AbstractInterface

class SubmissionsInterface(AbstractInterface):
    def __init__(self, cur):
        super().__init__(cur)
        self.create_fields = ['user_id', 'problem_id', 'code', 'language', 'result']
        self.retrieve_fields = ['id', 'user_id', 'problem_id', 'code', 'language', 'result']
        self.update_fields = self.create_fields
        self.table_name = 'judge.SUBMISSIONS'

        def create(self, **data: Dict):
            if 'result' in data:
                result = data.get('result')
                data['result'] = json.dumps(result)

            return super().create(**data)

        def update(self, id: int, **data: Dict):
            if 'result' in data:
                result = data.get('result')
                data['result'] = json.dumps(result)
                
            return super().update(id, **data)
