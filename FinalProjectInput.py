'''
    a) ManufacturerList.csv -- contains items listed by row. Each row contains item ID, manufacturer name, item type, and optionally a damaged indicator
    b) PriceList.csv -- contains items listed by row. Each row contains item ID and the item price.
    c) ServiceDatesList.csv -- contains items listed by row. Each row contains item ID and service date.

 '''

import csv
from datetime import datetime

with open('/Users/lilytran/Documents/UH Summer 2024/Final project GitHub/ManufacturerList.csv', 'r') as file:
    manufacturer_list = list(csv.reader(file))

with open('/Users/lilytran/Documents/UH Summer 2024/Final project GitHub/PriceList.csv', 'r') as file: 
    price_list = list(csv.reader(file))

with open('/Users/lilytran/Documents/UH Summer 2024/Final project GitHub/ServiceDatesList.csv', 'r') as file:
    service_dates_list = list(csv.reader(file))

inventory = []

for item in manufacturer_list:
    item_id = item[0]
    manufacturer_name = item[1]
    item_type = item[2]
    damaged = item[3] if len(item) > 3 else ''

price = '0'
for price_item in price_list:
    if price_item[0] == item_id:
        price = price_item[1]
        break

service_date = ''
for date_item in service_dates_list:
    if date_item[0] == item_id:
        service_date = date_item[1]
        break
    
inventory.append([item_id, manufacturer_name, item_type, price, service_date, damaged])




