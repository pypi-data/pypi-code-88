import copy
from pprint import pprint

def merge(d1, d2): 
    if type(d2) == dict:
        for k in d2:
            if k in d1.keys():
                if type(d2[k]) == dict:
                    merge(d1[k], d2[k])
                    continue
            d1[k] = copy.deepcopy(d2[k])
    return d1

def get_from_key_list(data, keys):
    if data == None:
        return None
    if len(keys) > 1:
        if type(data) != dict:
            return None

        # if the key doesn't exist then return None
        if not keys[0] in data.keys():
            return None
        # if we aren't at the last key then go a level deeper
        return get_from_key_list(data[keys[0]], keys[1:])
    else:
        # if the key doesn't exist then return None
        if not keys[0] in data.keys():
            return None
        # return the value we want
        return data[keys[0]]

def set_from_key_list(data, keys, value):
    is_dict = not (keys[0][0] == '[' and keys[0][-1] == ']')
    print(is_dict)
    if is_dict:
        if data == None:
            data = {}
        if type(data) != dict:
            return None
    else:
        if data == None:
            data = []
        if type(data) != list:
            return None

    if is_dict:
        if not keys[0] in data.keys():
            if len(keys) == 1:
                data[keys[0]] = copy.deepcopy(value)
                return data
            else:
                if keys[1][0] == '[' and keys[1][-1] == ']':
                    data[keys[0]] = []
                else:
                    data[keys[0]] = {}
        if len(keys) > 1:
            # if we aren't at the last key then go a level deeper
            ret = copy.deepcopy(set_from_key_list(data[keys[0]], keys[1:], value))
            if ret == None:
                return None
            else:
                data[keys[0]] = ret
        else:
            # return the value we want
            data[keys[0]] = value
        return data
    else:
        index = int(keys[0][1:-1])
        if len(keys) == 1:
            while len(data) < index + 1:
                data.append(None)
            data[index] = copy.deepcopy(value)
            return data
        if len(data) < index + 1:
            while len(data) < index + 1:
                data.append(None)
            if keys[1][0] == '[' and keys[1][-1] == ']':
                data[index] = []
            else:
                data[index] = {}
        if len(keys) > 1:
            # if we aren't at the last key then go a level deeper
            ret = copy.deepcopy(set_from_key_list(data[index], keys[1:], value))
            if ret == None:
                return None
            else:
                while len(data) < index + 1:
                    data.append(None)
                data[index] = ret
        else:
            while len(data) < index + 1:
                data.append(None)
            # set the value we want
            data[index] = value
        return data

if __name__ == '__main__':
    in_dict = {
        "foo": "bar",
        "a": [
            "b",
            "c"
        ]
    }

    pprint(set_from_key_list(copy.deepcopy(in_dict), 'abc'.split('.'), 'def'))
    pprint(set_from_key_list(copy.deepcopy(in_dict), 'a.[0]'.split('.'), 'B'))
    pprint(set_from_key_list(copy.deepcopy(in_dict), 'a.[4]'.split('.'), 'd'))
    pprint(set_from_key_list(copy.deepcopy(in_dict), 'hello.world'.split('.'), 'ARG'))
    in_dict = set_from_key_list(copy.deepcopy(in_dict), 'a.[4]'.split('.'), 'd')
    pprint(set_from_key_list(copy.deepcopy(in_dict), 'a.[2].foo'.split('.'), 'bar'))