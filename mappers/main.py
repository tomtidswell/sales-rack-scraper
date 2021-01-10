import requests
import re
from bs4 import BeautifulSoup

class NothingScraped(Exception):
    pass


class NothingParsed(Exception):
    pass

class NothingMapped(Exception):
    pass

class SaveError(Exception):
    def __init__(self, response, message="Failed to save to API"):
        self.response = response
        self.status_code = response.status_code
        self.message = message
        print(message, self.response, self.status_code, self.response.json())


class Mapper:
    def __init__(self, scraped_data=[], site="", feedname="", retailer="", category=""):
        # dbclient = MongoClient('mongodb://localhost/')
        # sales_data = dbclient["sales"]
        # self.collection = sales_data["products"]
        self.site = site
        self.feedname = feedname
        self.retailer = retailer
        self.category = category
        self.scraped_data = scraped_data
        self.parsed_products = []
        self.mapped_products = []
        self.success_count = 0
        self.failure_count = 0
        self.begin()

    def begin(self):
        # check we have scraped data
        if not self.scraped_data:
            raise NothingScraped("No scraped data was found by the mapper")
        # parse each scraped record
        for product in self.scraped_data:
            self.parse_product_data(product)
        # check we parsed some data
        if not self.parsed_products:
            raise NothingParsed("No data was parsed from the scrape")
        # map each parsed item
        for product in self.parsed_products:
            self.map_product_data(product)
        # check we mapped something
        if not self.mapped_products:
            raise NothingMapped(
                "No mapped data was identified before saving to database")
        
        self.success_count = 0
        self.failure_count = 0
        # save into the database
        for product in self.mapped_products:
            success = self.save_product_data(product)
            if success:
                self.success_count+=1
            else:
                self.failure_count+=1

        self.save_stats()

    def save_product_data(self, product_data):
        success = False
        try:
            res = requests.put('http://localhost:4000/api/products', json=product_data)
            if res.status_code != 202:
                raise SaveError(res)
            else:
                print("Success saving", product_data['name'])
                success = True
        except Exception as e:
            print("Failure saving", product_data['name'], e)

        return success

    def save_stats(self):
        print('Successes:', self.success_count)
        print('Failures:', self.failure_count)
        print('Total products scraped:', len(self.mapped_products))
