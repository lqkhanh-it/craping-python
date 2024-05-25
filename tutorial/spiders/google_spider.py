from pathlib import Path
import scrapy

class GoogleSpider(scrapy.Spider):
    name = "google"
    def __init__(self, *args, **kwargs):
        super(GoogleSpider, self).__init__(*args, **kwargs)
        self.target_url = kwargs.get('target_url')

    def start_requests(self):
        yield scrapy.Request(url=self.target_url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f"quotes-{page}.html"
        Path(filename).write_bytes(response.body)
        self.log(f"Saved file {filename}")