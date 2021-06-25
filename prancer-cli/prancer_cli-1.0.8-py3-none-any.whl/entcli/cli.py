"Run the local application"
import argparse
import requests
import json
import sys
import getpass
import os
import time

PREFIX = 'api'
SPACEID = 'space-id'
app_info = {}

def run_main(args):
    "Run it as a command line client to accept requests for prancer-ent"
    from cli_enterprise.entcli.configutils import config_value, set_config_value, prancer_config, make_config
    from cli_enterprise.entcli.fileutils import exists_file, remove_file

    global app_info

    if args.a:
        dprint("CLI configuration...", args.o)
        cfg = args.a
        if cfg.lower() == 'view':
            dprint("Viewing current configuration...", args.o)
            with open(prancer_config()) as f:
                print(f.read())
            return
        elif cfg.lower() == 'clean':
            dprint("cleaning current configuration...",args.o)
            f = prancer_config()
            if exists_file(f):
                dprint("Deleting %s configuration....." % f, args.o)
                remove_file(f)
            else:
                dprint("No configuration exists.....", args.o)
        elif cfg.lower() == 'create':
            dprint("creating current configuration...", args.o)
            make_config()
            set_config_value('DEFAULT', 'SERVER', 'http://portal.prancer.io/')
            set_config_value('DEFAULT', 'spaceid', '101')
            set_config_value('DEFAULT', 'customer', 'customer1')
            return
      
    server = config_value('DEFAULT', 'SERVER')
    if 'SERVER' in os.environ:
        envserver = os.environ.get('SERVER')
        if envserver:
            server = envserver
    spaceid = config_value('DEFAULT', 'SPACEID')
    customer = config_value('DEFAULT', 'CUSTOMER')
    
    if not server or not spaceid:
        print("Please add server config, exiting....!")
        sys.exit(1)
    validToken, token = validate_token(server, customer, spaceid, args)
    if not validToken:
        user = args.u if args.u else getenv('ENTCLI_KEY')
        pwd = args.p if args.p else getenv('ENTCLI_SECRET')
        if not user or not pwd:
            user = input('User:')
            pwd = getpass.getpass('Password:')
        dprint("Using user: %s and server: %s to connect...connecting" % (user, server), args.o)
        # url = '%s%s/token/' % (server, PREFIX)
        # usrPass = "%s:%s" % (user, pwd)
        # b64Val = base64.b64encode(usrPass.encode()).decode()
        url = '%s%s/%s/login/' % (server,customer, PREFIX)
        print(url)
        data = {
                   "email": user,
                   "password": pwd,
                "customer_id": customer

        }
        print(data)
        # hdrs = {SPACEID: spaceid, "Authorization": "Basic %s" % b64Val}
        hdrs = {SPACEID: spaceid, "content-type": "application/json"}

        # status, data = http_post_request(url, json.dumps(data), headers=hdrs, json_type=False, name='POST')
        # if status == 200:
        #     print(data)
        #     # token = '%s:1234' % data['token']
        #     # val = base64.b64encode(token.encode()).decode()
        #     set_config_value('DEFAULT','TOKEN', data['token'])
        resp = requests.post(url, json=data, headers=hdrs)
        data = resp.json()
        dprint(data, args.o)
        if data and 'data' in data and 'token' in data['data']:
            set_config_value('DEFAULT', 'TOKEN', data['data']['token'])
        else:
            print("Unable to get authentication token with the credentials, please check!")
            return

    if args.l:
        containers = container_list(server, customer, spaceid, token, args)
        print(containers)
    elif args.v:
        vaults = vault_list(server, customer, spaceid, token, args)
        print(vaults)
    elif args.c:
        crawler(server, customer, spaceid, token, args.c, args)
    elif args.t:
        tests(server, customer, spaceid, token, args.t, args)
    elif args.r:
        testsview(server, customer, spaceid, token, args.r, args)
    else:
        dprint("Select some operation!", args.o)

    sys.exit(0)


def validate_token(server, customer, spaceid, args):
    from cli_enterprise.entcli.configutils import config_value
    from cli_enterprise.entcli.httputils import http_get_request

    customer = config_value('DEFAULT', 'CUSTOMER')
    token = config_value('DEFAULT', 'TOKEN')
    validToken = False
    if token:
        url = '%s%s/%s/version/' % (server, customer, PREFIX)
        hdrs = {SPACEID: spaceid, "Authorization": "Basic %s" % token}
        # print(hdrs)
        status, data = http_get_request(url, hdrs)
        if status == 200:
            validToken = True
            dprint(data, args.o)
    return validToken, token


def container_list(server, customer, spaceid, token, args):
    from cli_enterprise.entcli.httputils import http_get_request
    if token:
        url = '%s%s/%s/containers/' % (server, customer, PREFIX)
        hdrs = {SPACEID: spaceid, "Authorization": "Bearer %s" % token}
        # print(hdrs)
        status, data = http_get_request(url, hdrs)
        if status == 200:
            # print(data)
            return data['value'] if 'value' in data else []
    return []

def vault_list(server, customer, spaceid, token, args):
    from cli_enterprise.entcli.httputils import http_get_request
    if token:
        url = '%s%s/%s/vault/list' % (server, customer, PREFIX)
        hdrs = {SPACEID: spaceid, "Authorization": "Basic %s" % token}
        # print(hdrs)
        status, data = http_get_request(url, hdrs)
        if status == 200:
            # print(data)
            return data if data else {}
    return {}

def tests(server, customer, spaceid, token, container, args):
    from cli_enterprise.entcli.httputils import http_post_request
    dprint('Checking %s is present in the containers' % container, args.o)
    containers = container_list(server, customer, spaceid, token, args)
    if container and container in containers:
        dprint('Running test for %s ' % container, args.o)
        url = '%s%s/%s/tests/' % (server, customer, PREFIX)
        hdrs = {SPACEID: spaceid, "Authorization": "Bearer %s" % token, "Content-Type": "application/json"}
        resp = requests.post(url, json={'container': container}, headers=hdrs)
        data = resp.json()
        print(data)
        logname = ''
        if data and 'log' in data:
            logname = data['log']
            dprint("Fetching test results", args.o)
            time.sleep(10)
            url = '%s%s/%s/results/%s/' % (server, customer, PREFIX, container)
            resp = requests.get(url,headers=hdrs)
            data = resp.json()
            if data and 'value' in data and isinstance(data['value'], list):
                results = data['value']
                for res in results:
                    o = res['json']
                    if 'container' in o and o['container'] == container and 'log' in o  and o['log'] == logname:
                        print(json.dumps(o['results'], indent=2))
                        break
        # status, data = http_post_request(url, {'container': container}, headers=hdrs, json_type=False, name='POST')
        # if status == 200:
        #     print(data)
        #     return data
    else:
        dprint('Cannot run test for %s as it is not present!' % container, args.o)
    return None

def testsview(server, customer, spaceid, token, container, args):
    dprint('Checking %s is present in the containers' % container, args.o)
    containers = container_list(server, customer, spaceid, token, args)
    if container and container in containers:
        dprint('Viewing test results for %s ' % container, args.o)
        hdrs = {SPACEID: spaceid, "Authorization": "Bearer %s" % token, "Content-Type": "application/json"}
        dprint("Fetching test results", args.o)
        url = '%s%s/%s/results/%s/' % (server, customer, PREFIX, container)
        resp = requests.get(url,headers=hdrs)
        data = resp.json()
        if data and 'value' in data and isinstance(data['value'], list):
                results = data['value']
                for res in results:
                    o = res['json']
                    print(json.dumps(o['results'], indent=2))
                    break
    else:
        dprint('Cannot run test for %s as it is not present!' % container, args.o)
    return None

def crawler(server, customer, spaceid, token, container, args):
    dprint('Checking %s is present in the containers' % container, args.o)
    containers = container_list(server, customer, spaceid, token, args)
    if container and container in containers:
        dprint('Running crawler for %s ' % container, args.o)
        url = '%s%s/%s/crawler/' % (server, customer, PREFIX)
        hdrs = {SPACEID: spaceid, "Authorization": "Basic %s" % token, "Content-Type": "application/json"}
        resp = requests.post(url, json={'container': container}, headers=hdrs)
        try:
            data = resp.json()
            print(data)
        except Exception as e:
            print("Failed to run crawler with exception: %s" % e)
        # status, data = http_post_request(url, {'container': container}, headers=hdrs, json_type=False, name='POST')
        # if status == 200:
        #     print(data)
        #     return data
    else:
        print('Cannot run crawler for %s as it is not present!' % container)
    return None


def dprint(msg, toPrint=True):
    if toPrint:
        print(msg)


def getenv(key):
    val = None
    if key and key in os.environ:
        val = os.environ.get(key)
    return val


# if __name__ == "__main__":
def run_cli():
    CMDPARSER = argparse.ArgumentParser()
    CMDPARSER.add_argument('-u', action='store', default=None, help='Username to login')
    CMDPARSER.add_argument('-p', action='store', default=None, help='Password for the user.')
    CMDPARSER.add_argument('-l', action='store_true', default=False, help='Container list')
    CMDPARSER.add_argument('-o', action='store_true', default=False, help='Verbose flag')
    CMDPARSER.add_argument('-v', action='store_true', default=False, help='Vault list')
    CMDPARSER.add_argument('-c', action='store', default=None, help='Container crawl')
    CMDPARSER.add_argument('-a', action='store', default=None, help='Configure prancer CLI using -a create')
    CMDPARSER.add_argument('-t', action='store', default=None, help='Container for running tests')
    CMDPARSER.add_argument('-r', action='store', default=None, help='results for tests')
    ARGS = CMDPARSER.parse_args()
    run_main(ARGS)


