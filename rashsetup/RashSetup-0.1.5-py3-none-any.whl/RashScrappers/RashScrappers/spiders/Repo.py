import shutil
import urllib.request
from abc import ABC
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import tempfile
import concurrent.futures
import os
from queue import Queue


class TempHandler:
    def __init__(self, path=None):
        self.note = {
            False: [],
            True: []
        }

        self.temp = os.path.join(
            os.path.dirname(__file__) if not path else path if os.path.isdir(path) else os.path.dirname(path),
            "temp"
        )

        None if os.path.exists(self.temp) else os.mkdir(self.temp)

    def __call__(self, is_dir=False, suffix='', prefix='', dir_=None, text=True):

        if is_dir:
            path = tempfile.mkdtemp(suffix, prefix, dir_)
        else:
            mode, path = tempfile.mkstemp(suffix, prefix, dir_, text)
            os.close(mode)

        self.note[os.path.isdir(path)].append(path)
        return path

    def close(self):
        for _ in self.note[True]:
            shutil.rmtree(_, ignore_errors=True)

        for _ in self.note[False]:
            os.remove(_) if os.path.exists(_) else None


class DirWalk(Queue, object):
    # LEVEL ORDER TRANSVERSAL

    def __init__(
            self,
            name
    ):
        object.__init__(self)
        Queue.__init__(self)

        self.handler = TempHandler()
        self.temp_root = self.handler(
            True,
            prefix=name,
            dir_=self.handler.temp
        )

        self.pointer = ""
        self.thread_executor = concurrent.futures.ThreadPoolExecutor(
            max_workers=min(32, os.cpu_count() + 4),
            thread_name_prefix="Downloads"
        )

        self.base = Queue()

        self.put(
            self.temp_root
        )

    def add_entity(self, url):
        check = self.base.queue[0]

        self.level_up() if url == check["start"] else None
        self.base.get() if url == check["end"] else None

        path = os.path.join(
            self.pointer, os.path.split(url)[-1]
        )

        return path

    def add_file(self, url, raw):
        path = self.add_entity(url)

        urllib.request.urlretrieve(
            raw, path
        )

        return path

    def add_dir(self, url):
        path = self.add_entity(url)
        os.mkdir(path)

        self.put(
            path
        )

        return path

    def level_up(self):
        self.pointer = os.path.join(
            self.pointer, self.get()
        ) if self.pointer else os.path.join(
            self.get(), self.pointer
        )

    def end_walk(self):
        del self.base
        self.handler.close()
        del self.handler
        del self.temp_root


class RepoSpider(CrawlSpider, ABC):
    name = 'Repo'
    allowed_domains = ['github.com']

    custom_settings = {
        'CONCURRENT_REQUESTS': '1',
        "DEPTH_PRIORITY": 1,
        "SCHEDULER_DISK_QUEUE": 'scrapy.squeues.PickleFifoDiskQueue',
        "SCHEDULER_MEMORY_QUEUE": 'scrapy.squeues.FifoMemoryQueue'
    }

    # using BREADTH FIRST ORDER

    rules = (
        Rule(LinkExtractor(
            restrict_xpaths="//div[@role='row']/div[@role='rowheader']/span/a",
            deny_extensions=set()  # allows any file
        ),
            callback='parse_item', follow=True, process_links="pre_check"
        ),
    )

    def __init__(
            self,
            url,
            pipe,
            name
    ):
        super().__init__()
        self.start_urls = url

        self.room = DirWalk(
            name
        )

        self.pipe = pipe

    def start_requests(self):
        yield scrapy.Request(
            self.start_urls
        )

    def parse_item(self, response):
        is_file = response.xpath("//div[@class='BtnGroup']/a[1]/@href").get()
        raw = response.urljoin(is_file)

        path = self.room.add_file(response.url, raw) if is_file else self.room.add_dir(raw)

        yield {
            "is_file": is_file,
            "raw": raw,
            "path": path
        }

    def pre_check(self, link):
        if not link:
            return link

        self.room.base.put(
            {
                "start": link[0].url,
                "end": link[-1].url
            }
        )

        return link

    def close(self, spider, reason):

        self.pipe(
            self.room.temp_root
        )

        self.room.end_walk(

        )
        super().close(spider, reason)
