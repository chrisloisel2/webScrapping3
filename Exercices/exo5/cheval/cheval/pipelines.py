# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo


class ChevalPipeline:
    # fonction au lancement de ma spider
    def open_spider(self, spider):
        print("Début du scraping")
        self.client = pymongo.MongoClient(
            "mongodb+srv://christoloisel:Rose230323@cluster0.soahdz4.mongodb.net/")
        self.db = self.client["cheval"]  # Nom de votre base de données



    def process_item(self, item, spider):
        print(item["name"])
        print(item["nomLatin"])
        print(item["famille"])
        # ajout dans la base de données
        self.db["chevaux"].insert_one(dict(item))
        return item

    # fonction à la fin de ma spider
    def close_spider(self, spider):
        print("Fin du scraping")
