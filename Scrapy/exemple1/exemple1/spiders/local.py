import scrapy


class LocalSpider(scrapy.Spider):
    name = "local"
    allowed_domains = ["127.0.0.1:5500"]
    start_urls = ["http://127.0.0.1:5500/webScrapping3/Scrapy/exemple2/test.html", "http://127.0.0.1:5500/webScrapping3/Scrapy/Admin/admin.html"]

    def parse(self, response):

        res = response.css("div#footer > ul > li > a::attr('alt')").extract()
        print(res)

        res = response.css("div#footer > ul > li > a::text").extract()
        print(res)


        res = response.css("div#footer > ul > li > a::attr('alt')").extract()
        print(res)

        xres = response.xpath("//div[@id='footer']/ul/li/a/text()").extract()
        print(xres)

        xres = response.xpath("//div[@id='footer']/ul/li/a/@alt").extract()
        print(xres)

        xres = response.xpath("//div[@id='footer']/ul/li/a/@name").extract_first()
        print(xres)
        pass
