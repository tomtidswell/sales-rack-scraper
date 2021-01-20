import requests
import re
from bs4 import BeautifulSoup

from .main_mapper import Mapper

class DunelmMapper(Mapper):

    def parse_product_data(self, product_element):
        """Extracts product data from HTML element."""
        p = BeautifulSoup(product_element, 'html.parser')
        p_data = {}
        print(product_element)
        p_data['name'] = p.select_one("p[data-testid='product-title']").text

        current_price = p.select_one("p[data-testid='price']")
        previous_price = p.select_one("p[data-testid='wasPrice']")
        if current_price:
            p_data['price'] = current_price.text
        if previous_price:
            p_data['prevPrice'] = previous_price.text
        
        p_data['url'] = f"{self.site}{p.a['href']}"
        p_data['badge'] = ""

        images = p.select("img[data-testid='product-image']")
        p_data['image'] = images[0]['src'] if len(images) else None

        print('Parsed data', p_data)
        print("------")
        self.parsed_products.append(p_data)

    def map_product_data(self, product_data):
        """Extracts and prints out product information."""
        p_data = {}
        p_data['name'] = product_data['name']
        p_data['price'] = product_data['price']
        if product_data['prevPrice']:
            p_data['prevPrice'] = product_data['prevPrice']
        
        if product_data['badge']:
            p_data['badge'] = product_data['badge']

        p_data['url'] = product_data['url']
        p_data['image'] = product_data['image']
        p_data['source'] = self.page
        p_data['category'] = self.category
        p_data['retailer'] = self.retailer
        print('Mapped data', p_data)
        print("------")
        self.mapped_products.append(p_data)

