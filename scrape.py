from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
# from pprint import pprint
# import csv
import requests
# from requests_html import HTMLSession
from bs4 import BeautifulSoup
# from pymongo import MongoClient

# mydict = {
#     "name": "Pure Cotton Luxury Spa Towel",
#     "prices": ['Sale price', '£6.00 - £18.00', 'Previous price'],
#     "url": "https://www.marksandspencer.com/pure-cotton-luxury-spa-towel/p/hbp60467039?color=WHITE#intid=prodColourId-60467042",
#     "badge": "40% off"
# }
# collection.insert_one(mydict)


site = "https://www.marksandspencer.com"
page = "/l/offers/home-offers"


class NothingScraped(Exception):
    pass


class NothingParsed(Exception):
    pass


class NothingMapped(Exception):
    pass


class MarksAndSpencerScraper:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get(f"{site}{page}")

    def close_browser(self):
        self.driver.close()
        self.driver.quit()

    def handle_privacy(self):
        try:
            banner = self.driver.find_element_by_css_selector(
                ".privacy_prompt_footer")
            banner.click()
        finally:
            print('Found privacy', banner)

    def handle_pagination(self):
        pagination_available = True
        pagination = None
        while pagination_available:
            try:
                pagination = self.driver.find_element_by_css_selector(
                    ".grid__load-more > .pagination")
                # click it!
                pagination.click()
                print('Found load more', pagination_available, pagination)
            except Exception as e:
                pagination_available = False
                print('No load more found', e)

    def get_grid(self):
        """Extracts and returns company links (maximum number of company links for return is provided)."""

        self.wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "ul.grid")))

        scrolled_to = 0
        self.driver.execute_script(f"window.scrollTo(0, {scrolled_to})")
        body_height = self.driver.find_element(
            By.TAG_NAME, "body").get_attribute('offsetHeight')
        print('Page height:', body_height)
        while scrolled_to < int(body_height):
            scrolled_to += 200
            self.driver.execute_script(f"window.scrollTo(0, {scrolled_to})")

        return [el.get_attribute('innerHTML') for el in self.driver.find_elements_by_css_selector("ul.grid > li")]


class MarksAndSpencerMapper:
    def __init__(self, scraped_data=[]):
        # dbclient = MongoClient('mongodb://localhost/')
        # sales_data = dbclient["sales"]
        # self.collection = sales_data["products"]
        self.feedname = "marksandspencer-home"
        self.category = "homeware"
        self.retailer = "marksandspencer"
        self.scraped_data = scraped_data
        self.parsed_products = []
        self.mapped_products = []

    def begin_parse(self):
        # check we have scraped data
        if not self.scraped_data:
            raise NothingScraped("No scraped data was found by the mapper")
        # parse each scraped record
        for product in self.scraped_data:
            self.parse_product_data(product)
        # check we parsed some data
        if not self.scraped_data:
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
        p_data['name'] = p.find(class_='product__title').text
        p_data['prices'] = []
        print('Sale prices:', p.find(class_='price'))
        if p.find(class_='price'):
            for child in p.find(class_='price').descendants:
                if isinstance(child, type('bs4.element.NavigableString')):
                    p_data['prices'].append(child.string)
        p_data['url'] = f"{site}{p.a['href']}"
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
        if len(product_data['prices']) > 2:
            p_data['prevPriceDescription'] = product_data['prices'][2]
            p_data['prevPrice'] = product_data['prices'][3]
        
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

    def save_product_data(self, product_data):
        res = requests.put('http://localhost:4000/api/products', json=product_data)
        if res.status_code != 202:
            print(res, res.status_code, res.json(), dir(x))
        else:
            print("Success saving", product_data['name'])


if __name__ == '__main__':
    scraper = MarksAndSpencerScraper()
    print('Starting scrape')
    scraper.handle_privacy()
    scraper.handle_pagination()
    products = scraper.get_grid() or []
    scraper.close_browser()
    print('Finished scrape. Closing browser')
    # products = [
    #     '<a href="/percale-cotton-300-thread-count-duvet-cover/p/hbp60460724?color=WHITE" class="product " title="Product name is Percale 300 Thread Count Duvet Cover, 40% off, Previous price is , Sale price is £30.00 - £48.00, Available in 2 colours, Promotion description is Special offer" aria-label="Product name is Percale 300 Thread Count Duvet Cover, 40% off, Previous price is , Sale price is £30.00 - £48.00, Available in 2 colours, Promotion description is Special offer"><div class="product__image product__listing__image" aria-hidden="true"><div class="product__image--display"><img src="https://asset1.marksandspencer.com/is/image/mands/CL_05_T35_5152D_Z0_X_EC_0?wid=250&amp;qlt=80" alt="Percale 300 Thread Count Duvet Cover" class=" product__image--view portrait"><img src="https://asset1.marksandspencer.com/is/image/mands/CL_05_T35_5152D_Z0_X_EC_90?wid=250&amp;qlt=80" alt="Percale 300 Thread Count Duvet Cover" class=" product__image--hover portrait"></div><div class="product__badge"><span class="badge badge--sale">40% off</span></div></div><div class="product__details-link" aria-hidden="true"><div class="product__details"><h3 class="product__title">Percale 300 Thread Count Duvet Cover</h3><div class="sale-price"><p class="price price--reduced"><span class="acc__text">Sale price</span>£30.00 - £48.00</p><p class="price price--previous"><span class="acc__text">Previous price</span></p></div></div></div><div class="product__swatch"><a class="product__swatch__link" href="/percale-cotton-300-thread-count-duvet-cover/p/hbp60460724?color=WHITE#intid=plpnav_swatch"><img src="https://asset1.marksandspencer.com/is/image/mands/CL_05_T35_5152D_Z0_X_EC_88" alt="Percale 300 Thread Count Duvet Cover - white" class=" product__swatch__link-image portrait"></a><a class="product__swatch__link" href="/percale-cotton-300-thread-count-duvet-cover/p/hbp60460724?color=LIGHTGREY#intid=plpnav_swatch"><img src="https://asset1.marksandspencer.com/is/image/mands/CL_05_T35_5152D_T1_X_EC_88" alt="Percale 300 Thread Count Duvet Cover - lightgrey" class=" product__swatch__link-image portrait"></a><div class="product__swatch-label">2 colours available</div></div><div class="product__details" aria-hidden="true"><p class="star-rating"><span class="star-rating__base"><svg aria-hidden="true" width="89" height="12" viewBox="0 0 61 11" xmlns="http://www.w3.org/2000/svg" title="Star Rating"><g><path d="M2.101 11l.655-3.987L0 4.193l3.79-.584L5.512 0l1.723 3.644 3.79.584-2.757 2.819L8.923 11 5.512 9.11zM14.595 11l.655-3.987-2.756-2.82 3.79-.584L18.006 0l1.723 3.644 3.79.584-2.757 2.819.655 3.953-3.411-1.89zM27.09 11l.654-3.987-2.756-2.82 3.79-.584L30.5 0l1.723 3.644 3.789.584-2.756 2.819.655 3.953L30.5 9.11zM39.583 11l.655-3.987-2.756-2.82 3.79-.584L42.993 0l1.722 3.644 3.79.584-2.756 2.819.655 3.953-3.411-1.89zM52.077 11l.655-3.987-2.756-2.82 3.79-.584L55.487 0l1.722 3.644 3.79.584-2.756 2.819.655 3.953-3.411-1.89z"></path></g></svg></span><span class="star-rating__filled" style="width: calc(101.25%);"><svg aria-hidden="true" width="89" height="12" viewBox="0 0 61 11" xmlns="http://www.w3.org/2000/svg" title="Star Rating"><g><path d="M2.101 11l.655-3.987L0 4.193l3.79-.584L5.512 0l1.723 3.644 3.79.584-2.757 2.819L8.923 11 5.512 9.11zM14.595 11l.655-3.987-2.756-2.82 3.79-.584L18.006 0l1.723 3.644 3.79.584-2.757 2.819.655 3.953-3.411-1.89zM27.09 11l.654-3.987-2.756-2.82 3.79-.584L30.5 0l1.723 3.644 3.789.584-2.756 2.819.655 3.953L30.5 9.11zM39.583 11l.655-3.987-2.756-2.82 3.79-.584L42.993 0l1.722 3.644 3.79.584-2.756 2.819.655 3.953-3.411-1.89zM52.077 11l.655-3.987-2.756-2.82 3.79-.584L55.487 0l1.722 3.644 3.79.584-2.756 2.819.655 3.953-3.411-1.89z"></path></g></svg></span><span class="acc__text">Average rating: 5.0 out of 5</span></p><p class="product__offer">Special offer</p></div></a>'
    # ]
    mapper = MarksAndSpencerMapper(scraped_data=products)
    mapper.begin_parse()
