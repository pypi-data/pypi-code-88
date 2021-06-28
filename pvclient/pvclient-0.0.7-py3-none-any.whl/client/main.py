from os import times
from pyapacheatlas.auth import ServicePrincipalAuthentication
from pyapacheatlas.core import AtlasEntity, AtlasProcess
import json
import argparse

from pyapacheatlas.core.client import PurviewClient
from pvclient.utils import excel
from pvclient.utils import account
from pvclient.client.purview_client import ExtendedPurviewClient

def get_configuration():
    with open('configs.json') as json_file:
        return json.load(json_file)

def build_service_principal():
    import os
    TENANT_ID = os.getenv('TENANT_ID')
    CLIENT_ID = os.getenv('CLIENT_ID')
    CLIENT_SECRET = os.getenv('CLIENT_SECRET')  
    return ServicePrincipalAuthentication(
            tenant_id = TENANT_ID,
            client_id = CLIENT_ID,
            client_secret = CLIENT_SECRET)

def upload_entities(client):
    entities = excel.parse_excel_file_to_entities()
    if not entities and len(entities) > 0:
        return client.upload_entities(entities)

def list_glossary_terms(client):
    glossary = client.get_glossary(name="Glossary", guid=None, detailed=True)
    try:
        return glossary["termInfo"]
    except KeyError:
        print("Your default glossary appears to be empty.")
        exit(3)

def build_all_terms_guid(client):
    termsInfo = list_glossary_terms(client)
    return [i for i in termsInfo]

def check_env_variables():
    import os
    if None in [os.getenv('TENANT_ID'), os.getenv('CLIENT_ID'), os.getenv('CLIENT_SECRET'), os.getenv('SUBSCRIPTION_ID')]:
        raise ValueError("Missing environment variables. Please refer to https://pypi.org/project/pvclient/")
        exit(1)
def main():
    parser = argparse.ArgumentParser(description='Interaction with Purview')
    parser.add_argument("--version", action='store_true', help="Version of purview command-line")
    parser.add_argument("--create-purview", action='store_true')
    parser.add_argument("--assign-roles", action='store_true')
    parser.add_argument("--delete-purview", action='store_true')
    parser.add_argument("--create-glossary", help="Create a glossary with name")
    parser.add_argument("--list-terms", action='store_true')
    parser.add_argument("--upload-entities", action='store_true')
    parser.add_argument("--import-terms")
    parser.add_argument("--delete-term", help="Delete a term from the default Glossary")
    parser.add_argument("--delete-all-terms", action="store_true", help="Delete all terms from the default Glossary")
    parser.add_argument("--list-term-templates", action="store_true", help="List all term templates from the default Glossary")
    parser.add_argument("--import-term-templates", help="Import term templates from a file to the default Glossary")
    parser.add_argument("--delete-term-templates", help="Delete all templates from a file from the default Glossary")
    args = parser.parse_args()

    if args.version:
        from pvclient import __version__
        print("Purview version {}".format(__version__))
        exit(0)
    check_env_variables()
    configs = get_configuration()
    # Create a client to connect to your service.
    client = ExtendedPurviewClient(
        account_name = configs["Purview-account-name"],
        authentication = build_service_principal()
    )

    if args.create_purview:
        account.create_purview()
        account.assign_roles()
    
    if args.assign_roles:
        account.assign_roles()

    if args.delete_purview:
        account.delete_purview()

    if args.upload_entities:
        upload_entities(client)
    
    if args.list_terms:
        termInfos = list_glossary_terms(client)
        print(json.dumps(termInfos, indent=2))
    
    if args.import_terms:
        results = client.import_terms(csv_path=args.import_terms, glossary_name="Glossary", glossary_guid=None)
        print(json.dumps(results, indent=2))

    if args.delete_term:
        res = client.delete_glossary_term(args.delete_term)
        print(json.dumps(res, indent=2))

    if args.delete_all_terms:
        term_guids = build_all_terms_guid(client)
        client.delete_all_terms(term_guids)
    
    if args.list_term_templates:
        res = client.get_all_term_templates()
        print(json.dumps(res, indent=2))
    
    if args.import_term_templates:
        with open(args.import_term_templates) as file:
            res = client.import_term_templates(json.load(file))
            print(json.dumps(res, indent=2))
    if args.delete_term_templates:
        with open(args.delete_term_templates) as file:
            res = client.delete_term_templates(json.load(file))
            print(json.dumps(res, indent=2))
    
    if args.create_glossary:
        res = client.create_glossary(args.create_glossary)
        print(json.dumps(res, indent=2))


if __name__ == "__main__":
    main()