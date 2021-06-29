import configargparse


def parse() -> configargparse.Namespace:
    p = configargparse.ArgParser()
    p.add('-c', '--config', required=False, is_config_file=True, help='config file path')
    p.add('--host', action='append', help='remote host address, simulate training if not set')
    return p.parse_args()


if __name__ == '__main__':
    options = parse()
    print(options)
