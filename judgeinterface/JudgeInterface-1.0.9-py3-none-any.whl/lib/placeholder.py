from typing import Dict, List
import re

class Placeholder:
    @staticmethod
    def for_create_query(fields_len: int) -> str:
        placeholder = ''
        for i in range(fields_len):
            placeholder += '?, '
        placeholder = re.sub(', $', '', placeholder)
        return placeholder

    @staticmethod
    def for_select_query(select_fields: List[str], requested_fields: List[str]) -> str:
        filtered_fields = list(filter(lambda field: field in requested_fields, select_fields))
        if len(filtered_fields) <= 0: return ''
        placeholder = ''
        for field in filtered_fields:
            placeholder += f'{field}, '
        placeholder = re.sub(', $', '', placeholder)
        return placeholder   

    @staticmethod
    def for_update_query(update_fields: List[str], **data: Dict) -> str:
        placeholder = ''
        for key in update_fields:
            if key in data:
                placeholder += key + ' = ?, '
        placeholder = re.sub(', $', '', placeholder)
        return placeholder
