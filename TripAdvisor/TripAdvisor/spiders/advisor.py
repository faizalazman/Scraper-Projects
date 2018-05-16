# -*- coding: utf-8 -*-
import scrapy
from scrapy.conf import settings


class AdvisorSpider(scrapy.Spider):
    name = 'advisor'
    start_urls = ['https://www.tripadvisor.com.my/Restaurants-g298298-Ipoh_Kinta_District_Perak.html']

    def __init__(self):
        settings.overrides['DEPTH_LIMIT'] = 100

    def parse(self, response):
        name = [item.strip() for item in response.xpath('//div[@class="title"]/a/text()').extract()]
        link = response.xpath('//div[@class="title"]/a/@href').extract()
        rating = response.xpath('//div[@class="rating rebrand"]/span/@alt').extract()
        for item in zip(name,link,rating):
            yield {'name': item[0],
                   'link': item[1],
                   'rating': item[2],
                   }

        next_page = response.xpath('//div[@class="unified pagination js_pageLinks"]/a/@href').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)





