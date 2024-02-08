import scrapy
from cheval.items import ChevalItem


class SpiderchevalSpider(scrapy.Spider):
    name = "spidercheval"
    allowed_domains = ["fr.wikipedia.org"]
    start_urls = ["https://fr.wikipedia.org/wiki/Cheval"]

    def parse(self, response):
        item = ChevalItem()

        item["name"] = "cheval"
        item["nomLatin"] = "chevalus"
        item["famille"] = "yolo"

        yield item
