from pathlib import Path
import scrapy

class GoogleSpider(scrapy.Spider):
    name = "google"
    def __init__(self, *args, **kwargs):
        super(GoogleSpider, self).__init__(*args, **kwargs)
        self.target_url = kwargs.get('target_url')

    def start_requests(self):
        if self.target_url:
            yield scrapy.Request(url=self.target_url, callback=self.parse)
        else:
            self.logger.error("Missing target URL. Please provide a URL to scrape.")

    def parse(self, response):
        title = response.css('title::text').get()
        links = response.css('a::attr(href)').getall()

        page = response.url.split("/")[-2]
        filename = f"quotes-{page}.html"
        Path(filename).write_bytes(response.body)
        self.log(f"Saved file {filename}")
        yield {
            'title': title,
            'links': links,
        }