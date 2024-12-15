import scrapy
import json

from scrapy.crawler import CrawlerProcess


class WeatherItem(scrapy.Item):
    locationName = scrapy.Field()
    currTemp = scrapy.Field()
    humidity = scrapy.Field()
    wind = scrapy.Field()
    weatherIcon = scrapy.Field()


class WeatherSpiderChoosed(scrapy.Spider):
    name = "weather"

    def __init__ (self, coordSend=None,*args, **kwargs):
        super(WeatherSpiderChoosed, self).__init__(*args, **kwargs)
        self.start_urls = ['https://weather.com/weather/today/l/%s' % coordSend]

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
