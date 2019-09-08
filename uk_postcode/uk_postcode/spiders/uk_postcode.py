import scrapy
from ..items import UkPostcodeItem

class uk_postcodeSpder(scrapy.Spider):
    name = "uk_postcode"
    start_urls = [
        'https://www.doogal.co.uk/UKPostcodes.php?Search=AB'
    ]

    def parse(self, response):

        code = UkPostcodeItem()

        sample_codes = response.css('table.postcodeTable')

        for codes in sample_codes:
           postcodes = codes.css('td a::text').extract()

           code['post'] = postcodes

           yield code


