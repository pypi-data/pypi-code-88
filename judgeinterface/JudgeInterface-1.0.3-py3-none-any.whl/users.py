from typing import Dict
from .abstract import AbstractInterface
import bcrypt

class UsersInterface(AbstractInterface):
    def __init__(self, cur):
        super().__init__(cur)
        self.create_fields = ['username', 'password', 'email']
        self.retrieve_fields = ['id', 'username', 'email']
        self.update_fields = ['password', 'email']
        self.table_name = 'judge.USERS'

    def create(self, **data: Dict):
        if 'password' in data:
            password = data.get('password')
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            data['password'] = hashed_password.decode()
        
        return super().create(**data)

    def update(self, id: int, **data: Dict):
        if 'password' in data:
            password = data.get('password')
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            data['password'] = hashed_password.decode()
            
        return super().update(id, **data)
