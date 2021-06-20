"""Main module."""
import urllib.request

def get_my_ip():
    external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
    return external_ip