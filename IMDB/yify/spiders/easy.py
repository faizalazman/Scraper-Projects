import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class EasySpider(CrawlSpider):
    name = 'easy'
    allowed_domains = ['imdb.com']
    start_urls = ['https://www.imdb.com/search/title?genres=horror&explore=title_type,genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=75c37eae-37a7-4027-a7ca-3fd76067dd90&pf_rd_r=4S1979D70QS5VV1R9R8Z&pf_rd_s=center-1&pf_rd_t=15051&pf_rd_i=genre&view=advanced&page=2&ref_=adv_nxt']

    rules = (Rule(LinkExtractor(restrict_xpaths = ''//a[contains(text(),"Next")]'), callback='parse', follow=True),)


    
    def parse(self, response):
        movies = response.xpath("//h3[@class='lister-item-header']/a/text()").extract()
        ratings = response.xpath('//div/div[1]/strong/text()').extract()
        Actors_1 = response.xpath('//*[@id="main"]/div/div/div/div/div/p/a[2]/text()').extract()
        Actors_2 = response.xpath('//*[@id="main"]/div/div/div/div/div/p/a[3]/text()').extract()
        Actors_3 = response.xpath('//*[@id="main"]/div/div/div/div/div/p/a[4]/text()').extract()
        genre = [i.strip() for i in response.xpath('//span[@class="genre"]/text()').extract()]
        Synopsis = [i.strip() for i in  response.xpath('//*[@id="main"]/div/div/div/div/div/p[2]/text()').extract()]
        for item in zip(movies,ratings,Actors_1,Actors_2,Actors_3,genre,Synopsis):
            yield{'Movies': item[0],
                  'Ratings': item[1],
                  'Actor 1' : item[2],
                  'Actor 2' : item[3],
                  'Actor 3' : item[4],
                  'Genres': item[5],
                  'Synopsis': item[6],
                  }
