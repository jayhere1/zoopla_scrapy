from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from zoopla_scrapy.spiders.zoopla_glasgow import ZooplaGlasgowSpider

process = CrawlerProcess(settings=get_project_settings())
process.crawl(ZooplaGlasgowSpider)

process.start()
