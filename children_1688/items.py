# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Children1688Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    '''
     purchaseIndex1688 1688采购指数
     purchaseIndexTb 淘宝采购指数
     supplyIndex   1688供应指数
      category1	 category2　　　　time	          line_Type	                      value　　　　crawl_Time
		童装	　      所有　　　　2018/9.27  　　 1688采购指数/淘宝采购指数/1688供应指数　　32191　　　2019/9.30
    '''

    category1 = scrapy.Field()
    category2 = scrapy.Field()
    showtime = scrapy.Field()
    line_Type = scrapy.Field()
    value = scrapy.Field()
    crawl_Time = scrapy.Field()


class SecondIndexItem(scrapy.Item):
    purchaseIndex1688 = scrapy.Field()
    supplyIndex = scrapy.Field()
    demandForecast = scrapy.Field()
