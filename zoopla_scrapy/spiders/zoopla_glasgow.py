import scrapy


class ZooplaGlasgowSpider(scrapy.Spider):
    name = 'zoopla_glasgow'
    allowed_domains = ['www.zoopla.co.uk']
    start_urls = ['http://www.zoopla.co.uk/for-sale/property/glasgow/?q=Glasgow&results_sort=newest_listings&search_source=home']

    def parse(self, response):
        for home in response.xpath('//div[@class="css-kdnpqc-ListingsContainer earci3d2"]/div'):
            price = home.xpath('.//div[@class="css-1e28vvi-PriceContainer e2uk8e8"]/p[2]/text()').get()
            if price:
                yield {
                    "House type": home.xpath('//div[@class="css-wfndrn-StyledContent e2uk8e18"]/a/h2/text()').get(),
                    "Address": home.xpath('.//div[@class="css-wfndrn-StyledContent e2uk8e18"]/a/p/text()').get(),
                    "Price": home.xpath('.//div[@class="css-1e28vvi-PriceContainer e2uk8e8"]/p[2]/text()').get()
                }

        next_page = response.xpath(
            '//li[@class="css-qhg1xn-PaginationItemPreviousAndNext-PaginationItemNext eaoxhri2"]/a/@href').get()

        if next_page:
            yield scrapy.Request(url=response.urljoin(next_page),
                                 callback=self.parse
                                 )
# scrapy crawl zoopla_glasgow -o dataset.json
