# -*- coding: utf-8 -*-
import scrapy


class TinhteCrawlSpider(scrapy.Spider):
    name = 'tinhte_crawl'
    allowed_domains = ['tinhte.vn']
    start_urls = ['http://tinhte.vn/']

    def parse(self, response):
        pass
