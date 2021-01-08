# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CygItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    sect = scrapy.Field()
    sex = scrapy.Field()
    level = scrapy.Field()
    name = scrapy.Field()
    score = scrapy.Field()
    xiulian = scrapy.Field()
    jinjie = scrapy.Field()
    price = scrapy.Field()
    area = scrapy.Field()
    is_tag = scrapy.Field()
    pass
