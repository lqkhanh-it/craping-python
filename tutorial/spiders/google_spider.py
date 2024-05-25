from pathlib import Path
import scrapy
# from scrapy import signals

class GoogleSpider(scrapy.Spider):
    name = "google"
    def __init__(self, *args, **kwargs):
        super(GoogleSpider, self).__init__(*args, **kwargs)
        url = kwargs.get('target_url')
        self.target_url = url
        # self.allowed_domains = ['google.com']

    # @classmethod
    # def from_crawler(cls, crawler, *args, **kwargs):
    #     spider = super(GoogleSpider, cls).from_crawler(crawler, *args, **kwargs)
    #     crawler.signals.connect(spider.spider_closed, signal=signals.spider_closed)
    #     return spider

    # def spider_closed(self, spider):
    #     spider.logger.info("Spider closed: %s", spider.name)

    def start_requests(self):
        if self.target_url:
            self.logger.info("Target URL: %s", self.target_url)
            yield scrapy.Request(url=self.target_url, callback=self.parse)
        else:
            self.logger.error("Missing target URL. Please provide a URL to scrape.")
            
    def parse(self, response):
        self.logger.info("Parse function called on: %s", response.url)
        title = response.css('h3>div::text').getall()
        links = response.css('a::attr(href)').getall()
        stats = response.css('#top_nav').getall()

        links = [link for link in links if link.startswith('/url?q=http')]

        filename = f"quotes-1.html"
        Path(filename).write_bytes(response.body)
        self.log(f"Saved file {filename}")
        yield {
            'title': title,
            'stats': stats,
            'links': links,
        }