import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

main_list = []


def extract(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0'}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup.find_all('div', class_='info')


def finder(sub_finder):
    for item in sub_finder:
        busness_name = item.find('a', class_='business-name').text
        busness_categorie = item.find('div', class_='categories').text
        try:
            if item.find('div', class_='phones phone primary').text is not None:
                busness_phone = item.find(
                    'div', class_='phones phone primary').text
        except:
            busness_phone = 'Not Found'
        try:
            busness_website = item.find(
                'a', class_='track-visit-website')['href']
        except:
            busness_website = 'Not Found'
        try:
            busness_location1 = item.find('div', class_='adr').text
        except:
            busness_location1 = 'Not Found'
        # print(busness_name)
        # print(busness_categorie)
        # print(busness_phone)
        # print(busness_website)
        # print(busness_location1)
        all_site_data = {
            'Business-name': busness_name,
            'Business-categories': busness_categorie,
            'Phone-Number': busness_phone,
            'Website': busness_website,
            'Address-1': busness_location1,
        }
        main_list.append(all_site_data)
    # return


def load():
    df = pd.DataFrame(main_list)
    df.to_csv('Yellow_pages_data.csv', index=False)


for x in range(1, 5):
    print(f'Scraping data from page {x}')
    sub_finder = extract(
        f'https://www.yellowpages.com/search?search_terms=24%20hour%20fitness&geo_location_terms=Los%20Angeles%2C%20CA&page={x}')
    finder(sub_finder)
    time.sleep(5)

load()
print('Saved to csv')
