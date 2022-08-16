from atexit import register
import scrapy


class BikedetailsSpider(scrapy.Spider):
    name = 'bikedeails'
    allowed_domains = ['www.pakwheels.com']
    start_urls = ['https://www.pakwheels.com/used-bikes/honda-cd-70-2021-for-sale-in-islamabad-398699']

    def parse(self, response):
        price = response.css('.price-box strong::text').get()
        title = response.css('.well h1::text').get()
        location = response.css('.well p a::text').get()
        engine_data = response.css('.table.table-bordered.text-center.table-engine-detail.fs16  p::text').getall()
        features = response.css('.table.table-featured.nomargin td::text').getall()
        body_type = response.css('.table.table-featured.nomargin td a::text').get()         
        engine_year, engine_millage, engine_type = engine_data
        registered_in, last_updated, ad_refrence = features[1], features[3], features[6]
        
        bike_details = {
            'Price': price,
            'Title': title,
            'Location': location,
            'Engine Year': engine_year,
            'Engine Millage': engine_millage,
            'Engine Type': engine_type,
            'Registered In': registered_in,
            'Last Updated': last_updated,
            'Body Type': body_type,
            'Ad Ref #': ad_refrence
        }

        yield bike_details 
