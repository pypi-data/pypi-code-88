import scrapy


class SettingsSpider(scrapy.Spider):
    name = 'Settings'
    allowed_domains = [
        'github.com'
    ]

    def __init__(
            self,
            url,
            path,
            pipe,

    ):
        super().__init__()

        self.start_urls = url
        self.pipe = pipe
        self.save = path

    def start_requests(self):
        yield scrapy.Request(self.start_urls)

    def parse(self, response, *args):
        entities = response.xpath("//div[@class='Box-row Box-row--focus-gray py-2 d-flex position-relative "
                                  "js-navigation-item ']")

        for entity in entities:
            if entity.xpath(".//span/a/text()").get() != "settings.json":
                continue

            self.logger.info("Found the Setting.json, :)")

            yield scrapy.Request(
                response.urljoin(
                    entity.xpath(".//span/a/@href").get()
                ), callback=self.yield_raw_settings
            )

            break

    def yield_raw_settings(self, response):
        raw = response.urljoin(response.xpath("//div[@class='BtnGroup']/a/@href").get())

        self.pipe(
            self.save, raw
        )

        yield {
            "raw_link": raw
        }
