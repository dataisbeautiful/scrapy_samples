# -*- coding: utf-8 -*-
import scrapy
import urllib
from HTMLParser import HTMLParser

class ExampleSpider(scrapy.Spider):
    name = "example"
    allowed_domains = ["dataisbeautiful.io"]
    start_urls = (
        'http://www.dataisbeautiful.io/',
    )

    def parse(self, response):
        p = PyOpenGraphParser()
        self.metadata = []
        ogmeta = unicode(response.body.decode(response.encoding)).encode('utf-8')
        p.feed(ogmeta)
        self.metadata = p.properties
        print self.metadata
        p.close()
        pass


class PyOpenGraphParser(HTMLParser):
    
    def __init__(self):
        HTMLParser.__init__(self)
        self.properties = {}
    
    def handle_starttag(self, tag, attrs):
        if tag == 'meta':
            attrdict = dict(attrs)
            if attrdict.has_key('property') and attrdict['property'].startswith('og:') and attrdict.has_key('content'):
                self.properties[attrdict['property'].replace('og:', '')] = attrdict['content']

    def handle_endtag(self, tag):
        pass
    
    def error(self, msg):
        pass
