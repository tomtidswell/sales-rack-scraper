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
        p_data['prices'] = []
        current_price = p.select_one("p[data-testid='price']")
        previous_price = p.select_one("p[data-testid='wasPrice']")
        if current_price:
            p_data['prices'].append(current_price.text)
        if previous_price:
            p_data['prices'].append(previous_price.text)
        
        p_data['url'] = f"{self.site}{p.a['href']}"
        p_data['badge'] = ""

        print(p.select("img[data-testid='product-image']"))
        p_data['images'] = [{'source': f"{img['src']}", 'class': img.get('class')}
                            for img in p.select("img[data-testid='product-image']")]

        print('Parsed data', p_data)
        print("------")
        self.parsed_products.append(p_data)

    def map_product_data(self, product_data):
        """Extracts and prints out product information."""
        p_data = {}
        p_data['name'] = product_data['name']
        price_data = {}
        price_data['price'] = product_data['prices'][0]
        if len(product_data['prices']) == 2:
            price_data['prevPrice'] = product_data['prices'][1]
        elif len(product_data['prices']) == 0:
            print('No price data extracted')
        
        if product_data['badge']:
            price_data['badge'] = product_data['badge']

        p_data['priceData'] = price_data
        p_data['url'] = product_data['url']
        for img in product_data['images']:
            if img['class'] and 'product-image' in img['class']:
                p_data['main_image'] = img['source']
        p_data['source'] = self.page
        p_data['category'] = self.category
        p_data['retailer'] = self.retailer
        print('Mapped data', p_data)
        print("------")
        self.mapped_products.append(p_data)

