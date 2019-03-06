#!/usr/bin/env python3

import urllib
from bs4 import BeautifulSoup

def get_soup(url):
    site = urllib.request.urlopen(url)
    return BeautifulSoup(site, 'html.parser')

base_url = 'https://en.wikipedia.org'
url = 'https://en.wikipedia.org/wiki/List_of_UFC_events'
site = urllib.request.urlopen(url)
soup = BeautifulSoup(site, 'html.parser')
tables = soup.find_all('table')

rows = tables[1].find_all('tr')
# ideas from here
# - get the url of the fight
# - get geo location
# - get altitude

links = {}

for row in rows:
    if row.find('td'):
        cells = row.find_all('td')
        # for a in cells[1].find('a', href=True)
        links[cells[0].text.strip()] = base_url + cells[1].find('a', href=True)['href']

soup = get_soup(links['201'])
tables = soup.find_all('table')
results = tables[2]
records = results.find_all('tr')
records = records[2:]
elements = records[1].find_all('td')
row_test = []
for i in range(len(elements)):
    row_test.append(elements[i].text.strip())
    if elements[i].find('a', href=True):
        a = elements[i].find('a', href=True)['href']
        a = base_url + a
        row_test.append(a)
    # elements[i].text.

# for link in links:
#     soup = get_soup(links[link])
#     soup.find_all('table')

