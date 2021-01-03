from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver


class MarksAndSpencerScraper:
    def __init__(self, site, page):
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

    def scroll_to_bottom(self):
        """Scrolls to the bottom of the page."""

        self.wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "ul.grid")))

        scrolled_to = 0
        self.driver.execute_script(f"window.scrollTo(0, {scrolled_to})")
        body_height = self.driver.find_element(
            By.TAG_NAME, "body").get_attribute('offsetHeight')

        while scrolled_to < int(body_height):
            scrolled_to += 200
            self.driver.execute_script(f"window.scrollTo(0, {scrolled_to})")
            # reset the body height just in case there is infinite scroll
            body_height = self.driver.find_element(
                By.TAG_NAME, "body").get_attribute('offsetHeight')

    def get_grid(self):
        return [el.get_attribute('innerHTML') for el in self.driver.find_elements_by_css_selector("ul.grid > li")]
