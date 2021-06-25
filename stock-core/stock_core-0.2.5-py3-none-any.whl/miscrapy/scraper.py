import os
import time
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from multiprocessing import Process

import logging
logger = logging.getLogger(__name__)
formatter = logging.Formatter('%(levelname)s: [%(name)s] %(message)s')
ch = logging.StreamHandler()
ch.setFormatter(formatter)
logger.addHandler(ch)
logger.setLevel(logging.WARNING)


def chcwd(func):
    # scrapy는 항상 프로젝트 내부에서 실행해야하기때문에 일시적으로 현재 실행경로를 변경한다.
    def wrapper(*args, **kwargs):
        before_cwd = os.getcwd()
        logger.info(f'current path : {before_cwd}')
        after_cwd = os.path.dirname(os.path.realpath(__file__))
        logger.info(f'change path to {after_cwd}')
        os.chdir(after_cwd)
        func(*args, **kwargs)
        logger.info(f'restore path to {before_cwd}')
        os.chdir(before_cwd)
    return wrapper


def _use_single(spider):
    # reference from https://docs.scrapy.org/en/latest/topics/practices.html(코드로 스파이더 실행하기)
    process = CrawlerProcess(get_project_settings())
    process.crawl(spider)
    process.start()


@chcwd
def mi():
    spider_list = ('aud', 'chf', 'gbond3y', 'gold', 'kosdaq', 'kospi', 'sp500', 'usdkrw', 'wti', 'silver')
    print('*' * 25, f"Scrape multiprocess mi", '*' * 25)
    logger.info(spider_list)

    start_time = time.time()
    ths = []
    error = False
    for spider in spider_list:
        ths.append(Process(target=_use_single, args=(spider,)))
    for i in range(len(ths)):
        ths[i].start()
    for i in range(len(ths)):
        ths[i].join()
        if ths[i].exitcode != 0:
            error = True
    print(f'Total spent time : {round(time.time() - start_time, 2)} sec')
    print('done.')
    return error


@chcwd
def mihistory(year: int):
    process = CrawlerProcess(get_project_settings())
    process.crawl('mihistory', year=year)
    process.start()


if __name__ == '__main__':
    mi()

