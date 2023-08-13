```python
from scrapy.crawler import CrawlerProcess
from web_scraper.web_scraper.spiders.g2_spider import G2Spider

def run_spider():
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
        'FEED_FORMAT': 'json',
        'FEED_URI': 'result.json'
    })

    process.crawl(G2Spider)
    process.start()

if __name__ == "__main__":
    run_spider()
```