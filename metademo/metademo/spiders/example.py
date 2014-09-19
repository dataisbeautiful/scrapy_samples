# -*- coding: utf-8 -*-
import scrapy
from metademo.items import MetademoItem

class ExampleSpider(scrapy.Spider):
    name = "example"
    allowed_domains = ["tutorialspoint.com"]
    start_urls = (
        'http://www.tutorialspoint.com/html/html_meta_tags.htm',
    )

    def parse(self, response):
        item = MetademoItem()
        item['title'] = response.xpath('//title/text()').extract()
        item['description'] = response.xpath('//meta[contains(@name, "escription")]/@content').extract()
        item['keywords'] = response.xpath('//meta[contains(@name, "eywords")]/@content').extract()
        return item
