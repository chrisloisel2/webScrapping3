import scrapyclass Exo1Spider(scrapy.Spider):
name = "exo1"
allowed_domains = ["127.0.0.1:5500"]
start_urls = ["http://127.0.0.1:5500/pratique/Special.html"]
def parse(self, response):

results = {}

# Extraire et afficher toutes les informations space-content

space_content_info = {}


# Extraire les articles

articles = response.css('#space-content article')

space_content_info['articles'] = []

for article in articles:


article_info = {}


article_info['title'] = article.css('h2::text').get()


article_info['paragraphs'] = article.css('p::text').extract()


space_content_info['articles'].append(article_info)


# Extraire les divs

divs = response.css('#space-content div')

space_content_info['divs'] = [div.extract() for div in divs]


# Extraire les éléments de la liste ul

ul_items = response.css('#space-content ul#mission-list li::text').extract()

space_content_info['ul'] = ul_items

results['space_content'] = space_content_info


# Récupérer et afficher le texte de toutes les balises <p> qui ont la classe space-highlight

space_highlight_paragraphs = response.css('p.space-highlight::text').extract()

results['space_highlight_paragraphs'] = space_highlight_paragraphs


# Sélectionnez et affichez le premier paragraphe (<p>) de chaque article (<article>)

first_paragraphs = response.css('article > p:first-of-type::text').extract()

results['first_paragraphs'] = first_paragraphs


# Extrayez et affichez tous les éléments impairs de la liste #mission-list

mission_list_items = response.css('#mission-list li:nth-child(odd)::text').extract()

results['mission_list_items'] = mission_list_items

# Récupérez et affichez le contenu de toutes les balises <div> qui n'ont pas la classe space-highlight

non_highlight_divs = response.css('div:not(.space-highlight)::text').extract()

results['non_highlight_divs'] = non_highlight_divs

# Utilisez une combinaison de sélecteurs pour extraire le texte de chaque titre <h2> dans les articles

article_h2s = response.css('article h2::text').extract()

results['article_h2s'] = article_h2s

yield results
