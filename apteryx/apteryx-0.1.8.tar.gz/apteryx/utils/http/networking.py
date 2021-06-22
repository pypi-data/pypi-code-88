import requests
import pandas as pd


def get_public_ip():
    resp = requests.get('https://www.whatismyip.org/my-ip-address')
    df = pd.read_html(resp.text)[0]
    df.columns = ['labels', 'vals']
    return df[df.labels == 'Your IP'].vals[0]
