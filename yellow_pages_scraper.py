import time
from selenium import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common import keys
import pandas as pd

all_data = []

driver = webdriver.Chrome()
driver.maximize_window()
for x in range(1, 3):
    print(f'Getting page {x}')
    driver.get(
        f"https://www.yellowpages.com/search?search_terms=24%20hour%20fitness&geo_location_terms=Los%20Angeles%2C%20CA&page={x}")
    products = driver.find_elements(By.CLASS_NAME, 'info')

    for product in products:
        busness_name = driver.find_element(
            By.XPATH, '/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/div[1]/div/div/div[2]/div[1]/h2/a/span').text
        busness_categories = driver.find_element(
            By.XPATH, '/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/div[1]/div/div/div[2]/div[1]/div[1]').text
        busness_phone = driver.find_element(
            By.XPATH, '/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/div[1]/div/div/div[2]/div[2]/div[1]').text
        busness_website = driver.find_element(
            By.XPATH, '/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/div[1]/div/div/div[2]/div[1]/div[3]/a')
        busness_location1 = driver.find_element(
            By.XPATH, '/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/div[1]/div/div/div[2]/div[2]/div[2]/div[1]').text
        busness_location2 = driver.find_element(
            By.XPATH, '/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/div[1]/div/div/div[2]/div[2]/div[2]/div[2]').text
        # print(f"Business name:- {busness_name}")
        # print(f"Business categories:- {busness_categories}")
        # print(f"Phone Number:- {busness_phone}")
        # print(f"Website:- {busness_website.get_attribute('href')}")
        # print(f"Address-1:- {busness_location1}")
        # print(f"Address-2:- {busness_location2}")
        all_site_data = {
            'Business-name': busness_name,
            'Business-categories': busness_categories,
            'Phone-Number': busness_phone,
            'Website': busness_website.get_attribute('href'),
            'Address-1': busness_location1,
            'Address-2': busness_location2
        }
        time.sleep(0.5)
        all_data.append(all_site_data)


def load():
    df = pd.DataFrame(all_data)
    df.to_csv('yellopages.csv', index=False)


load()
print('Saved to CSV')
