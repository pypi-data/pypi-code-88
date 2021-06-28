from azure.identity import ClientSecretCredential
from azure.mgmt import resource 
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.purview import PurviewManagementClient
from azure.mgmt.purview.models import Identity, AccountSku, Account
from datetime import datetime, timedelta
import time
import json

from pyapacheatlas import auth

def __make_purview_client__():
    with open('auth.json') as json_file:
        auth = json.load(json_file)
        credential = ClientSecretCredential(client_id=auth['client_id'],
         client_secret=auth['client_secret'], tenant_id=auth['tenant_id'])
        return PurviewManagementClient(credential, subscription_id=auth['subscription_id'])

def assign_roles():
    with open('auth.json') as json_file:
        auth = json.load(json_file)

    cmd_parameters = ["az role assignment create --assignee '{group}'".format(group=auth['Yggdrasil-Data-Platform-Developers']),
        "--role '{role}'",
        "--subscription '{resource_group}'".format(resource_group=auth['subscription_id'])]
    cmd_template = " ".join(cmd_parameters)

    roles = ['Purview Data Curator', 'Purview Data Reader', 'Purview Data Source Administrator']
    for role in roles:
        print('Assigning {role} to {group}'.format(role=role, group=auth['InteractiveGroups']))
        cmd = cmd_template.format(role=role)
        import os
        stream = os.popen(cmd)
        output = stream.readlines()
        print(output)
        time.sleep(5)
    


def create_purview():
    purview_client = __make_purview_client__()
    with open('configs.json') as json_file:
        configs = json.load(json_file)
        #Create a purview
        identity = Identity(type= "SystemAssigned")
        sku = AccountSku(name= 'Standard', capacity= 4)
        purview_resource = Account(identity=identity,sku=sku,location =configs['location'])
        rg_name = configs['Resource-group']
        purview_name = configs['Purview-account-name']

        try:
            pa = (purview_client.accounts.begin_create_or_update(rg_name, purview_name, purview_resource)).result()
            print("location:", pa.location, " Purview Account Name: ", purview_name, " Id: " , pa.id ," tags: " , pa.tags) 
        except:
            print("Error in submitting job to create account")
            print(pa)

        while (getattr(pa,'provisioning_state')) != "Succeeded" :
            pa = (purview_client.accounts.get(rg_name, purview_name))
            status = getattr(pa,'provisioning_state')
            print(status)
            if status == "Succeeded":
                assign_roles()
                break
            elif status == "Failed":
                break
            elif status == "Creating" or  status == "Updating":
                time.sleep(30)
            else:
                ValueError("Unhandled status")

def delete_purview():
    purview_client = __make_purview_client__()
    with open('configs.json') as json_file:
        configs = json.load(json_file)

    rg_name = configs['Resource-group']
    purview_name = configs['Purview-account-name']
    try:
        pa = purview_client.accounts.begin_delete(rg_name, purview_name).result()
        print(pa)
    except:
        print("Error in submitting job to create account")
        print(pa)


def main():
    create_purview()
    #delete_purview()
