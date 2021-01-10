from scrapers.marksandspencer import MarksAndSpencerScraper
from scrapers.johnlewis import JohnLewisScraper

from mappers.marksandspencer import MarksAndSpencerMapper
from mappers.johnlewis import JohnLewisMapper

# from pprint import pprint
# import csv

# from requests_html import HTMLSession

def scrapeMarksAndSpencer():
    site = "https://www.marksandspencer.com"
    page = "/l/offers/sale/home-sale"
    scraper = MarksAndSpencerScraper(site, page)
    print('Starting scrape')
    scraper.handle_privacy(banner_selector=".privacy_prompt_footer")
    scraper.handle_pagination()
    scraper.scroll_to_bottom()
    products = scraper.get_grid() or []
    print('Identified', len(products), 'products')
    # scraper.close_browser()
    print('Finished scrape. Closing browser')
    # products = [
    #     '<a href="/goose-feather-and-down-10-5-tog-duvet/p/hbp60440537?color=WHITE" class="product " title="Product name is Goose Feather &amp; Down 10.5 Tog Duvet, Current price is £70.00 - £115.00, Available in 1 colour" aria-label="Product name is Goose Feather &amp; Down 10.5 Tog Duvet, Current price is £70.00 - £115.00, Available in 1 colour"><div class="product__image product__listing__image" aria-hidden="true"><div class="product__image--display"><img src="https://asset1.marksandspencer.com/is/image/mands/PL_05_T35_5417A_Z0_X_EC_0?wid=285&amp;qlt=80" alt="Goose Feather &amp; Down 10.5 Tog Duvet" class=" product__image--view portrait"><img src="https://asset1.marksandspencer.com/is/image/mands/PL_05_T35_5417A_Z0_X_EC_90?wid=285&amp;qlt=80" alt="Goose Feather &amp; Down 10.5 Tog Duvet" class=" product__image--hover portrait"></div></div><div class="product__details-link" aria-hidden="true"><div class="product__details"><h3 class="product__title">Goose Feather &amp; Down 10.5 Tog Duvet</h3><div class="product__price"><div class="price product__price--current"><h4 class="acc__text">Current Price</h4>£70.00 - £115.00</div></div></div></div><div class="product__details" aria-hidden="true"><p class="star-rating"><span class="star-rating__base"><svg aria-hidden="true" width="89" height="12" viewBox="0 0 61 11" xmlns="http://www.w3.org/2000/svg" title="Star Rating"><g><path d="M2.101 11l.655-3.987L0 4.193l3.79-.584L5.512 0l1.723 3.644 3.79.584-2.757 2.819L8.923 11 5.512 9.11zM14.595 11l.655-3.987-2.756-2.82 3.79-.584L18.006 0l1.723 3.644 3.79.584-2.757 2.819.655 3.953-3.411-1.89zM27.09 11l.654-3.987-2.756-2.82 3.79-.584L30.5 0l1.723 3.644 3.789.584-2.756 2.819.655 3.953L30.5 9.11zM39.583 11l.655-3.987-2.756-2.82 3.79-.584L42.993 0l1.722 3.644 3.79.584-2.756 2.819.655 3.953-3.411-1.89zM52.077 11l.655-3.987-2.756-2.82 3.79-.584L55.487 0l1.722 3.644 3.79.584-2.756 2.819.655 3.953-3.411-1.89z"></path></g></svg></span><span class="star-rating__filled" style="width: calc(98.175%);"><svg aria-hidden="true" width="89" height="12" viewBox="0 0 61 11" xmlns="http://www.w3.org/2000/svg" title="Star Rating"><g><path d="M2.101 11l.655-3.987L0 4.193l3.79-.584L5.512 0l1.723 3.644 3.79.584-2.757 2.819L8.923 11 5.512 9.11zM14.595 11l.655-3.987-2.756-2.82 3.79-.584L18.006 0l1.723 3.644 3.79.584-2.757 2.819.655 3.953-3.411-1.89zM27.09 11l.654-3.987-2.756-2.82 3.79-.584L30.5 0l1.723 3.644 3.789.584-2.756 2.819.655 3.953L30.5 9.11zM39.583 11l.655-3.987-2.756-2.82 3.79-.584L42.993 0l1.722 3.644 3.79.584-2.756 2.819.655 3.953-3.411-1.89zM52.077 11l.655-3.987-2.756-2.82 3.79-.584L55.487 0l1.722 3.644 3.79.584-2.756 2.819.655 3.953-3.411-1.89z"></path></g></svg></span><span class="acc__text">Average rating: 4.85 out of 5</span></p></div></a>'
    #     '<a href="/percale-cotton-300-thread-count-duvet-cover/p/hbp60460724?color=WHITE" class="product " title="Product name is Percale 300 Thread Count Duvet Cover, 40% off, Previous price is , Sale price is £30.00 - £48.00, Available in 2 colours, Promotion description is Special offer" aria-label="Product name is Percale 300 Thread Count Duvet Cover, 40% off, Previous price is , Sale price is £30.00 - £48.00, Available in 2 colours, Promotion description is Special offer"><div class="product__image product__listing__image" aria-hidden="true"><div class="product__image--display"><img src="https://asset1.marksandspencer.com/is/image/mands/CL_05_T35_5152D_Z0_X_EC_0?wid=250&amp;qlt=80" alt="Percale 300 Thread Count Duvet Cover" class=" product__image--view portrait"><img src="https://asset1.marksandspencer.com/is/image/mands/CL_05_T35_5152D_Z0_X_EC_90?wid=250&amp;qlt=80" alt="Percale 300 Thread Count Duvet Cover" class=" product__image--hover portrait"></div><div class="product__badge"><span class="badge badge--sale">40% off</span></div></div><div class="product__details-link" aria-hidden="true"><div class="product__details"><h3 class="product__title">Percale 300 Thread Count Duvet Cover</h3><div class="sale-price"><p class="price price--reduced"><span class="acc__text">Sale price</span>£30.00 - £48.00</p><p class="price price--previous"><span class="acc__text">Previous price</span></p></div></div></div><div class="product__swatch"><a class="product__swatch__link" href="/percale-cotton-300-thread-count-duvet-cover/p/hbp60460724?color=WHITE#intid=plpnav_swatch"><img src="https://asset1.marksandspencer.com/is/image/mands/CL_05_T35_5152D_Z0_X_EC_88" alt="Percale 300 Thread Count Duvet Cover - white" class=" product__swatch__link-image portrait"></a><a class="product__swatch__link" href="/percale-cotton-300-thread-count-duvet-cover/p/hbp60460724?color=LIGHTGREY#intid=plpnav_swatch"><img src="https://asset1.marksandspencer.com/is/image/mands/CL_05_T35_5152D_T1_X_EC_88" alt="Percale 300 Thread Count Duvet Cover - lightgrey" class=" product__swatch__link-image portrait"></a><div class="product__swatch-label">2 colours available</div></div><div class="product__details" aria-hidden="true"><p class="star-rating"><span class="star-rating__base"><svg aria-hidden="true" width="89" height="12" viewBox="0 0 61 11" xmlns="http://www.w3.org/2000/svg" title="Star Rating"><g><path d="M2.101 11l.655-3.987L0 4.193l3.79-.584L5.512 0l1.723 3.644 3.79.584-2.757 2.819L8.923 11 5.512 9.11zM14.595 11l.655-3.987-2.756-2.82 3.79-.584L18.006 0l1.723 3.644 3.79.584-2.757 2.819.655 3.953-3.411-1.89zM27.09 11l.654-3.987-2.756-2.82 3.79-.584L30.5 0l1.723 3.644 3.789.584-2.756 2.819.655 3.953L30.5 9.11zM39.583 11l.655-3.987-2.756-2.82 3.79-.584L42.993 0l1.722 3.644 3.79.584-2.756 2.819.655 3.953-3.411-1.89zM52.077 11l.655-3.987-2.756-2.82 3.79-.584L55.487 0l1.722 3.644 3.79.584-2.756 2.819.655 3.953-3.411-1.89z"></path></g></svg></span><span class="star-rating__filled" style="width: calc(101.25%);"><svg aria-hidden="true" width="89" height="12" viewBox="0 0 61 11" xmlns="http://www.w3.org/2000/svg" title="Star Rating"><g><path d="M2.101 11l.655-3.987L0 4.193l3.79-.584L5.512 0l1.723 3.644 3.79.584-2.757 2.819L8.923 11 5.512 9.11zM14.595 11l.655-3.987-2.756-2.82 3.79-.584L18.006 0l1.723 3.644 3.79.584-2.757 2.819.655 3.953-3.411-1.89zM27.09 11l.654-3.987-2.756-2.82 3.79-.584L30.5 0l1.723 3.644 3.789.584-2.756 2.819.655 3.953L30.5 9.11zM39.583 11l.655-3.987-2.756-2.82 3.79-.584L42.993 0l1.722 3.644 3.79.584-2.756 2.819.655 3.953-3.411-1.89zM52.077 11l.655-3.987-2.756-2.82 3.79-.584L55.487 0l1.722 3.644 3.79.584-2.756 2.819.655 3.953-3.411-1.89z"></path></g></svg></span><span class="acc__text">Average rating: 5.0 out of 5</span></p><p class="product__offer">Special offer</p></div></a>',
    #     '<a href="/cabin-4-wheel-hard-suitcase-with-security-zip/p/hbp60444797?color=BLACK" class="product " title="Product name is Porto 4 Wheel Hard Shell Cabin Suitcase, Previous price is £39.00, Sale price is £23.70, Available in 2 colours, Promotion description is Special offer" aria-label="Product name is Porto 4 Wheel Hard Shell Cabin Suitcase, Previous price is £39.00, Sale price is £23.70, Available in 2 colours, Promotion description is Special offer"><div class="product__image product__listing__image" aria-hidden="true"><div class="product__image--display"><img src="https://asset1.marksandspencer.com/is/image/mands/PL_05_T40_8902L_Y0_X_EC_0?wid=285&amp;qlt=80" alt="Porto 4 Wheel Hard Shell Cabin Suitcase" class=" product__image--view portrait"><img src="https://asset1.marksandspencer.com/is/image/mands/PL_05_T40_8902L_Y0_X_EC_90?wid=285&amp;qlt=80" alt="Porto 4 Wheel Hard Shell Cabin Suitcase" class=" product__image--hover portrait"></div></div><div class="product__details-link" aria-hidden="true"><div class="product__details"><h3 class="product__title">Porto 4 Wheel Hard Shell Cabin Suitcase</h3><div class="sale-price"><p class="price price--reduced"><span class="acc__text">Sale price</span>£23.70</p><p class="price price--previous"><span class="acc__text">Previous price</span>£39.00</p></div></div></div><div class="product__swatch"><a class="product__swatch__link" href="/cabin-4-wheel-hard-suitcase-with-security-zip/p/hbp60444797?color=BLACK#intid=plpnav_swatch"><img src="https://asset1.marksandspencer.com/is/image/mands/PL_05_T40_8902L_Y0_X_EC_88" alt="Porto 4 Wheel Hard Shell Cabin Suitcase - black" class=" product__swatch__link-image portrait"></a><a class="product__swatch__link" href="/cabin-4-wheel-hard-suitcase-with-security-zip/p/hbp60444797?color=NAVY#intid=plpnav_swatch"><img src="https://asset1.marksandspencer.com/is/image/mands/PL_05_T40_8902L_F0_X_EC_88" alt="Porto 4 Wheel Hard Shell Cabin Suitcase - navy" class=" product__swatch__link-image portrait"></a><div class="product__swatch-label">2 colours available</div></div><div class="product__details" aria-hidden="true"><p class="star-rating"><span class="star-rating__base"><svg aria-hidden="true" width="89" height="12" viewBox="0 0 61 11" xmlns="http://www.w3.org/2000/svg" title="Star Rating"><g><path d="M2.101 11l.655-3.987L0 4.193l3.79-.584L5.512 0l1.723 3.644 3.79.584-2.757 2.819L8.923 11 5.512 9.11zM14.595 11l.655-3.987-2.756-2.82 3.79-.584L18.006 0l1.723 3.644 3.79.584-2.757 2.819.655 3.953-3.411-1.89zM27.09 11l.654-3.987-2.756-2.82 3.79-.584L30.5 0l1.723 3.644 3.789.584-2.756 2.819.655 3.953L30.5 9.11zM39.583 11l.655-3.987-2.756-2.82 3.79-.584L42.993 0l1.722 3.644 3.79.584-2.756 2.819.655 3.953-3.411-1.89zM52.077 11l.655-3.987-2.756-2.82 3.79-.584L55.487 0l1.722 3.644 3.79.584-2.756 2.819.655 3.953-3.411-1.89z"></path></g></svg></span><span class="star-rating__filled" style="width: calc(101.25%);"><svg aria-hidden="true" width="89" height="12" viewBox="0 0 61 11" xmlns="http://www.w3.org/2000/svg" title="Star Rating"><g><path d="M2.101 11l.655-3.987L0 4.193l3.79-.584L5.512 0l1.723 3.644 3.79.584-2.757 2.819L8.923 11 5.512 9.11zM14.595 11l.655-3.987-2.756-2.82 3.79-.584L18.006 0l1.723 3.644 3.79.584-2.757 2.819.655 3.953-3.411-1.89zM27.09 11l.654-3.987-2.756-2.82 3.79-.584L30.5 0l1.723 3.644 3.789.584-2.756 2.819.655 3.953L30.5 9.11zM39.583 11l.655-3.987-2.756-2.82 3.79-.584L42.993 0l1.722 3.644 3.79.584-2.756 2.819.655 3.953-3.411-1.89zM52.077 11l.655-3.987-2.756-2.82 3.79-.584L55.487 0l1.722 3.644 3.79.584-2.756 2.819.655 3.953-3.411-1.89z"></path></g></svg></span><span class="acc__text">Average rating: 5.0 out of 5</span></p><p class="product__offer">Special offer</p></div></a>'
    # ]
    mapper = MarksAndSpencerMapper(
        scraped_data=products, 
        site=site,
        feedname="marksandspencer-home",
        retailer="marksandspencer",
        category="homeware"
    )


def scrapeJohnLewis():
    site = "https://www.johnlewis.com"
    page = "/browse/clearance/home-garden-offers/tableware-offers/_/N-5nhq"
    scraper = JohnLewisScraper(site, page)
    print('Starting scrape')
    scraper.handle_privacy(banner_selector="button[data-test='allow-all']")
    scraper.scroll_to_bottom()
    # scraper.handle_pagination()
    products = scraper.get_grid() or []
    print('Identified', len(products), 'products')
    print(products[0])
    # scraper.close_browser()
    print('Finished scrape. Closing browser')
    # products = [
    #     '<section data-test="product-card" data-product-id="4153153" class="product-card_c-product-card__1UT9N ProductGrid_product__1OU-N product-card_c-product-card--mobile-add-to-basket__3WUAq" data-tagg-processed="true"><div data-test="product-image-container" class="product-card_c-product-card__container__38Nrq"><div class="product-card_c-product-card__image-container__d5DEN"><a class="image_imageLink__1tBDW product-card_c-product-card__image__3CdTi product__image" href="/dartington-crystal-simplicity-white-wine-glasses-250ml-set-of-6-clear/p4153153" tabindex="-1" aria-hidden="true"><img class="image_image__E2_gC" width="250" height="333" src="//johnlewis.scene7.com/is/image/JohnLewis/238036808?$rsp-plp-port-320$" alt="Dartington Crystal Simplicity White Wine Glasses, 250ml, Set of 6, Clear" srcset="//johnlewis.scene7.com/is/image/JohnLewis/238036808?$rsp-plp-port-160$ 160w, //johnlewis.scene7.com/is/image/JohnLewis/238036808?$rsp-plp-port-320$ 320w, //johnlewis.scene7.com/is/image/JohnLewis/238036808?$rsp-plp-port-540$ 540w" sizes="(max-width: 567px) 50vw, (min-width: 568px) and (max-width:768px) 33vw, 20vw"></a><div data-test="component-hover-drawer" class="product-card_c-product-card__hover-drawer__1yAaH hover-drawer_hover-drawer__1-nW2"><div class="hover-drawer_hover-drawer__inner__3pCbh"><button data-test="component-quick-view-button" type="button" class="button_c-button__221gd button_c-button--secondary__1lc8l button_c-button--small__1QxUG hover-drawer_hover-drawer__button__28mCH hover-drawer_hover-drawer__button--desktop-only__24dcD">Quick view</button><button data-test="add to basket" type="button" class="button_c-button__221gd button_c-button--primary__3jR7U button_c-button--small__1QxUG hover-drawer_hover-drawer__button__28mCH add-to-basket_c-product-card__add-to-basket-btn__PyVEu">Add to your basket</button></div></div></div><a class="product-card_c-product-card__link__3NDUX" href="/dartington-crystal-simplicity-white-wine-glasses-250ml-set-of-6-clear/p4153153"><div class="info-section_c-product-card__section__2D2D-" data-test="product-title"><h2 class="title_title__1MULs title_title--four-lines__VHzXP">Dartington Crystal Simplicity White Wine Glasses, 250ml, Set of 6, Clear</h2></div><div class="info-section_c-product-card__section__2D2D- price_c-product-card__price__3NI9k">£31.50</div><div class="info-section_c-product-card__section__2D2D- product-card-rating_rating__2Cb9y"><div class="rating_starsWrapper__3BjaZ"><span class="rating_stars__34OwL" style="width:66%">This product has received, on average,<!-- --> <!-- -->3.30<!-- --> star reviews</span></div><span class="rating_reviews__tWPMc">(<!-- -->3<!-- -->)</span></div></a><div class="info-section_c-product-card__section__2D2D-"><p class="promo-messages_promo__3CCVH">Save 30% (Price Includes Saving)</p></div></div></section>',
    #     '<section data-test="product-card" data-product-id="4769336" class="product-card_c-product-card__1UT9N ProductGrid_product__1OU-N product-card_c-product-card--mobile-add-to-basket__3WUAq" data-tagg-processed="true"><div data-test="product-image-container" class="product-card_c-product-card__container__38Nrq"><div class="product-card_c-product-card__image-container__d5DEN"><a class="image_imageLink__1tBDW product-card_c-product-card__image__3CdTi product__image" href="/john-lewis-partners-geometric-shot-glasses-set-of-4/p4769336" tabindex="-1" aria-hidden="true"><img class="image_image__E2_gC" width="250" height="333" src="//johnlewis.scene7.com/is/image/JohnLewis/238386216?$rsp-plp-port-320$" alt="John Lewis &amp; Partners Geometric Shot Glasses, Set of 4" srcset="//johnlewis.scene7.com/is/image/JohnLewis/238386216?$rsp-plp-port-160$ 160w, //johnlewis.scene7.com/is/image/JohnLewis/238386216?$rsp-plp-port-320$ 320w, //johnlewis.scene7.com/is/image/JohnLewis/238386216?$rsp-plp-port-540$ 540w" sizes="(max-width: 567px) 50vw, (min-width: 568px) and (max-width:768px) 33vw, 20vw"></a><div data-test="component-hover-drawer" class="product-card_c-product-card__hover-drawer__1yAaH hover-drawer_hover-drawer__1-nW2"><div class="hover-drawer_hover-drawer__inner__3pCbh"><button data-test="component-quick-view-button" type="button" class="button_c-button__221gd button_c-button--secondary__1lc8l button_c-button--small__1QxUG hover-drawer_hover-drawer__button__28mCH hover-drawer_hover-drawer__button--desktop-only__24dcD">Quick view</button><button data-test="add to basket" type="button" class="button_c-button__221gd button_c-button--primary__3jR7U button_c-button--small__1QxUG hover-drawer_hover-drawer__button__28mCH add-to-basket_c-product-card__add-to-basket-btn__PyVEu">Add to your basket</button></div></div></div><a class="product-card_c-product-card__link__3NDUX" href="/john-lewis-partners-geometric-shot-glasses-set-of-4/p4769336"><div class="info-section_c-product-card__section__2D2D-" data-test="product-title"><h2 class="title_title__1MULs title_title--four-lines__VHzXP">John Lewis &amp; Partners Geometric Shot Glasses, Set of 4</h2></div><div class="info-section_c-product-card__section__2D2D- price_c-product-card__price__3NI9k price_c-product-card__price--reduced__1mTZl"><span class="price_u-visually-hidden__18Iaj">Was </span><del>£18.00</del><em><span class="price_u-visually-hidden__18Iaj">, now</span> <!-- -->£12.60</em></div></a><div class="info-section_c-product-card__section__2D2D-"><p class="promo-messages_promo__3CCVH">Reduced To Clear</p></div></div></section>',
    #     '<div data-test="component-grid-column" class="GridColumn_col-sm-6__Ba6rz GridColumn_col-md-4__2vhmE GridColumn_col-lg-3__38Mp8 GridColumn_product-grid-column__C4TI0 GridColumn_shouldAnimate__2Aj_B" data-grid-checked="max" data-grid-device="desktop"><section data-test="product-card" data-product-id="4888160" class="product-card_c-product-card__1UT9N ProductGrid_product__1OU-N product-card_c-product-card--mobile-add-to-basket__3WUAq" data-tagg-processed="true"><div data-test="product-image-container" class="product-card_c-product-card__container__38Nrq"><div class="product-card_c-product-card__image-container__d5DEN"><a class="image_imageLink__1tBDW product-card_c-product-card__image__3CdTi product__image" href="/john-lewis-partners-christmas-sequin-table-runner-200cm/red/p4888160" tabindex="-1" aria-hidden="true"><img class="image_image__E2_gC" width="250" height="333" src="//johnlewis.scene7.com/is/image/JohnLewis/238556684?$rsp-plp-port-320$" alt="John Lewis &amp; Partners Christmas Sequin Table Runner, 200cm" srcset="//johnlewis.scene7.com/is/image/JohnLewis/238556684?$rsp-plp-port-160$ 160w, //johnlewis.scene7.com/is/image/JohnLewis/238556684?$rsp-plp-port-320$ 320w, //johnlewis.scene7.com/is/image/JohnLewis/238556684?$rsp-plp-port-540$ 540w" sizes="(max-width: 567px) 50vw, (min-width: 568px) and (max-width:768px) 33vw, 20vw"></a><div data-test="component-hover-drawer" class="product-card_c-product-card__hover-drawer__1yAaH hover-drawer_hover-drawer__1-nW2"><div class="hover-drawer_hover-drawer__inner__3pCbh"><button data-test="component-quick-view-button" type="button" class="button_c-button__221gd button_c-button--secondary__1lc8l button_c-button--small__1QxUG hover-drawer_hover-drawer__button__28mCH hover-drawer_hover-drawer__button--desktop-only__24dcD">Quick view</button><button data-test="multi sku add to basket" type="button" class="button_c-button__221gd button_c-button--primary__3jR7U button_c-button--small__1QxUG hover-drawer_hover-drawer__button__28mCH add-to-basket_c-product-card__add-to-basket-btn__PyVEu">Add to basket</button></div></div></div><a class="product-card_c-product-card__link__3NDUX" href="/john-lewis-partners-christmas-sequin-table-runner-200cm/red/p4888160"><div class="info-section_c-product-card__section__2D2D-" data-test="product-title"><h2 class="title_title__1MULs title_title--four-lines__VHzXP">John Lewis &amp; Partners Christmas Sequin Table Runner, 200cm</h2></div><div class="info-section_c-product-card__section__2D2D- price_c-product-card__price__3NI9k price_c-product-card__price--reduced__1mTZl"><span class="price_u-visually-hidden__18Iaj">Was </span><del>£25.00</del><span class="price_u-visually-hidden__18Iaj">, then</span> <del>£17.50</del><em><span class="price_u-visually-hidden__18Iaj">, now</span> £10.00</em></div></a><div class="info-section_c-product-card__section__2D2D- swatches_swatches__3FYPc"><span class="swatches_visuallyHidden__NeDea">View this product in other colours by selecting one of the following:</span><ul class="swatches_swatchesList__2nSfk"><li class="swatches_swatchItem__x4_ob"><a href="/john-lewis-partners-christmas-sequin-table-runner-200cm/red/p4888160" title="Red" tabindex="0"><img src="//johnlewis.scene7.com/is/image/JohnLewis/238556684?cropN=0.42105263157894735,0.42105263157894735,0.16842105263157894,0.16842105263157894&amp;/&amp;$rsp-plp-swtch$" alt="Red"><span class="swatches_visuallyHidden__NeDea">This colour is available</span></a></li><li class="swatches_swatchItem__x4_ob"><a href="/john-lewis-partners-christmas-sequin-table-runner-200cm/gold/p4888160" title="Gold" tabindex="0"><img src="//johnlewis.scene7.com/is/image/JohnLewis/238556677?cropN=0.42105263157894735,0.42105263157894735,0.16842105263157894,0.16842105263157894&amp;/&amp;$rsp-plp-swtch$" alt="Gold"><span class="swatches_visuallyHidden__NeDea">This colour is available</span></a></li></ul></div><div class="info-section_c-product-card__section__2D2D-"><p class="promo-messages_promo__3CCVH">Reduced To Clear</p></div></div></section></div>',
    #     '<div data-test="component-grid-column" class="GridColumn_col-12__1hCvH GridColumn_product-grid-column__C4TI0"><aside class="ProductCount_productCountInfo__1feRF"><span data-test="product-count-copy">Youve viewed 72 of 109 < /span > </aside > </div >'
    # ]
    mapper = JohnLewisMapper(
        scraped_data=products,
        site=site, 
        feedname="johnlewis-tableware",
        retailer="johnlewis",
        category="tableware"
    )




if __name__ == '__main__':
    scrapeMarksAndSpencer()
    # scrapeJohnLewis()


