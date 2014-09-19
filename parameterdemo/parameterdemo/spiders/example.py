# -*- coding: utf-8 -*-
import scrapy


class ExampleSpider(scrapy.Spider):
    name = "example"
    allowed_domains = ["dataisbeautiful.io"]

    def __init__(self, year=None, month=None, *args, **kwargs):
        super(ExampleSpider, self).__init__(*args, **kwargs)
        self.start_urls = ['http://www.dataisbeautiful.io/{!s}/{!s}/'.format(year, month)]

    def parse(self, response):
        print response.url
