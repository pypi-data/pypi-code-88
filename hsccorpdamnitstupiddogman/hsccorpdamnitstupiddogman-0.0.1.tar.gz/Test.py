from hscorp import Web
test_crawl = Web("https://google.com")
for i in test_crawl.crawl('common.txt'):
    print(i)