# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LimoonadItem(scrapy.Item):
    # define the fields for your item here like:
    img = scrapy.Field()
    title = scrapy.Field()
    time = scrapy.Field()
    teacher = scrapy.Field()   
    price = scrapy.Field()
    url = scrapy.Field()

