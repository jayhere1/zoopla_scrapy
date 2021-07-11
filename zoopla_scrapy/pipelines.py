# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo
import os


class MongodbPipeline:
    collection_name = "zoopla_glasgow"

    def open_spider(self,spider):
        password = os.environ.get("password")
        self.client = pymongo.MongoClient(f"mongodb+srv://jay:{password}@cluster0.y4fw6.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        self.db = self.client["Zoopla"]

    def close_spider(self,spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[self.collection_name].insert(item)
        return item
