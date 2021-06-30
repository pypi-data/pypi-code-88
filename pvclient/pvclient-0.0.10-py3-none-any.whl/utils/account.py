from azure.identity import ClientSecretCredential
from azure.mgmt import resource 
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.purview import PurviewManagementClient
from azure.mgmt.purview.models import Identity, AccountSku, Account
from datetime import datetime, timedelta
import time
import os

from pyapacheatlas import auth

def __make_purview_client__():
    TENANT_ID = os.getenv('TENANT_ID')
    CLIENT_ID = os.getenv('CLIENT_ID')
    CLIENT_SECRET = os.getenv('CLIENT_SECRET')
    SUBSCRIPTION_ID = os.getenv('SUBSCRIPTION_ID')
    credential = ClientSecretCredential(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET, 
        tenant_id=TENANT_ID)
    return PurviewManagementClient(credential, subscription_id=SUBSCRIPTION_ID)
        

def assign_roles():
    import os
    SUBSCRIPTION_ID = os.getenv('SUBSCRIPTION_ID')
    INTERACTIVEGROUPS = os.getenv('INTERACTIVEGROUPS')
    cmd_parameters = ["az role assignment create --assignee '{group}'".format(group=auth['Yggdrasil-Data-Platform-Developers']),
        "--role '{role}'",
        "--subscription '{resource_group}'".format(resource_group=SUBSCRIPTION_ID)]
    cmd_template = " ".join(cmd_parameters)

    roles = ['Purview Data Curator', 'Purview Data Reader', 'Purview Data Source Administrator']
    
    for role in roles:
        print('Assigning {role} to {group}'.format(role=role, group=INTERACTIVEGROUPS))
        cmd = cmd_template.format(role=role)
        stream = os.popen(cmd)
        output = stream.readlines()
        print(output)
        time.sleep(5)

def create_purview():
    purview_client = __make_purview_client__()
    #Create a purview
    identity = Identity(type= "SystemAssigned")
    sku = AccountSku(name= 'Standard', capacity= 4)
    purview_resource = Account(identity=identity,sku=sku,location =os.getenv('LOCATION'))
    rg_name = os.getenv('RESOURCE_GROUP')
    purview_name = os.getenv('PURVIEW_ACCOUNT_NAME')

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
    try:
        pa = purview_client.accounts.begin_delete(os.getenv('RESOURCE_GROUP'), os.getenv('PURVIEW_ACCOUNT_NAME')).result()
        print(pa)
    except:
        print("Error in submitting job to create account")
        print(pa)


def main():
    create_purview()
    #delete_purview()
