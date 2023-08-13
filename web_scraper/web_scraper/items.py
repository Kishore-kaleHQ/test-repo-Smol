```python
import scrapy

class G2Item(scrapy.Item):
    # define the fields for your item here like:
    product_name = scrapy.Field()
    product_rating = scrapy.Field()
    product_reviews = scrapy.Field()
    product_category = scrapy.Field()
    product_description = scrapy.Field()
```