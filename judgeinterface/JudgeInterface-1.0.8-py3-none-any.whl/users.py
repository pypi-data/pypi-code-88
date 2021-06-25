from typing import Dict
from .abstract import AbstractInterface
import bcrypt


class UsersInterface(AbstractInterface):
    create_fields = ['username', 'password', 'email']
    retrieve_fields = ['id', 'username', 'email']
    update_fields = ['password', 'email']
    table_name = 'judge.USERS'

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
