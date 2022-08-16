import scrapy


class BikesSpider(scrapy.Spider):
    name = 'Bikes'
    allowed_domains = ['www.pakwheels.com']
    start_urls = ['https://www.pakwheels.com/used-bikes/honda-cd-70/56630']

    def parse(self, response):
        bike_links = response.css('li .search-title a::attr(href)').getall()
        for bike_link in bike_links:
            Link = {
                'Bike Link': bike_link
            }
            yield Link
            
