import json


# import pickle


def process_name(name: str) -> str:
    name = name.replace('社区居委会', '社区')
    name = name.replace('牧委会', '牧')
    name = name.replace('镇管委会社区', '镇')
    name = name.replace('路居委会', '路')
    name = name.replace('社区居民委员会', '社区')
    name = name.replace('居民委员会', '')
    name = name.replace('社区居委员会', '社区')
    name = name.replace('村村委员会', '村')
    name = name.replace('居民社区委员会', '社区')
    name = name.replace('村委员会', '村')
    name = name.replace('村委会', '村')
    name = name.replace('村村民委员会', '村')
    name = name.replace('村民民委员会', '村')
    name = name.replace('村民委员会', '')
    name = name.replace('村村', '村')

    if name.endswith('居委会'):
        name = name[:-3]
    if '社区' in name:
        box = name.split('社区')
        name = box[0] + '社区'
    return name


def load():
    area2street = {}
    data = json.load(open('streets.json', 'r', encoding='utf-8'))
    for rec in data:
        area_code = rec['areaCode']
        code = rec['code']
        name = rec['name']
        cache = area2street.get(area_code, {})
        cache[code] = {'name': name, 'villages': []}
        area2street[area_code] = cache
    data = json.load(open('villages.json', 'r', encoding='utf-8'))
    for rec in data:
        area_code = rec['areaCode']
        street_code = rec['streetCode']
        name = rec['name']

        name = process_name(name)
        code = rec['code']
        cache = area2street.get(area_code).get(street_code).get('villages')
        cache.append(name)
        area2street.get(area_code)[street_code]['villages'] = cache
    ret = {}
    for area_code, street_dict in area2street.items():
        cache = {}
        for street_code, street_info in street_dict.items():
            cache[street_info['name']] = street_info['villages']
        ret[area_code] = cache
    for code, info in ret.items():
        for vi, info2 in info.items():
            print(code, vi, info2)
    json.dump(ret, open('area2street_village.json', 'w', encoding='utf-8'), ensure_ascii=False)
    # pickle.dump(ret, open('area2street_village.pkl', 'wb'))


load()
