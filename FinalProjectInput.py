''' Instructions for inputs:
    a) ManufacturerList.csv -- contains items listed by row. Each row contains item ID, manufacturer name, item type, and optionally a damaged indicator
    b) PriceList.csv -- contains items listed by row. Each row contains item ID and the item price.
    c) ServiceDatesList.csv -- contains items listed by row. Each row contains item ID and service date.

 '''
#importing csv code will allow python to work with CSV or Comma-Separated Values files to integrate with the code
import csv
#datetime modules allow manipulation of classes that involves date and tim e
from datetime import datetime
#I kept getting error with my pathway and had to ask AI to help clear out my error message in my terminal in order to link the CSV
#code to open all three input files, ManufacturerList, PriceList and ServiceDatesList
with open('/Users/lilytran/Documents/GitHub/CIS2348Finalproject/ManufacturerList.csv', 'r') as file:
    manufacturer_list = list(csv.reader(file))

with open('/Users/lilytran/Documents/GitHub/CIS2348Finalproject/PriceList.csv', 'r') as file: 
    price_list = list(csv.reader(file))

with open('/Users/lilytran/Documents/GitHub/CIS2348Finalproject/ServiceDatesList.csv', 'r') as file:
    service_dates_list = list(csv.reader(file))

#Main inventory list 
inventory = []
#Format of the inventory data by column and row 
for item in manufacturer_list:
    item_id = item[0]
    manufacturer_name = item[1]
    item_type = item[2]
    damaged = item[3] if len(item) > 3 else ''

#Using for and if/else loop to determine the price and date of the data from CSV
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
    
#append, adding on the information by the order format specificed from the inventory format   
inventory.append([item_id, manufacturer_name, item_type, price, service_date, damaged])

#take the information and sort with specifications, lambda x: x[1] which is a defined sorting criterion 
#need to change the file to be able to write, open file with 'w' writing mode 
inventory.sort(key=lambda x: x[1]) 
with open('FullInventory.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(inventory)

#take the information and sort with specifications, lambda x: x[1] which is a defined sorting criterion 
#need to change the file to be able to write, open file with 'w' writing mode 
inventory.sort(key=lambda x: x[1]) 
with open('FullInventory.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(inventory)

#take the information and sort with specifications, lambda x: x[1] which is a defined sorting criterion 
#need to change the file to be able to write, open file with 'w' writing mode 
inventory.sort(key=lambda x: x[1]) 
with open('DamagedInventory.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(inventory)



