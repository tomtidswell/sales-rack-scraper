import requests
import re
from bs4 import BeautifulSoup

from .main_mapper import Mapper

class JohnLewisMapper(Mapper):

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
        badge_data = p.find(class_=re.compile("promo-messages*"))
        p_data['badge'] = badge_data.text if badge_data else ""

        # print(p.find_all('img'))
        # p_data['images'] = [{'source': f"http:{img['src']}", 'class': img.get('class')}
                            # for img in p.find_all('img')]

        images = p.find_all('img', class_="image_image__E2_gC")
        p_data['image'] = images[0]['src'] if len(images) else None


        print('Parsed data', p_data)
        print("------")
        self.parsed_products.append(p_data)

    def map_product_data(self, product_data):
        """Extracts and prints out product information."""
        p_data = {}
        p_data['name'] = product_data['name']

        if len(product_data['prices']) == 1:
            p_data['price'] = product_data['prices'][0]
        elif len(product_data['prices']) == 0:
            print('No price data extracted')
        else:
            p_data['prevPrice'] = product_data['prices'][1]
            p_data['price'] = product_data['prices'][3]
        
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

