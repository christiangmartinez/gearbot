import re

from playwright.sync_api import Playwright, expect, sync_playwright

from ..constants.locators import (PRODUCT_CELL, PRODUCT_GRID, PRODUCT_PRICE,
                                  PRODUCT_TITLE)
from ..constants.pages import GEAR_URL, PAGE_TITLE, SHOP_URL


def scrape_latest_gear(playwright: Playwright):
    """Get latest items and price from shop url"""
    chromium = playwright.chromium
    browser = chromium.launch()
    page = browser.new_page()
    page.goto(GEAR_URL)
    expect(page).to_have_title(re.compile(PAGE_TITLE))

    gear = []
    try:
        page.locator(PRODUCT_GRID).wait_for()
        items = page.locator(PRODUCT_CELL).all()
        for item in items:
            gear_name = item.locator(PRODUCT_TITLE).inner_text()
            gear_price = item.locator(PRODUCT_PRICE).inner_text()
            gear_link = f'{SHOP_URL}{item.get_by_role("link").first.get_attribute("href")}'
            gear.append({"name": gear_name, "price": gear_price, "link": gear_link})
    except TimeoutError as e:
        print(f'TimeoutError occurred: {e}')

    browser.close()
    return gear

def get_latest_gear():
    with sync_playwright() as playwright:
        return scrape_latest_gear(playwright)
