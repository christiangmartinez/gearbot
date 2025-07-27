"""
Scraper for Hank's Music Exchange.
"""
import re

from playwright.sync_api import Playwright, expect, sync_playwright

from constants.locators import (PRODUCT_CELL, PRODUCT_GRID, PRODUCT_PRICE,
                                PRODUCT_TITLE)
from constants.pages import GEAR_URL, PAGE_TITLE, SHOP_URL


def scrape_latest_gear(playwright: Playwright):
    """Get posts on lates gear page"""
    chromium = playwright.chromium
    browser = chromium.launch()
    page = browser.new_page()
    page.goto(GEAR_URL)
    expect(page).to_have_title(re.compile(PAGE_TITLE))

    gear_list = []
    page.locator(PRODUCT_GRID).wait_for()
    products = page.locator(PRODUCT_CELL).all()
    for product in products:
        gear_name = product.locator(PRODUCT_TITLE).inner_text()
        gear_price = product.locator(PRODUCT_PRICE).inner_text()
        gear_link = f'{SHOP_URL}{product.get_by_role("link").first.get_attribute("href")}'
        item = {"name": gear_name, "price": gear_price, "link": gear_link}
        gear_list.append(item)
    browser.close()
    return gear_list

def get_latest_gear():
    """Get gear without importing playwright into other modules"""
    with sync_playwright() as playwright:
        return scrape_latest_gear(playwright)
