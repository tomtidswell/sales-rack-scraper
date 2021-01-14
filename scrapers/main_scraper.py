import requests

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver


class APIError(Exception):
    def __init__(self, response, message="Failed to save to API"):
        self.response = response
        self.status_code = response.status_code
        self.message = message
        print(message, self.response, self.status_code, self.response.json())


class APIConnectionError(Exception):
    def __init__(self, message="Could not access API"):
        print(message)



class Scraper:
    def __init__(self, site, retailer=""):
        self.site = site
        self.driver = webdriver.Chrome()
        self.retailer = retailer
        self.settings = {}
        self.products = []
        self.fetch_settings()
        self.begin()

    def begin(self):
        for page in self.settings:
            self.scrape_page(page)
        self.close_browser()
        print('Finished scrape. Closing browser')
    
    def scrape_page(self, config):
        page = config.get('page')
        category = config.get('category')
        privacySelector = config.get('privacySelector')
        gridItemSelector = config.get('gridItemSelector')
        paginationSelector = config.get('paginationSelector')
        print('Starting scrape')
        # self.wait = WebDriverWait(self.driver, 15)
        self.driver.get(f"{self.site}{page}")
        self.handle_privacy(privacySelector)
        self.scroll_to_bottom()
        self.handle_pagination(paginationSelector)
        products = self.get_grid(gridItemSelector) or []
        self.products.append({
            "products": products,
            "page": page,
            "category": category
        })
        print('Identified', len(products), 'products')

    def fetch_settings(self):
        res = None
        try:
            res = requests.get(
                f"http://localhost:4000/api/scrapesettings?retailer={self.retailer}"
            )
        except Exception as e:
            print("Failure fetching scrape settings", e)
        
        if not res:
            raise APIConnectionError()
        elif res.status_code != 200:
            raise APIError(res)
        else:
            self.settings = res.json()
            print("Success fetching scrape settings", res, self.settings)

    def close_browser(self):
        self.driver.close()
        self.driver.quit()
    
    def handle_privacy(self, selector):
        if not selector:
            return
        banner = None
        try:
            banner = self.driver.find_element_by_css_selector(selector)
        except Exception as e:
            print("Didn't find banner on first attempt", e)
        try:
            if not banner:
                banner = self.driver.find_element_by_css_selector(selector)
        except Exception as e:
            print("Didn't find banner on second attempt", e)

        if banner:
            print('Text:', banner.text)
            print('Found privacy', banner)
            banner.click()

    def handle_pagination(self, selector):
        if not selector:
            return
        pagination_available = True
        pagination = None
        while pagination_available:
            try:
                pagination = self.driver.find_element_by_css_selector(
                    ".grid__load-more > .pagination")
                # create action chain object
                action = ActionChains(self.driver)
                # perform the operation
                action.move_to_element(pagination).click().perform()
                # click it!
                # pagination.click()
                print('Found load more', pagination_available, pagination)
            except Exception as e:
                pagination_available = False
                print('No load more found', e)

    def scroll_to_bottom(self):
        """Scrolls to the bottom of the page."""

        scrolled_to = 0
        self.driver.execute_script(f"window.scrollTo(0, {scrolled_to})")
        body_height = self.driver.find_element(
            By.TAG_NAME, "body").get_attribute('offsetHeight')
        print("scrolled to the top")

        while scrolled_to < int(body_height):
            scrolled_to += 200
            self.driver.execute_script(f"window.scrollTo(0, {scrolled_to})")
            # reset the body height just in case there is infinite scroll
            body_height = self.driver.find_element(
                By.TAG_NAME, "body").get_attribute('offsetHeight')

    def get_grid(self, selector):
        if not selector:
            return
        return [el.get_attribute('innerHTML') for el in self.driver.find_elements_by_css_selector(selector)]
