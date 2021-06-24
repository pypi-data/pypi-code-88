import scrapy


class ModuleCheckerSpider(scrapy.Spider):
    name = 'ModuleChecker'

    allowed_domains = [
        'github.com'
    ]

    def __init__(
            self,
            url,
            pipe,
            err_back
    ):
        super().__init__()
        self.pipe = pipe
        self.start_urls = url
        self.error_back = err_back

    def start_requests(self):
        yield scrapy.Request(
            self.start_urls,
            errback=self.error_back
        )

    def parse(self, response, *args):
        entities = response.xpath("//div[@class='Box-row Box-row--focus-gray py-2 d-flex position-relative "
                                  "js-navigation-item ']")

        result = [False, False, False]
        index = 0

        for entity in entities:
            entity_ = entity.xpath(".//span/a/text()").get()

            if entity_ not in (
                    "settings.json",
                    "setup.py",
                    "README.md"
            ):
                continue

            result[index] = True
            index += 1

            yield scrapy.Request(
                response.urljoin(
                    entity.xpath(".//span/a/@href").get()
                ), callback=self.yield_raw_settings, meta={"name": entity_}, errback=self.error_back
            )

            break

        self.pipe(
            all(result)
        )

    def yield_raw_settings(self, response):
        raw = response.urljoin(response.xpath("//div[@class='BtnGroup']/a/@href").get())

        self.pipe(
            {
                response.request.meta["name"]: raw
            }
        )

        yield {
            "raw_link": raw
        }
