#import libraries
import urllib2 
from bs4 import BeautifulSoup as soup 
import csv
from datetime import datetime
import os.path

#creating a stocks file if not made
filename = "stocks.csv"
if not os.path.exists(filename):
    file(filename, 'w').close()

data = []
today = datetime.today()


#open connection to url and extract content
#req = urllib2.Request("https://www.bloomberg.com/quote/SPX:IND")
#response = urllib2.urlopen(req)

#another option to open url without requesting connection to the url
quote_page = ["https://www.bloomberg.com/quote/NVDA:US", 
"https://www.bloomberg.com/quote/INTC:US", "https://www.bloomberg.com/quote/SBUX:US", "https://www.bloomberg.com/quote/MSFT:US"]


for pg in quote_page: 

	response = urllib2.urlopen(pg)
	#read content into a variable  - YOU NEED THIS OR ELSE THERE IS NO HTML CONTENT TO READ IN FOLLOWING STEPS
	the_page = response.read()

	#HTML parsing
	page_soup = soup(the_page, "html.parser")


	name_box = page_soup.find('h1', {'class': 'companyName__99a4824b'})
	print name_box #tag
	print "Name Box Text = " + name_box.text #str
	name = name_box.text.strip()
	print "Name = " + name #minus spaces before and after   

	print "------------------------"
	price_box = page_soup.find("span", {"class": "priceText__1853e8a5"})
	print price_box
	price = price_box.text
	print price

	data.append((name, price))
	print data

with open(filename, "a") as csv_file:
  writer = csv.writer(csv_file) 
  for name, price in data:
 	writer.writerow([name, price, today.strftime('%I:%M:%S %p --- %b/%d/%Y')])

