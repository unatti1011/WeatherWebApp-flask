from flask_cors import CORS
from flask import Flask, jsonify, request
import webcrawler.spiders.weather_spider as WS
import webcrawler.spiders.weather_spider_choosed as WSC
from scrapy.crawler import CrawlerProcess
from scrapy.signalmanager import dispatcher
from scrapy.crawler import CrawlerRunner
from scrapy import signals
import scrapy
import crochet
crochet.setup()

app = Flask(__name__)
CORS(app)

output_data = []
output_data_city = []
crawl_runner = CrawlerRunner()


@app.route('/get_deafult_weather')
def get_default_weather():
    scrape_with_crochet()
    return jsonify(output_data[:3])


@app.route('/city_weather/<coordSend>')
def get_choosed_city(coordSend):
    output_data_city.clear()
    scrape_with_crochet_city(coordSend)
    return jsonify(output_data_city[:1])


@crochet.wait_for(timeout=60.0)
def scrape_with_crochet():
    dispatcher.connect(_crawler_result, signal=signals.item_scraped)
    eventual = crawl_runner.crawl(
        WS.WeatherSpider)
    return eventual


def _crawler_result(item, response, spider):
    output_data.append(dict(item))

@crochet.wait_for(timeout=60.0)
def scrape_with_crochet_city(coordSend):
    dispatcher.connect(_crawler_result_city, signal=signals.item_scraped)
    eventual = crawl_runner.crawl(
        WSC.WeatherSpiderChoosed, coordSend)
    return eventual


def _crawler_result_city(item, response, spider):
    output_data_city.append(dict(item))


if __name__ == '__main__':
    app.run('0.0.0.0', 8080)

if __name__ == '__main__':
    app.run()
