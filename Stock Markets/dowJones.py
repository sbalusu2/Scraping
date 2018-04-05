import urllib2
import os.path
import csv
from bs4 import BeautifulSoup as soup

data = []
url = "http://money.cnn.com/data/dow30/"
filename = "Dow Jones.csv"

if not os.path.exists(filename):
	with open(filename, 'wb') as f:
		writer = csv.writer(f)
		writer.writerow(["Company", "Title", "Price", "Change", "% Change", "Volume", "YTD Change"])


response = urllib2.urlopen(url)
the_page = response.read()
page_soup = soup(the_page, 'html.parser')

rows = page_soup.find_all('tr')

for row in rows[2:]:
	deets = row.find_all('td')
	tag = deets[0].find('a').text
	name = deets[0].find('span').text
	data.append(name)
	data.append(tag)
	for td in deets[1:]:
		# print td.text.encode('ascii', 'ignore')
		data.append(td.text.encode('ascii', 'ignore'))

	with open(filename, 'a') as f:
		writer = csv.writer(f)
		writer.writerow(data)
		data = []


	