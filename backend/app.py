from flask import Flask, request, jsonify
from scrape import scrape_data
import scrapy.crawler as crawler

import sys         
sys.path.append('E:/lqkhanh/scrapy/tutorial')

from tutorial.spiders.google_spider import GoogleSpider

app = Flask(__name__)
app.config["SECRET_KEY"] = 'secret!'
app.config["DEBUG"] = True

@app.route('/api/v1/scrape', methods=['POST'])
def receive_data():
    url = request.get_json()["url"]
    
    try:
        # process = crawler.CrawlerProcess(
        #     settings={
        #         "REQUEST_FINGERPRINTER_IMPLEMENTATION": "2.7"
        #         }
        #     )

        # process.crawl(GoogleSpider, target_url=url)
        # process.start()
     
        scrape_data(url)
        return jsonify({'message': "true"}), 200 
    except Exception as e:
        return jsonify({'error': str(e)}), 500 

if __name__ == '__main__':
    app.run()