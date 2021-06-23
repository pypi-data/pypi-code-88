import click

from src.client import rc, vendor


@click.group(name="lm")
def lm_cli():
    """
    Cli for lm proxy
    :return:
    """


@lm_cli.command()
@click.option("--vendor_name", required=True, help="name of vendor")
@click.option("--email", required=True, help="vendor's email address")
def create_vendor(vendor_name, email):
    req = {
        "name": vendor_name,
        "email": email
    }
    rc.post(rc.url + "/partners", req, table=vendor)


@lm_cli.command()
@click.option("--vendor_name", required=True, help="name")
def get_customers_of_a_vendor(vendor_name):
    rc.get(rc.url + "/licenses/partners/%s" % vendor_name)


def format_license_input(subscription, quota, sites):
    licenses, lic = [], {}
    if subscription:
        lic["subscription"] = {"time": subscription}
    if quota:
        lic["quota"] = {"users": quota}
    if sites:
        lic["multisite"] = {"sites": sites}
    licenses.append(lic)
    return licenses


@lm_cli.command()
@click.option("--customer_name", required=True, help="name of customer")
@click.option("--customer_email", required=True,
              help="customer's email address")
@click.option("--vendor", required=True, help="vendor name")
@click.option("--vendor_id", required=True, help="vendor id")
@click.option("--vendor_email", required=True, help="vendor's email address")
@click.option("--subscription",
              default=None,
              help="subscription period of dkube license eg. '1y' for 1 "
                   "year, '1m' for 1 month, '1w' for 1 week")
@click.option("--quota", default=None, type=int, help="no of users quota")
@click.option("--sites", default=None, type=int, help="no of dkube sites")
def create_customer(customer_name, customer_email, vendor,
                    vendor_id, vendor_email, subscription, quota, sites):
    licenses = format_license_input(subscription, quota, sites)
    req = {
        "customer_name": customer_name,
        "customer_email": customer_email,
        "vendor": vendor,
        "vendor_email": vendor_email,
        "vendor_id": vendor_id,
        "licenses": licenses
    }
    rc.post(rc.url + "/customers", req)


@lm_cli.command()
@click.option("--name", required=True, help='name of the customer')
def get_customer_licenses(name):
    rc.get_customers_licenses(rc.url + "/licenses/%s" % name)


@lm_cli.command()
@click.option("--id", required=True, help='name of the customer')
def get_customer_licenses_by_id(id):
    rc.get_customers_licenses(rc.url + "/licenses/customers/%s" % id)


@lm_cli.command()
@click.option("--vendor_id", required=True, help="Vendor Id")
def delete_vendor(vendor_id):
    rc.delete(rc.url + "/partners/%s" % vendor_id)


@lm_cli.command()
@click.option("--customer_id", required=True, help="Customer Id")
def delete_customer(customer_id):
    rc.delete(rc.url + "/customers/%s" % customer_id)


@lm_cli.command()
def list_customers():
    rc.get(rc.url + "/customers")


@lm_cli.command()
@click.option("--id", required=True, help="Customer Id")
def get_customer(id):
    rc.get(rc.url + "/customers/%s" % id)


@lm_cli.command()
@click.option("--session_id", required=True, help="Session Id")
@click.option("--customer_id", help="Customer Id")
def clear_session(session_id, customer_id):
    req = {}
    if customer_id:
        req = {'customer_id': customer_id}
    rc.post(rc.url + "/licenses/clear/%s" % session_id, req, table=None)


def format_update_license(subscription, quota, sites):
    license = dict()
    if subscription:
        license.update(subscription=subscription)
    if quota:
        license.update(quota=quota)
    if sites:
        license.update(sites=sites)
    return license


@lm_cli.command()
@click.option("--customer_id", required=True, help="Customer Id")
@click.option("--subscription",
              default=None,
              help="subscription period of dkube license eg. '1y' for 1 "
                   "year, '1m' for 1 month, '1w' for 1 week")
@click.option("--quota", default=None, type=int, help="no of users quota")
@click.option("--sites", default=None, type=int, help="no of dkube sites")
def update_license(customer_id, subscription, quota, sites):
    license = format_update_license(subscription, quota, sites)
    rc.update_lic(rc.url + "/customers/%s/license" % customer_id, license)
