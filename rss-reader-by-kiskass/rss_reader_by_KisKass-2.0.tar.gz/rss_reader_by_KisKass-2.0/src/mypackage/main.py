import urllib.request
import argparse
from bs4 import BeautifulSoup
from datetime import datetime
# from icecream import ic
import json
import sys

parser = argparse.ArgumentParser()

parser.add_argument('source', default='https://news.yahoo.com/rss/')
parser.add_argument('--version',
                    action='version', version='version 2.0',
                    help='Print version info')
parser.add_argument('--json',
                    action="store_true",
                    help='Print result as JSON in stdout')
parser.add_argument('--verbose',
                    action="store_true",
                    help='Outputs verbose status messages')
parser.add_argument('--limit',
                    type=int,
                    default=0,
                    help='Limit news topics if this parameter provided')
args = parser.parse_args()


def output_json():
    """json style output"""
    soup = parse_url(args.source)
    data_set = {'Feed': soup.source.string}
    news = parse_news(soup, args.limit)
    i = 0
    for n in news:
        data_set['item' + str(i)] = {'Title': n.title.text,
                                     'Date': n.pubDate.string,
                                     'Link': n.link.string}
        i += 1
    json_dump = json.dumps(data_set, indent=4, ensure_ascii=False)
    print(json_dump)


def parse_url(source: str):
    """Gets xml from url"""
    # ic('Parsing rss')
    with urllib.request.urlopen(source) as f:
        soup = BeautifulSoup(f, "xml")
    return soup


def parse_news(soup, limit_=0):
    """Gets items from xml"""
    # ic('Parsing news')
    if limit_:
        return soup.find_all('item', limit=limit_)
    else:
        return soup.find_all('item')


def normal_output():
    """Normal output"""
    soup = parse_url(args.source)
    print(soup.title.text)
    news = parse_news(soup, args.limit)
    for n in news:
        print(f'Title: {n.title.text}')
        print(f'Date: {n.pubDate.string}')
        print(f'Link: {n.link.string}\n')
        # ниже код который выводит подробности новости но т.к. он замедляет работу программы я его временно убрал
        # with urllib.request.urlopen(n.link.string) as f:
        #    item_details = BeautifulSoup (f, "lxml",)
        #    for item_detail in item_details.find_all('p'):
        #        if item_detail.text != '':
        #            print(item_detail.text)
        #            break
        #    print('-----------')
        pass


def main():

    # ic.disable
    # ic.configureOutput(prefix='log | ')

    if args.verbose:
        print('verbose on')
        # ic.enable

    # if args.version:
    #     print(args.version)
    #     sys.exit(0)

    if args.json:
        output_json()
    else:
        normal_output()
