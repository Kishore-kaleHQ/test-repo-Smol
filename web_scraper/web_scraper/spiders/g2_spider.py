```python
import scrapy
from scrapy.http import Request
from web_scraper.web_scraper.items import G2Item

class G2Spider(scrapy.Spider):
    name = 'g2_spider'
    allowed_domains = ['g2.com']
    start_urls = ['http://g2.com/']

    def parse(self, response):
        items = response.xpath('//div[@class="item"]')
        for item in items:
            g2_item = G2Item()
            g2_item['title'] = item.xpath('.//h2/a/text()').extract_first()
            g2_item['link'] = item.xpath('.//h2/a/@href').extract_first()
            yield g2_item

        next_page = response.xpath('//a[@class="next"]/@href').extract_first()
        if next_page:
            yield Request(response.urljoin(next_page), callback=self.parse)
```