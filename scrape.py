import sys

from scrapers.marksandspencer import MarksAndSpencerScraper
from scrapers.johnlewis import JohnLewisScraper
from scrapers.dunelm import DunelmScraper

from mappers.marksandspencer import MarksAndSpencerMapper
from mappers.johnlewis import JohnLewisMapper
from mappers.dunelm import DunelmMapper

# from pprint import pprint
# import csv

# from requests_html import HTMLSession


def scrapeMarksAndSpencer(retailer, site):
    scraper = MarksAndSpencerScraper(site=site, retailer=retailer)
    products_by_category = scraper.products
    for item in products_by_category:
        page = item.get('page')
        category = item.get('category')
        products = item.get('products')
        print(page, category, len(products))
        mapper = MarksAndSpencerMapper(
            scraped_data=products,
            site=site,
            page=page,
            retailer=retailer,
            category=category
        )


def scrapeJohnLewis(retailer, site):
    scraper = JohnLewisScraper(site=site, retailer=retailer)
    products_by_category = scraper.products
    for item in products_by_category:
        page = item.get('page')
        category = item.get('category')
        products = item.get('products')
        print(page, category, len(products))
        mapper = JohnLewisMapper(
            scraped_data=products,
            site=site, 
            page=page, 
            retailer=retailer,
            category=category
        )

def scrapeDunelm(retailer, site):
    scraper = DunelmScraper(site=site, retailer=retailer)
    products_by_category = scraper.products
    for item in products_by_category:
        page = item.get('page')
        category = item.get('category')
        products = item.get('products')
        print(page, category, len(products))
        mapper = DunelmMapper(
            scraped_data=products,
            site=site, 
            page=page, 
            retailer=retailer,
            category=category
        )


retailer_config = {
    "marksandspencer": {"method": scrapeMarksAndSpencer, "site": "https://www.marksandspencer.com"},
    "johnlewis": {"method": scrapeJohnLewis, "site": "https://www.johnlewis.com"},
    "dunelm": {"method": scrapeDunelm, "site": "https://www.dunelm.com"},
}


if __name__ == '__main__':
    retailer = sys.argv[1:][0]
    if not retailer:
        raise Exception('No retailer specified')
    config = retailer_config.get(retailer)
    if not config:
        raise Exception('No retailer config found')
    
    print('Begining scrape of', retailer)
    config["method"](retailer=retailer, site=config["site"])


