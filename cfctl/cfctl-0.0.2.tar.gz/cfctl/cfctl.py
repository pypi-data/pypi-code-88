import CloudFlare
import argparse
import sys
from argparse import ArgumentParser

from CloudFlare.exceptions import CloudFlareAPIError


class ZoneDoesNotExist(Exception):
    pass

def get_zone(cf, zone_name):
    """
    Get information about a zone. 
    """
    zones = cf.zones.get()
    for zone in zones:
        if zone['name'] == zone_name:
            break
    else:
        msg = f"{zone_name} dns zone does not exist."
        raise ZoneDoesNotExist(msg)
    return zone

def do_list_zones():
    """
    Print a list of zones for the user account. 
    """
    cf = CloudFlare.CloudFlare()
    zones = cf.zones.get()
    for zone in zones:
        print(zone["name"])
        
def get_records(zone_name, ip_address_type="A"):
    """
    Get dns records for the given zone_name. 
    """
    
    cf = CloudFlare.CloudFlare()
    zone = get_zone(cf, zone_name)
    zone_id = zone["id"]

    params = {'match':'all'}
    dns_records = cf.zones.dns_records.get(zone_id, params=params)
    return dns_records    

    
def do_list_records(zone_name):
    """
    Display the dns records for given zone_name
    """
    dns_records = get_records(zone_name)
    print_records(dns_records)
        
    
def add_record(hostname,zone_name, content, ip_address_type="A"):
    """
    Add a dns record. 
    """
    
    cf = CloudFlare.CloudFlare()
    dns_name = f"{hostname}.{zone_name}"
    zone = get_zone(cf, zone_name)
      
    proxied_state = False
    
    dns_record = {
                'name':dns_name,
                'type':ip_address_type,
                'content':content,
                'proxied':proxied_state
            }
    
    zone_id = zone["id"]
    dns_record = cf.zones.dns_records.post(zone_id, data=dns_record)

def get_fqdn_records(fqdn, zone_name):
    dns_records = get_records(zone_name)
    
    results = []
    for dns_record in dns_records:
        name = dns_record.get("name")
        if name == fqdn:
            results.append(dns_record)
    return results

    
def do_inspect_fqdn(fqdn, zone_name):
    
    results = get_fqdn_records(fqdn, zone_name)
    if len(results) >0:
        print_records(results)
    else:
        print("No records found.")

def print_records(dns_records):
    for dns_record in dns_records:
        name = dns_record.get("name")
        content = dns_record.get("content")
        type = dns_record.get("type")        
        print(f"""{name}\t{type}\t{content}""")            
        

def do_delete_record(hostname,zone_name, content, ip_address_type="A"):
    
    
    cf = CloudFlare.CloudFlare()
    dns_name = f"{hostname}.{zone_name}"
    zone = get_zone(cf, zone_name)  
    proxied_state = False
    
    dns_record = {
                'name':dns_name,
                'type':ip_address_type,
                'content':content,
                'proxied':proxied_state
            }
    
    zone_id = zone["id"]
    dns_record = cf.zones.dns_records.get(zone_id, data=dns_record)
    
    for i in dns_record:
        iname = i["name"]
        icontent = i["content"]
        if iname == dns_name and icontent == content:
            cf.zones.dns_records.delete(zone_id,i["id"])


def main():
    
    parser = argparse.ArgumentParser()
    # Global options
   
    subparsers = parser.add_subparsers(dest="command")
    
    # Command: update-device
    parser_delete_record = subparsers.add_parser(
        "delete_record",
        help="Delete a record",
    )
    parser_delete_record.add_argument(
        "-f", "--fqdn",
        help="FQDN",
        required=True,
    )
    
    parser_delete_record.add_argument(
        "-c", "--content",
        help="record content",
    )
    
    # Command: list_zones
    parser_add_record = subparsers.add_parser(
        "add_record",
        help="Add a dns record",
    )
    

    parser_delete_record.add_argument(
        "-u", "--update",
        help="Update record if it exists",
        required = False
    )    
    
    parser_add_record.add_argument(
        "-f", "--fqdn",
        help="FQDN",
        required=True,
    )
     
    parser_add_record.add_argument(
        "-c", "--content",
        help="record content",
        required=True,
    )
       
    parser_add_record.add_argument(
        "-t", "--type",
        help="record type (optional)",
        default="A"
    )
     
     
    # Command: list_zone
    parser_list_records = subparsers.add_parser(
        "list_records",
        help="List records",
    )
    

    parser_list_records.add_argument(
        "zone_name",
        metavar="zone_name",
        type=str,
        help="the zone name aka Domain",
    )         
    
    
    # Command: list_zone
    parser_inspect_record = subparsers.add_parser(
        "inspect_fqdn",
        help="Show entry for record",
    )
    
    parser_inspect_record.add_argument(
        "-f", "--fqdn",
        help="FQDN",
        required=True,
    )
    
          
    
    args = parser.parse_args()
    if not args.command:
        parser.parse_args(["--help"])
        sys.exit(0)
    # Do the stuff here
    
    #print(args)
    #command = args.get("command")
    command = args.command
    if command == "list_zones":
        list_zones()
        
    elif command == "add_record":
       
        
        #since add_records expect a hostname and zone_name 
        #we need to split. 
        
        fqdn = args.fqdn
        hostname = fqdn[:fqdn.find(".")]
        zone_name = fqdn[fqdn.find(".")+1:]        
        
        try:
            add_record(hostname, zone_name, args.content)
        except CloudFlareAPIError as e:
            print(e)
        except ZoneDoesNotExist as e:
            msg = f"User account does not control zone: {zone_name}"
            print(msg)
        
        
    elif command == "delete_record":
        
        fqdn = args.fqdn
        hostname = fqdn[:fqdn.find(".")]
        zone_name = fqdn[fqdn.find(".")+1:]        
       
        try:
            do_delete_record(hostname, zone_name, args.content)
        except ZoneDoesNotExist as e:
            msg = f"User account does not control zone: {zone_name}"
            print(msg)            
            
    elif command == "list_records":
        print(args)
        do_list_records(args.zone_name)
        
    elif command == "inspect_fqdn":
        print(args)
        zone_name = args.fqdn[args.fqdn.find(".")+1:] 
        do_inspect_fqdn(args.fqdn, zone_name)
        
if __name__ == '__main__':
    main()