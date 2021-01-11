import requests
from bs4 import BeautifulSoup

from .main_mapper import Mapper

class MarksAndSpencerMapper(Mapper):

    def parse_product_data(self, product_element):
        """Extracts product data from HTML element."""
        p = BeautifulSoup(product_element, 'html.parser')
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
        p_data['images'] = [{'source': img['src'], 'class': img['class']}
                            for img in p.find_all('img')]
        print('Parsed data', p_data)
        print("------")
        self.parsed_products.append(p_data)

    def map_product_data(self, product_data):
        """Extracts and prints out product information."""
        p_data = {}
        p_data['name'] = product_data['name']
        price_data = {}
        # if len(product_data['prices']) == 3:
        price_data['priceDescription'] = product_data['prices'][0]
        price_data['price'] = product_data['prices'][1]
        if len(product_data['prices']) >= 4:
            price_data['prevPriceDescription'] = product_data['prices'][2]
            price_data['prevPrice'] = product_data['prices'][3]
        
        if product_data['badge']:
            price_data['badge'] = product_data['badge']

        p_data['priceData'] = price_data
        p_data['url'] = product_data['url']
        for img in product_data['images']:
            if 'product__image--view' in img['class']:
                p_data['main_image'] = img['source']
            elif 'product__image--hover' in img['class']:
                p_data['hover_image'] = img['source']
        p_data['source'] = self.feedname
        p_data['category'] = self.category
        p_data['retailer'] = self.retailer
        print('Mapped data', p_data)
        print("------")
        self.mapped_products.append(p_data)
