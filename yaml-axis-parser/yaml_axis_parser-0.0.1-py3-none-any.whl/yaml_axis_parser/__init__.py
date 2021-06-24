import argparse
import yaml
import copy
import collections


def matches(item, exclude):
    for key, value in exclude.items():
        if item[key] != value:
            return False
    return True


def is_excluded(item, excludes):
    for exclude in excludes:
        if matches(item, exclude):
            return True
    return False


def parse_axis(file, exclude_key):
    contents = yaml.full_load(file)
    excludes = []
    if contents[exclude_key]:
        for exclude in contents[exclude_key]:
            ex = {}
            for key, value in exclude.items():
                if type(value) == list:
                    raise Exception('Exclude value-lists not yet implemented')
                ex[key] = value
            excludes.append(ex)

    values = []
    for key, value in contents.items():
        if key == exclude_key:
            continue
        new_values = []
        if not values:
            for val in value:
                new_values.append(collections.OrderedDict({key: val}))
        else:
            for val in value:
                copied = copy.deepcopy(values)
                for c in copied:
                    c[key] = val
                new_values.extend(copied)
        values = new_values

    def sort_key(i):
        return tuple(str(x) for x in i.values())

    for value in sorted(values, key=sort_key):
        if not is_excluded(value, excludes):
            print(dict(value))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--exclude-key', '-e', default='exclude',
                        help='The exclude key. Defaults to "exclude"')
    parser.add_argument('file', type=argparse.FileType(mode='r'),
                        help='The yaml axis file')

    ns = parser.parse_args()
    parse_axis(ns.file, ns.exclude_key)


if __name__ == '__main__':
    main()
