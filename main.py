from playwright.sync_api import sync_playwright

import time

def run(playwright):
    chromium = playwright.chromium # or "firefox" or "webkit".
    browser = chromium.launch(headless = False, slow_mo=50)
    page = browser.new_page()
    page.goto("https://econnect.markham.ca/Facilities/FacilitiesSearchWizard.asp#")
    page.locator('//*[@id="search-facavail-radio"]').click()

    page.locator('//*[@id="FacilityTypes"]').click()
    page.locator('#FacilityTypes').select_option(value = "116")

    page.locator('//*[@id="ComplexPanel"]/ul/li[4]/input').click()
    page.locator('//*[@id="Form_Criteria_Panel"]/div[3]/span[2]/span/input').click()

    page.is_visible()

    # other actions...
    time.sleep(3)
    browser.close()

with sync_playwright() as playwright:
    run(playwright)