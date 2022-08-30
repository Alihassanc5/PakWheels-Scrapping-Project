from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BikeSpider(CrawlSpider):
    name = 'Bike'
    allowed_domains = ['www.pakwheels.com']
    start_urls = ['https://www.pakwheels.com/used-bikes/search/-/']
    
    rules = (
        Rule(
            LinkExtractor(restrict_css='.search-title a'), callback='parse_bike', follow=False
        ),
        Rule(
            LinkExtractor(restrict_css='.next_page a'), follow=True
        )
    )
    

    def parse_bike(self, response):
        url = response.url
        price = response.css('.price-box strong::text').get()
        unit = response.css('.price-box strong span::text').get()
        try:
            if unit is None:
                price = int(price[3:].replace(',', ''))
            elif unit == 'lacs':
                price = int(float(price[3:])*100000)
            else:
                price = int(float(price[3:])*10000000)
        except:
            price = 'N/A'

        title = response.css('.well h1::text').get()
        brand = title[:title.find(' ')]
        variant = title[title.find(' ')+1:-5]
        model = int(title[-4:]) 
        location = response.css('.well p a::text').get()
        if ',' in location:
            area = location[:location.find(',')]
            location = location[location.find(',')+2:]            
        else:
            area = 'N/A'

        city = location[:location.find(' ')]
        province = location[location.find(' ')+1:]
        engine_year = int(response.css('.engine-icon.year + p::text').get())
        engine_mileage = int(response.css('.engine-icon.millage + p::text').get().replace(',','')[:-3])
        engine_type = response.css('.engine-icon.type + p::text').get()
        registered_in = response.css('.table.table-featured.nomargin td:first-child + td::text').get()
        body_type = response.css('.table.table-featured.nomargin td a::text').get()
        
        yield {
            'url': url,
            'price': price,
            'title': title,
            'brand': brand,
            'variant': variant,
            'model': model,
            'area': area,
            'city': city,
            'province': province,
            'engine_year': engine_year,
            'engine_mileage': engine_mileage,
            'engine_type': engine_type,
            'registered_in': registered_in,
            'body_type': body_type,
        }
