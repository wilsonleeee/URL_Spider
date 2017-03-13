# coding: utf-8

from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy import Request
from Url.itms import UrlLink
import re


class DoubanSpider(Spider):
    name = 'url'
    allowed_domains = ['XXXXX.com']
    start_urls = ['http://XXXX.XXXX.com/']


    def parse(self, response):
        sel = Selector(response)
        links = sel.xpath('//a[@href]')
        
        for link in links:
            item = UrlLink()
            url = str(link.re(r'href="(.*?)"')[0])
            if url:
                if not url.startswith('http'):
                    url = response.url + url
                yield Request(url, callback=self.parse)
                item['link'] = url

                url_text = link.xpath('text()').extract()
                if url_text:
                    item[u'link_text'] = str(url_text[0].encode('utf-8').strip())
                else:
                    item[u'link_text'] = None
                yield item



