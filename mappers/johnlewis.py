import requests
import re
from bs4 import BeautifulSoup

class NothingScraped(Exception):
    pass


class NothingParsed(Exception):
    pass


class NothingMapped(Exception):
    pass


class JohnLewisMapper:
    def __init__(self, scraped_data=[], site=""):
        # dbclient = MongoClient('mongodb://localhost/')
        # sales_data = dbclient["sales"]
        # self.collection = sales_data["products"]
        self.feedname = "johnlewis-tableware"
        self.category = "tableware"
        self.retailer = "johnlewis"
        self.scraped_data = scraped_data
        self.parsed_products = []
        self.mapped_products = []
        self.site = site

    def begin_parse(self):
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
        # save into the database
        for product in self.mapped_products:
            self.save_product_data(product)

    def parse_product_data(self, product_element):
        """Extracts product data from HTML element."""
        p = BeautifulSoup(product_element, 'html.parser')
        p_data = {}

        # check for a grid separator
        if p.select_one("aside"):
            print("SEPARATOR")
            return

        p_data['name'] = p.select_one("div[data-test='product-title']").text
        p_data['prices'] = []
        price_el = p.find(class_=re.compile("price_c-product-card__price*"))
        if price_el:
            for child in price_el.descendants:
                if isinstance(child, type('bs4.element.NavigableString')) and child.string and child.string != ' ':
                    p_data['prices'].append(child.string)
        
        p_data['url'] = f"{self.site}{p.a['href']}"
        # p_data['badge'] = p.find(class_='product__badge').text if p.find(class_='product__badge') else None
        # use regex to match on a partial class name
        p_data['badge'] = p.find(class_=re.compile("promo-messages*")).text

        print(p.find_all('img'))
        p_data['images'] = [{'source': f"http:{img['src']}", 'class': img.get('class')}
                            for img in p.find_all('img')]

        print('Parsed data', p_data)
        print("------")
        self.parsed_products.append(p_data)

    def map_product_data(self, product_data):
        """Extracts and prints out product information."""
        p_data = {}
        p_data['name'] = product_data['name']
        price_data = {}
        if len(product_data['prices']) == 1:
            price_data['price'] = product_data['prices'][0]
        else:
            price_data['prevPriceDescription'] = product_data['prices'][0]
            price_data['prevPrice'] = product_data['prices'][1]
            price_data['priceDescription'] = product_data['prices'][2]
            price_data['price'] = product_data['prices'][3]
        
        if product_data['badge']:
            price_data['badge'] = product_data['badge']

        p_data['priceData'] = price_data
        p_data['url'] = product_data['url']
        for img in product_data['images']:
            if img['class'] and 'image_image__E2_gC' in img['class']:
                p_data['main_image'] = img['source']
            elif img['class'] and 'product__image--hover' in img['class']:
                p_data['hover_image'] = img['source']
        p_data['source'] = self.feedname
        p_data['category'] = self.category
        p_data['retailer'] = self.retailer
        print('Mapped data', p_data)
        print("------")
        self.mapped_products.append(p_data)

    def save_product_data(self, product_data):
        try:
            res = requests.put('http://localhost:4000/api/products', json=product_data)
            if res.status_code != 202:
                print("Failure saving", res, res.status_code, res.json(), dir(x))
            else:
                print("Success saving", product_data['name'])
        except Exception as e:
            print("Failure saving", product_data['name'], e)
