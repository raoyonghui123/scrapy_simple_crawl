# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import logging
import random

class ItcastSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)

class ProxyMiddleWare(object):
    proxy_list=[
	'http://113.123.8.128:808',
	'http://182.46.217.90:808', 
	'http://113.122.6.225:808', 
	'http://120.76.55.49:8088', 
	'http://106.9.170.112:808', 
	'http://223.240.210.40:808', 
	'http://60.11.255.76:808', 
	'http://101.68.73.54:53281', 
	'http://106.14.241.155:80', 
	'http://118.114.77.47:8080']


    logger = logging.getLogger(__name__)
    def process_request(self, request, spider):
	ip = random.choice(self.proxy_list)
	self.logger.debug('using proxy:'+ ip)
	request.meta['proxy'] = ip
