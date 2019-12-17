import scrapy

class searchSpider(scrapy.Spider):
    name = 'searchSpider'

    def start_requests(self):
        self.index = 0
        urls = [
            'http://reddit.com/r/cats'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self,response):
        for i in response.xpath('//a/@href'):
            img_url = i.extract()
            if img_url.endswith('.jpg') or img_url.endswith('.png'):
                print(img_url)
