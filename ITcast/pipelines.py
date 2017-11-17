# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3

class ItcastPipeline(object):
    def open_spider(self, spider):
	self.conn = sqlite3.connect('itcast.sqlite')
	self.cur = self.conn.cursor()
	self.cur.execute('create table if not exists itcast(title varchar(100), content text, time varchar(50))')
    def close_spider(self, spider):
	self.conn.commit()
	self.conn.close()
	#pass
    def process_item(self, item, spider):
	col = ','.join(item.keys())
	placeholders = ','.join(len(item) * '?')
	sql = 'insert into itcast({}) values({})'
	self.cur.execute(sql.format(col, placeholders), item.values())
        return item
