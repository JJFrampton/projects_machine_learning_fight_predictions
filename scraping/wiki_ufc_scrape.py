#!/usr/bin/env python3

import csv
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

links = []

for row in rows:
    if row.find('td'):
        cells = row.find_all('td')
        # for a in cells[1].find('a', href=True)
        links.append(base_url + cells[1].find('a', href=True)['href'])

fighters = []

# write to csv file
with open('fight_data.csv', 'w') as fight_data:
    writer = csv.writer(fight_data)
    data = []
    # link = links[0]
    # if link:
    for link in links:
        soup = get_soup(link)
        records = soup.find_all('table')[2].find_all('tr')[2:]
        for record in records:
            elements = record.find_all('td')
            row_test = []
            row_test.append(link)
            for i in range(len(elements)):
                row_test.append(elements[i].text.strip())
                if elements[i].find('a', href=True):
                    a = base_url + elements[i].find('a', href=True)['href']
                    row_test.append(a)
                    if i == 3 or i == 6:
                        if a not in fighters:
                            fighters.append(a)
            if len(row_test) > 2 and row_test[0] != 'Weight class':
                data.append(row_test)
                writer.writerow(row_test)

number_of_elements_per_row = []
for i in range(len(data)):
    if len(data[i]) not in number_of_elements_per_row:
        number_of_elements_per_row.append(len(data[i]))
number_of_elements_per_row.sort()
print(number_of_elements_per_row)


# fighters

# need to remove all rows with only the url
# ie: some headings like "weight class", "method" or "prelims", "main card" etc
# all of these rows only have the event url
