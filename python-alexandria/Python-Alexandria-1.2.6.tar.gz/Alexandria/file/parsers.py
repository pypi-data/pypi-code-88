import yaml


def yaml_parser(file):
    with open(file) as f:
        return {k:
                tuple(int(item) for item in v[1:-1].split(", "))
                if isinstance(v, str) and v[0] == "(" and v[-1] == ")"
                else v
                for k, v in yaml.safe_load(f.read()).items() if v is not None}
