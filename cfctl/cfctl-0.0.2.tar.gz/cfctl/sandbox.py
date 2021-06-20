import CloudFlare
import argparse
import sys
from argparse import ArgumentParser


class ZoneDoesNotExist(Exception):
    pass

def get_zone(cf, zone_name):
    zones = cf.zones.get()
    for zone in zones:
        if zone['name'] == zone_name:
            break
    else:
        msg = f"{zone_name} dns zone does not exist."
        raise ZoneDoesNotExist(msg)
    return zone

def list_zones():
    cf = CloudFlare.CloudFlare()
    zones = cf.zones.get()
    for zone in zones:
        print(zone["name"])
        
def get_records(zone_name, ip_address_type="A"):
    
    cf = CloudFlare.CloudFlare()
    zone = get_zone(cf, zone_name)
    zone_id = zone["id"]

    params = {'match':'all'}
    dns_records = cf.zones.dns_records.get(zone_id, params=params)
    return dns_records    

    
def list_records(zone_name):
    
    dns_records = get_records(zone_name)
    
    for dns_record in dns_records:
        name = dns_record.get("name")
        content = dns_record.get("content")
        type = dns_record.get("type")
        
        print(f"""{name}\t{type}\t{content}""")
    
def add_record(hostname,zone_name, content, ip_address_type="A"):
    
    
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
        print(f"{iname},{icontent}")
        if iname == dns_name and icontent == content:
            cf.zones.dns_records.delete(zone_id,i["id"])



if __name__ == '__main__':
   
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
        print(args)
        
        #since add_records expect a hostname and zone_name 
        #we need to split. 
        
        fqdn = args.fqdn
        hostname = fqdn[:fqdn.find(".")]
        zone_name = fqdn[fqdn.find(".")+1:]        
        
        
        add_record(hostname, zone_name, args.content)
        
    elif command == "delete_record":
        
        print("delete re")
        
        
        """
        
        """
        
       
        
        