# -*- coding: utf-8 -*-
import scrapy


class ExampleSpider(scrapy.Spider):
    name = "example"
    allowed_domains = ["dataisbeautiful.io"]
    start_urls = (
        'http://www.dataisbeautiful.io/',
    )

    def parse(self, response):
        pass
