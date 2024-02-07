import scrapy


class LocalSpider(scrapy.Spider):
    name = "local"
    allowed_domains = ["127.0.0.1:5500"]
    start_urls = ["http://127.0.0.1:5500/webScrapping3/Scrapy/exemple2/test.html", "http://127.0.0.1:5500/webScrapping3/Scrapy/Admin/admin.html"]

    def parse(self, response):

        print(response.text)
        print("----------------------------")
        print("Bonjour")
        print("----------------------------")
        pass
