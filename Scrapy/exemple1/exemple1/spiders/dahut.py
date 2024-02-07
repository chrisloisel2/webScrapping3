import scrapy


class DahutSpider(scrapy.Spider):
    name = "dahut"
    allowed_domains = ["fr.wikipedia.org"]
    start_urls = ["https://fr.wikipedia.org/wiki/Dahut"]

    def parse(self, response):
        obj = response.css("h1#firstHeading > span.mw-page-title-main::text").get()
        print(obj)
        yield {
			"title": obj,
		}
