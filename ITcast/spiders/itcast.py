# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from ITcast.items import ItcastItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class ItcastSpider(CrawlSpider):
    name = 'itcast'
#    allowed_domains = ['http://www.itcast.cn']
    start_urls = ['https://tw.appledaily.com/new/realtime']
    rules = [
    	Rule(LinkExtractor(allow=('/new/realtime/[1-3]$')), callback='parse_list', follow = True) # crawl 1-3 pages
    ]

    def parse_list(self, response):
	res = BeautifulSoup(response.body)
	for news in res.find_all(class_='rtddt'): #find out the tags with class rtddt
	    #print news.select('a')[0]['href']
	    yield scrapy.Request(news.select('a')[0]['href'], self.parse_detail)

    def parse_detail(self, response):
	res = BeautifulSoup(response.body)
	itcastItem = ItcastItem()
	itcastItem['title'] = res. select('h1')[0].text
	itcastItem['content'] = res.select('p')[0].text
	itcastItem['time'] = res.select('.ndArticle_creat')[0].text
	return itcastItem
	#print res.select('h1')[0].text
