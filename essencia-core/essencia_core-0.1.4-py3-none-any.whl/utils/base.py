import unicodedata
from collections import namedtuple
import typing as tp



def make_people_tuple(data: tp.List[tp.Dict[str, tp.Any]]):
    Person = namedtuple('PersonKeyFullname', 'key fullname')
    cleaned_data = [ {'key': obj["key"], 'fullname': obj["fullname"]} for obj in data if (obj.get('key') and obj.get('fullname'))]
    people = [Person(**obj) for obj in cleaned_data]
    result = sorted(people, key=lambda x: x.fullname)
    return result

def make_people_key_fullname_dict(data: tp.List[tp.Dict[str, tp.Any]]):
    cleaned_data = [ {'key': obj["key"], 'fullname': obj["fullname"]} for obj in data if (obj.get('key') and obj.get('fullname'))]
    result = sorted(cleaned_data, key=lambda x: x['fullname'])
    return result

def make_people_select(id: str, label: str, data: tp.List[tp.Dict[str, tp.Any]]):
    dicts = make_people_key_fullname_dict(data)
    ordered_people = sorted(dicts, key=lambda x: x['fullname'])
    text = f'<select id="{id}">'
    text += f'<label for="{id}">{label}</label>'
    for person in ordered_people:
        text += f'<option value="{person["key"]}">{person["fullname"]}</option>'
    text += '</select>'
    return text


def normalize(input_str):
    def remove_accents(input_str):
        nfkd_form = unicodedata.normalize('NFKD', input_str)
        return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])
    return remove_accents(input_str=input_str).lower().strip()
