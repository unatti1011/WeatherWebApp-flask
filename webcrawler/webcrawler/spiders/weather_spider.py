import scrapy
import json

from scrapy.crawler import CrawlerProcess


class WeatherItem(scrapy.Item):
    locationName = scrapy.Field()
    currTemp = scrapy.Field()
    humidity = scrapy.Field()
    wind = scrapy.Field()
    weatherIcon = scrapy.Field()


class WeatherSpider(scrapy.Spider):
    name = "weather"
    start_urls = [
        'https://weather.com/weather/today/32.08,34.78',
        'https://weather.com/weather/today/51.50,0.12',
        'https://weather.com/weather/today/40.73,-73.93'
    ]
    def parse(self, response):
        return WeatherItem(
            locationName=response.xpath(
                '//*[@id="WxuCurrentConditions-main-b3094163-ef75-4558-8d9a-e35e6b9b1034"]/div/section/div/div[1]/h1/text()').get(),
            currTemp=response.xpath(
                '//*[@id="WxuCurrentConditions-main-b3094163-ef75-4558-8d9a-e35e6b9b1034"]/div/section/div/div[2]/div[1]/span/text()').get(),
            humidity=response.xpath(
                '//*[@id="WxuTodayDetails-main-fd88de85-7aa1-455f-832a-eacb037c140a"]/section/div[2]/div[3]/div[2]/span/text()').get(),
            wind=response.xpath(
                '//*[@id="WxuTodayDetails-main-fd88de85-7aa1-455f-832a-eacb037c140a"]/section/div[2]/div[2]/div[2]/span/text()').get(),
            weatherIcon=response.css('svg')[20].get()
        )
