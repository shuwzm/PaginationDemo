# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class PageSpider(CrawlSpider):
    name = 'page'
    allowed_domains = ['www.bestbuy.com']
    #start_urls = ['https://www.bestbuy.com/site/promo/latest-ipad-pro']
    start_urls = [
        'https://www.bestbuy.com/site/searchpage.jsp?st=ps4&_dyncharset=UTF-8&_dynSessConf=&id=pcat17071&type=page&sc'
        '=Global&cp=1&nrp=&sp=&qp=&list=n&af=true&iht=y&usc=All+Categories&ks=960&keys=keys']

    # rules = (
    #     Rule(LinkExtractor(restrict_xpaths='//*[@class="paging-list"]//a/@href'), callback='parse_rest'),
    # )

    def parse(self, response):
        print('this is the first page %s', response.url)
        next_page_url = response.xpath(
            '//*[@class="sku-list-page-next"]/@href').extract_first()
        if next_page_url:
            yield scrapy.Request(next_page_url, callback=self.parse)
        pass
