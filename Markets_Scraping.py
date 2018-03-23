import urllib2
import csv
from bs4 import BeautifulSoup as soup
from datetime import datetime
import os.path

data = []
today = datetime.today()

filename = "stocks.csv"
if not os.path.exists(filename):
	with open('stocks.csv', 'wb') as f:
		writer = csv.writer(f)
		writer.writerow(["Company", "Price", "Market Cap", "Open", "Close", "Day Range", "Time"])


quote_pages = ["https://www.bloomberg.com/quote/NVDA:US", "https://www.bloomberg.com/quote/INTC:US", "https://www.bloomberg.com/quote/SBUX:US", "https://www.bloomberg.com/quote/MSFT:US"]

for pg in quote_pages:
	response = urllib2.urlopen(pg)
	the_page = response.read()
	page_soup = soup(the_page, "html.parser")

	name = page_soup.find('h1', {'class': 'companyName__99a4824b'}).text
	print name
	
	price = page_soup.find("span", {"class": "priceText__1853e8a5"}).text
	print price

	values = page_soup.find_all("div", {"class" : "value__b93f12ea"})

	#open_value = values[0].text
	open_value = page_soup.find("div", {"class" : "value__b93f12ea"}).text
	print open_value

	closing_value = values[1].text
	print closing_value

	market_cap = values[3].text
	print market_cap

	low_range_value = page_soup.find("span", {"class" : "textLeft"}).text
	print low_range_value

	high_range_value = page_soup.find("span", {"class" : "textRight"}).text
	print high_range_value

	range_value = low_range_value + " - " + high_range_value
	print range_value

	data.append((name, price, market_cap, open_value, closing_value, range_value))

with open(filename, "a") as csv_file:
  writer = csv.writer(csv_file) 
  for name, price, market_cap, open_value, closing_value, range_value in data:
 	writer.writerow([name, price, market_cap, open_value, closing_value, range_value, today.strftime('%I:%M:%S %p --- %b/%d/%Y')])