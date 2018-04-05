import urllib2
import os.path
import csv
from bs4 import BeautifulSoup as soup

data = []
url = ["http://eoddata.com/stocklist/NASDAQ/A.htm",
"http://eoddata.com/stocklist/NASDAQ/B.htm",
"http://eoddata.com/stocklist/NASDAQ/C.htm",
"http://eoddata.com/stocklist/NASDAQ/D.htm",
"http://eoddata.com/stocklist/NASDAQ/E.htm",
"http://eoddata.com/stocklist/NASDAQ/F.htm",
"http://eoddata.com/stocklist/NASDAQ/G.htm",
"http://eoddata.com/stocklist/NASDAQ/H.htm",
"http://eoddata.com/stocklist/NASDAQ/I.htm",
"http://eoddata.com/stocklist/NASDAQ/J.htm",
"http://eoddata.com/stocklist/NASDAQ/K.htm",
"http://eoddata.com/stocklist/NASDAQ/L.htm",
"http://eoddata.com/stocklist/NASDAQ/M.htm",
"http://eoddata.com/stocklist/NASDAQ/N.htm",
"http://eoddata.com/stocklist/NASDAQ/O.htm",
"http://eoddata.com/stocklist/NASDAQ/P.htm",
"http://eoddata.com/stocklist/NASDAQ/Q.htm",
"http://eoddata.com/stocklist/NASDAQ/R.htm",
"http://eoddata.com/stocklist/NASDAQ/S.htm",
"http://eoddata.com/stocklist/NASDAQ/T.htm",
"http://eoddata.com/stocklist/NASDAQ/U.htm",
"http://eoddata.com/stocklist/NASDAQ/V.htm",
"http://eoddata.com/stocklist/NASDAQ/W.htm",
"http://eoddata.com/stocklist/NASDAQ/X.htm",
"http://eoddata.com/stocklist/NASDAQ/Y.htm",
"http://eoddata.com/stocklist/NASDAQ/Z.htm"] 
filename = "NASDAQ.csv"

if not os.path.exists(filename):
	with open(filename, 'wb') as f:
		writer = csv.writer(f)
		writer.writerow(["Title", "Company", "High", "Low", "Price", "Volume", "Change", "", "% Change"])

for pg in url: 
	response = urllib2.urlopen(pg)
	the_page = response.read()
	page_soup = soup(the_page, 'html.parser')

	rows = page_soup.find_all('tr')
	numRows = len(rows)

	for row in rows[6:numRows-21]:
		deets = row.find_all('td')
		for td in deets:
			# print td.text.encode('ascii', 'ignore')
			data.append(td.text.encode('ascii', 'ignore'))
		with open(filename, 'a') as f:
			writer = csv.writer(f)
			writer.writerow(data)
			data = []


