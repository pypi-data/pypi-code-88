from typing import Dict, List
from .lib.placeholder import Placeholder


class AbstractInterface:
    """
    AbstractInterface를 상속받아 새 DB Model의 Interface를 만들 수 있습니다. 
    """
    def __init__(self, cur):
        """
        cur은 DB Connector의 cursor입니다. 또한 해당 함수를 오버라이드하여 다음의 Instance Variable을 정의할 수 있습니다.
        1. self.create_fields
            INSERT할 때 필수적으로 필요한 Fields를 List로 정의할 수 있습니다.
        2. self.retrieve_fields
            SELECT할 때 필요한 Fields를 List로 정의할 수 있습니다.
        3. self.update_fields
            UPDATE할 때 필수적으로 필요한 Fields를 List로 정의할 수 있습니다.
        4. self.table_name
            액세스할 테이블의 이름을 str로 정의할 수 있습니다.
        """
        self.cur = cur

    def perform_create(self, **data: Dict) -> Dict:
        """data를 self.table_name 테이블에 추가합니다."""
        keys = set(data.keys())
        unknown_fields = keys - set(self.create_fields)
        if len(unknown_fields) > 0:
            # TODO: 허용되지 않은 fields 출력.
            raise AttributeError(f'{str(unknown_fields)} field(s) is(are) not allowed')

        valid_fields = [key for key in self.create_fields if key in data] # TODO: self.create_fields를 valid_fields로 바꾸는 것을 검토하기.
        # if len(valid_fields) <= 0:
        #     # TODO: mariadb.IntegrityError를 발생하게끔 해당 조건 없애기.
        #     return None
        query_fields = ', '.join(valid_fields)
        fields_values = tuple(data.get(key) for key in self.create_fields if key in data) # self.create_fields를 valid_fields로 바꿔도 무방.

        self.cur.execute(
            f'''
            INSERT INTO
            {self.table_name}({query_fields})
            VALUES({Placeholder.for_create_query(len(fields_values))})
            '''
            , fields_values
        )

        context = {key: data.get(key) for key in self.retrieve_fields} # self.create_fields를 self.retrieve_fields로 변경.
        context['id'] = self.cur.lastrowid

        return context

    def perform_retrieve(self, id: int = None, fields: List[str] = []):
        """
        id가 지정될 경우 해당하는 한 튜플을, 주어지지 않을 경우 전체 튜플을 SELECT합니다. fields는 속성을 프로젝션할 수 있습니다. 주어지지 않을 경우 전체를 프로젝션합니다.
        """
        unknown_fields = set(fields) - set(self.retrieve_fields)
        if len(unknown_fields) > 0:
            raise AttributeError(f'{str(unknown_fields)} field(s) is(are) not allowed')
        
        if fields == []:
            fields = self.retrieve_fields

        placeholder = Placeholder.for_select_query(self.retrieve_fields, fields)
        if placeholder == '': return
        if id == None:
            self.cur.execute(
                f'''
                SELECT {placeholder}
                FROM {self.table_name}
                '''
            )
            lst = self.cur.fetchall()
            return lst

        else:
            self.cur.execute(
                f'''
                SELECT {placeholder}
                FROM {self.table_name}
                WHERE id = ?
                ''',
                (id,)
            )
            row = self.cur.fetchone()
            if not row: return None
            return row

    def perform_update(self, id: int, **data: Dict) -> Dict:
        """
        id로 지정되는 한 튜플을 data로 갱신합니다.
        """
        keys = set(data.keys())
        unknown_fields = keys - set(self.update_fields)
        if len(unknown_fields) > 0:
            raise AttributeError(f'{str(unknown_fields)} field(s) is(are) not allowed')

        fields_values = tuple(data.get(key) for key in self.update_fields if key in data)
        
        if len(fields_values) <= 0: return None# 허용된 fields에 해당하는 data가 없으면 update할 data가 없다는 것을 의미하므로 종료.

        self.cur.execute(
            f'''
            UPDATE {self.table_name}
            SET {Placeholder.for_update_query(self.update_fields, **data)}
            WHERE id = ?
            ''',
            (*fields_values, id)
        )

        # TODO: last affected row가 0 이하이면 None 반환.
        if self.cur.rowcount <= 0:
            return None

        returnable_fields = list(set(self.retrieve_fields).intersection(set(data.keys())))

        context = {key: data.get(key) for key in returnable_fields}

        return context

    def perform_delete(self, id: int) -> None:
        """
        id로 지정되는 한 튜플을 삭제합니다.
        """
        self.cur.execute(
            f'''
            DELETE FROM {self.table_name}
            WHERE id = ?
            ''',
            (id,)
        )
        return None

    def create(self, **data: Dict) -> Dict:
        """
        data를 self.table_name 테이블에 추가합니다. perform_create(self, **data)와 다른 점이라면 오버라이드하여 data의 특정 field를 가공할 수 있습니다.
        """
        return self.perform_create(**data)

    def retrieve(self, id: int = None, fields: List[str] = []):
        """
        id가 지정될 경우 해당하는 한 튜플을, 주어지지 않을 경우 전체 튜플을 SELECT합니다. fields는 속성을 프로젝션할 수 있습니다. 주어지지 않을 경우 전체를 프로젝션합니다.
        """
        return self.perform_retrieve(id, fields)

    def update(self, id: int, **data: Dict) -> Dict:
        """
        id로 지정되는 한 튜플을 data로 갱신합니다. perform_update(self, id, **data)와 다른 점이라면 오버라이드하여 data의 특정 field를 가공할 수 있습니다.
        """
        return self.perform_update(id, **data)

    def delete(self, id: int) -> None:
        """
        id로 지정되는 한 튜플을 삭제합니다.
        """
        return self.perform_delete(id)
