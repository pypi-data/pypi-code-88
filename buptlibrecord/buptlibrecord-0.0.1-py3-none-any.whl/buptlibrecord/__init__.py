#!/usr/bin/python3

__author__ = 'sxwxs'
__date__ = '2021-06-24'

import requests
import json
import time
import sys
import csv
import os

headers = {'Accept': '*/*',
 'Accept-Encoding': 'gzip, deflate',
 'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
 'Connection': 'keep-alive',
 'Content-Length': '50',
 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
 'Cookie': 'JSESSIONID=',
 'Host': 'opac.bupt.edu.cn:8080',
 'Origin': 'http://opac.bupt.edu.cn:8080',
 'Referer': 'http://opac.bupt.edu.cn:8080/reader-history.html',
 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
 'X-Requested-With': 'XMLHttpRequest'
}

def get_result(page):
    r = requests.post('http://opac.bupt.edu.cn:8080/reader-history.json', data={
        "pageNo": str(page),
        "pageSize": "10",
        "name": "",
        "date": "",
        "dateEnd": "",
        "type": "all"
    }, headers=headers)
    return r
def get_all_record_list(JSESSIONID):
    if JSESSIONID.startswith('JSESSIONID='):
        JSESSIONID = JSESSIONID[len('JSESSIONID='):]
    headers['Cookie'] = 'JSESSIONID=' + JSESSIONID
    page = 1
    book_info_list = []
    while True:
        r = get_result(page)
        try:
            j = r.json()
        except Exception as e:
            print("Error: ", e, r, r.text)
            break
        book_info_list += j['data']
        print("%d / %d Finished." % (page, j['totalPage']))
        if page >= j['totalPage']:
            break
        time.sleep(1)
        page += 1
    return book_info_list , j['totalPage'], j['total']

def run(JSESSIONID):
    book_info_list, totalPage, total = get_all_record_list(JSESSIONID)
    t = int(time.time())
    with open('my_book_list_%d.json' % t, 'w', encoding='utf8') as f:
        json.dump(book_info_list, f, ensure_ascii=False)
    
    with open('my_book_list_gbk_%d.csv' % t, 'w', encoding='gbk',newline='') as f:
        f_csv = csv.writer(f)
        for l in book_info_list:
            if int(l['operateCode']) == 1:
                f_csv.writerow([l['title'], l['authors'], l['publisher'], l['pubdateDate'], l['operateDate']])
    bookset = {}
    with open('my_book_record_gbk_%d.csv' % t, 'w', encoding='gbk',newline='') as f:
        f_csv = csv.writer(f)
        for l in book_info_list:
            if l['title'] not in bookset:
                bookset[l['title']] = 0
            if int(l['operateCode']) == 1:
                bookset[l['title']] += 1
            if int(l['operateCode']) == 2:
                bookset[l['title']] -= 1
            f_csv.writerow([l['title'], l['authors'], l['publisher'], l['pubdateDate'], l['operateDate'], l['operateCode']])
    for b in bookset:
        if bookset[b] > 0:
            print("待归还图书：", b)


def main():
    if len(sys.argv) != 2:
        JSESSIONID = input("JSESSIONID=")
    else:
        JSESSIONID = sys.argv[1]
    run(JSESSIONID)