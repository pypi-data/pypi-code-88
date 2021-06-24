from configparser import ConfigParser
from json.decoder import JSONDecodeError

import requests
from pathlib import Path
from prettytable import PrettyTable

HOME_DIR = Path.home()
customer, vendor, cust_lics = PrettyTable(), PrettyTable(), PrettyTable()
customer.field_names = ["Customer Name", "Customer Id", "Customer Email",
                        "License CreationTime", "Vendor", "Vendor Id"]
vendor.field_names = ["Vendor Name", "Vendor Id", "Vendor Email",
                      "Vendor CreationTime", "Vendor", "Onboarded By"]
cust_lics.field_names = ["Customer Name", "Customer Id", "Customer Email",
                         "License CreationTime", "Vendor", "Vendor Id",
                         "Expires", "Quota", "Max Sessions"]


class RestClient:
    def __init__(self):
        self.config = ConfigParser()
        self.config.read("%s/.lm.ini" % HOME_DIR)
        self.token = self.config['DEFAULT']['Token']
        self.url = self.config['DEFAULT']['URL']
        session = requests.Session()
        adapters = requests.adapters.HTTPAdapter(max_retries=3)
        session.mount("http://", adapters)
        session.headers.update({'Accept': 'application/json',
                                'token': self.token})
        self.session = session
        self.debug = self.config['DEFAULT'].getboolean("debug", fallback=False)

    def post(self, url, req, **kwargs):
        target = kwargs.pop("table", customer)
        resp = self.session.post(url, json=req, **kwargs)
        resp = self.get_response(resp)
        self.print_response(resp, target)

    def get(self, url, **kwargs):
        target = kwargs.pop("table", customer)
        resp = self.session.get(url, **kwargs)
        resp = self.get_response(resp)
        self.print_response(resp, target)

    def get_customers_licenses(self, url, **kwargs):
        resp = self.session.get(url, **kwargs)
        if not resp.ok:
            return print(resp.text)
        self.dump_cust_lics(resp.json(), cust_lics)

    def put(self, url, req, **kwargs):
        target = kwargs.pop("table", customer)
        resp = self.session.put(url, json=req, **kwargs)
        resp = self.get_response(resp)
        self.print_response(resp, target)

    def update_lic(self, url, req, **kwargs):
        resp = self.session.put(url, json=req, **kwargs)
        resp = self.get_response(resp)
        print(resp.json().get('message'))

    def delete(self, url, **kwargs):
        resp = self.session.delete(url, **kwargs)
        # resp = self.get_response(resp)
        if resp.ok:
            print("%s successfully deleted" % url.split("/")[-1])

    def print_response(self, resp, table):
        objects = []
        if not resp.ok:
            print(self._print_json(resp))
            return
        resp = self._print_json(resp)
        if not resp or not table:
            try:
                print(resp.get('message', resp.get('response',
                                                   resp.get('msg', resp))))
            except AttributeError:
                print(resp)
            return
        elif "items" in resp and "item" in resp["items"]:
            objects.extend(resp["items"]["item"])
        elif isinstance(resp, list):
            objects.extend(resp)
        elif isinstance(resp, dict):
            objects.append(resp)
        self.dump_table(objects, table)

    @staticmethod
    def _print_json(resp):
        try:
            return resp.json()
        except JSONDecodeError:
            return resp.text

    def dump_table(self, objects, table):
        table.clear_rows()
        for ob in objects:
            if ob.get("name", "").lower() == "golcondaa":
                continue
            table.add_row([ob.get("name", ob.get("customer_name", "")),
                           ob.get("number", ob.get("customer_id", "")),
                           ob.get("email", ob.get("customer_email", "")),
                           ob.get("creationTime",
                                  ob.get("creation_time", "")),
                           ob.get("vendor", ob.get("vendor_name", "")),
                           ob.get("vendor_id", "")
                           ])
        print(table)
        table.clear_rows()

    def dump_cust_lics(self, objects, table):
        table.clear_rows()
        if isinstance(objects, dict):
            objects = [objects]
        for ob in objects:
            table.add_row([ob.get("name", ob.get("customer_name", "")),
                           ob.get("number", ob.get("customer_id", "")),
                           ob.get("email", ob.get("customer_email", "")),
                           ob.get("creationTime",
                                  ob.get("creation_time", "")),
                           ob.get("vendor", ob.get("vendor_name", "")),
                           ob.get("vendor_id", ""),
                           ob.get("expires", ""),
                           ob.get("quota", ""),
                           ob.get("max_sites", "")])
        print(table)
        table.clear_rows()

    def get_response(self, resp):
        try:
            resp.raise_for_status()
        except requests.exceptions.HTTPError as herr:
            print(herr)
        except requests.exceptions.Timeout as terr:
            print(terr)
        except requests.exceptions.ConnectionError as cerr:
            print(cerr)
        except requests.exceptions.RequestException as rerr:
            print(rerr)
        return resp


rc = RestClient()
