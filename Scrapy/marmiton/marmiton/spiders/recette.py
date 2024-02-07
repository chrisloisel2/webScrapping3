import scrapy
from marmiton.items import MarmitonItem

class RecetteSpider(scrapy.Spider):
    name = "recette"
    allowed_domains = ["www.cuisineaz.com"]
    start_urls = ["https://www.cuisineaz.com/categories/aperitif/chips-cat48645"]

    def parse(self, response):
        item = MarmitonItem()

        nomRecette = response.css("h1::text").extract_first()
        print(nomRecette)
        item['nomRecette'] = nomRecette
        yield item
