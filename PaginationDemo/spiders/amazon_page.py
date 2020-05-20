import scrapy
from scrapy.spiders import CrawlSpider, Rule

class AmazonPageSpider(CrawlSpider):
    name = "amazonPage"
    allowed_domains = "www.amazon.com"
    base_url = 'https://www.amazon.com'
    start_urls = ['https://www.amazon.com/s?k=ps4+game&page=2&qid=1589906338&ref=sr_pg_1']

    def parse(self, response):
        print(response.url)
        next_page_url = response.xpath('//ul[@class="a-pagination"]/li[@class="a-last"]/a/@href').extract_first()
        print(next_page_url)
        if next_page_url:
            next_page_url = self.base_url + next_page_url
            print('url is:', next_page_url )
            #dont_filter works
            yield scrapy.Request(next_page_url, callback=self.parse, dont_filter= True)
        else:
            print('reach the last page')
        pass