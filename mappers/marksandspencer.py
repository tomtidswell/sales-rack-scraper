import requests
from bs4 import BeautifulSoup
import re

from .main_mapper import Mapper

class MarksAndSpencerMapper(Mapper):

    def parse_product_data(self, product_element):
        """Extracts product data from HTML element."""
        p = BeautifulSoup(product_element, 'html.parser')
        print(p)
        p_data = {}
        p_data['name'] = p.find(class_='product__title').text
        p_data['prices'] = []
        prices = p.find_all(class_='price')
        if prices:
            for price in prices:
                for child in price.descendants:
                    if isinstance(child, type('bs4.element.NavigableString')):
                        p_data['prices'].append(child.string)
        p_data['url'] = f"{self.site}{p.a['href']}"
        p_data['badge'] = p.find(class_='product__badge').text if p.find(class_='product__badge') else None

        images = p.find_all('img', class_="product__image--view")
        p_data['image'] = images[0]['src'] if len(images) else None
        
        # p_data['images'] = [{'source': img['src'], 'class': img['class']}
        #                     for img in p.find_all('img')]
        print('Parsed data', p_data)
        print("------")
        self.parsed_products.append(p_data)

    def map_product_data(self, product_data):
        """Extracts and prints out product information."""
        p_data = {}
        p_data['name'] = product_data['name']
        # if len(product_data['prices']) == 3:
        p_data['priceArray'] = product_data['prices']
        p_data['price'] = product_data['prices'][1]
        if len(product_data['prices']) >= 4:
            p_data['prevPrice'] = product_data['prices'][3]
        
        if product_data['badge']:
            p_data['badge'] = product_data['badge']

        p_data['url'] = product_data['url']
        p_data['image'] = product_data['image']
        # for img in product_data['images']:
        #     if 'product__image--view' in img['class']:
        #         p_data['main_image'] = img['source']
        #     elif 'product__image--hover' in img['class']:
        #         p_data['hover_image'] = img['source']
        p_data['source'] = self.page
        p_data['category'] = self.category
        p_data['retailer'] = self.retailer
        print('Mapped data', p_data)
        print("------")
        self.mapped_products.append(p_data)
