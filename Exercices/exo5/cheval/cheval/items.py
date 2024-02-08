# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ChevalItem(scrapy.Item):
    name = scrapy.Field()
    nomLatin = scrapy.Field()
    famille = scrapy.Field()
    espece = scrapy.Field()
    synonymes = scrapy.Field()
    pass
