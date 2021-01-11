# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium import webdriver

from .main_scraper import Scraper


class JohnLewisScraper(Scraper):

    def get_grid(self):
        return [el.get_attribute('innerHTML') for el in self.driver.find_elements_by_css_selector("div[data-test='component-grid-container'] > div[data-test='component-grid-column']")]
