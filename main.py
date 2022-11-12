from playwright.sync_api import sync_playwright
from todaysDate import set_dates

import datetime
import time



def run(playwright):

    # Setting booking dates
    booking_ending_month, booking_ending_day = set_dates()

    # Setting up the playWright Library
    chromium = playwright.firefox # or "firefox" or "webkit".
    browser = chromium.launch(headless = False, slow_mo=50)
    page = browser.new_page()
    page.goto("https://econnect.markham.ca/Facilities/FacilitiesSearchWizard.asp#")

    # Locating the Facility Booking Information
    page.locator('//*[@id="search-facbook-radio"]').click()

    # Locating the Library Study Rooms
    page.locator('//*[@id="FacilityFunctions"]').click()
    page.locator('#FacilityFunctions').select_option(value = "129")

    # Setting it into Angus Glen
    page.locator('//*[@id="ComplexPanel"]/ul/li[3]/input').click()

    # #
    # page.locator('//*[@id="FacilityTypes"]').click()
    # page.locator('#FacilityTypes').select_option(value = "116")

    #submit
    page.locator('//*[@id="Form_Criteria_Panel"]/div[3]/span[2]/input').click()

    #next page
    page.locator('//*[@id="fac-search-results_next"]').click()


    """
    Record Count # when Study Room becomes Study Room D or E 
    """

    # other actions...
    time.sleep(1800)
    browser.close()

with sync_playwright() as playwright:
    run(playwright)