import chromedriver_binary
from selenium import webdriver
from time import sleep
# import options
from selenium.webdriver.chrome.options import Options
from data import string_to_search

your_string = "your_string"

searchables_raw = string_to_search.splitlines()
searchables = [f'site:{site_name} "{your_string}"' for site_name in searchables_raw]

options = Options()
# options.add_argument('--headless')

driver = webdriver.Chrome()

for searchable in searchables:
    driver.get(f'https://www.google.com/search?q={searchable}')
    sleep(2)
    driver.save_screenshot(f'media/{searchable}.png')
