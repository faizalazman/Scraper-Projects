# -*- coding: utf-8 -*-
import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['https://www.brainyquote.com/']
    start_urls = ['https://www.brainyquote.com/topics/website/']

    def parse(self, response):
        quotes = response.xpath('//a[@title = "view quote"]/text()').extract()
        author = response.xpath('//a[@title = "view author"]/text()').extract()
        tags = response.xpath('//a[@title = "view author"]/text()').extract()

        for item in zip(quotes,author):
            info = {'Quotes': item[0],
                    'Author': item[1],
                    }

            yield info
        
