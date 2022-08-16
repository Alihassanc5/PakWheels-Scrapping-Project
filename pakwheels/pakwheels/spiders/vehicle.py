from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class VehicleSpider(CrawlSpider):
    name = 'Bikes'
    allowed_domains = ['www.pakwheels.com']
    used_bikes_url = 'https://www.pakwheels.com/used-bikes/search/-/'
    
    start_urls = [
        used_bikes_url
    ]
    
    rules = (
        Rule(LinkExtractor(restrict_css='.search-title a'), callback='parse_item', follow=False),
        Rule(LinkExtractor(restrict_css='.next_page a'), follow=True)
    )

    def parse_item(self, response):
        url = response.url
        price = response.css('.price-box strong::text').get()
        title = response.css('.well h1::text').get()
        location = response.css('.well p a::text').get()
        engine_data = response.css('.table.table-bordered.text-center.table-engine-detail.fs16  p::text').getall()
        registered_in = response.css('.table.table-featured.nomargin td::text').getall()[1]
        body_type = response.css('.table.table-featured.nomargin td a::text').get()         
        engine_year, engine_millage, engine_type = engine_data 
        
        yield {
            'Url': url,
            'Price': price,
            'Title': title,
            'Location': location,
            'Engine Year': engine_year,
            'Engine Millage': engine_millage,
            'Engine Type': engine_type,
            'Registered In': registered_in,
            'Body Type': body_type,
        }
