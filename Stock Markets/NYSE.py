import urllib2
import os.path
import csv
from bs4 import BeautifulSoup as soup

data = []
url = ["http://www.barrons.com/public/page/majormarket-nysecomposite-A.html",
"http://www.barrons.com/public/page/majormarket-nysecomposite-B.html",
"http://www.barrons.com/public/page/majormarket-nysecomposite-C.html",
"http://www.barrons.com/public/page/majormarket-nysecomposite-D.html",
"http://www.barrons.com/public/page/majormarket-nysecomposite-E.html",
"http://www.barrons.com/public/page/majormarket-nysecomposite-F.html",
"http://www.barrons.com/public/page/majormarket-nysecomposite-G.html",
"http://www.barrons.com/public/page/majormarket-nysecomposite-H.html",
"http://www.barrons.com/public/page/majormarket-nysecomposite-I.html",
"http://www.barrons.com/public/page/majormarket-nysecomposite-J.html",
"http://www.barrons.com/public/page/majormarket-nysecomposite-K.html",
"http://www.barrons.com/public/page/majormarket-nysecomposite-L.html",
"http://www.barrons.com/public/page/majormarket-nysecomposite-M.html",
"http://www.barrons.com/public/page/majormarket-nysecomposite-N.html",
"http://www.barrons.com/public/page/majormarket-nysecomposite-O.html",
"http://www.barrons.com/public/page/majormarket-nysecomposite-P.html",
"http://www.barrons.com/public/page/majormarket-nysecomposite-Q.html",
"http://www.barrons.com/public/page/majormarket-nysecomposite-R.html",
"http://www.barrons.com/public/page/majormarket-nysecomposite-S.html",
"http://www.barrons.com/public/page/majormarket-nysecomposite-T.html",
"http://www.barrons.com/public/page/majormarket-nysecomposite-U.html",
"http://www.barrons.com/public/page/majormarket-nysecomposite-V.html",
"http://www.barrons.com/public/page/majormarket-nysecomposite-W.html",
"http://www.barrons.com/public/page/majormarket-nysecomposite-X.html",
"http://www.barrons.com/public/page/majormarket-nysecomposite-Y.html",
"http://www.barrons.com/public/page/majormarket-nysecomposite-Z.html"]
filename = "NYSE.csv"

if not os.path.exists(filename):
	with open(filename, 'wb') as f:
		writer = csv.writer(f)
		writer.writerow(["Company", "Title", "Price", "Volume", "High", "Low"])

for pg in url: 

	response = urllib2.urlopen(pg)
	the_page = response.read()
	page_soup = soup(the_page, 'html.parser')

	rows = page_soup.find_all('tr',{"align": "right"})
	# print len(rows)

	for row in rows:
		deets = row.find_all('td')
		name = deets[5].text
		sym = deets[6].text
		vol = deets[7].text
		high = deets[10].text
		low = deets[11].text
		price = deets[12].text
		data.append(name)
		data.append(sym)
		data.append(price)
		data.append(vol)
		data.append(high)
		data.append(low)

	# 	tag = deets[0].find('a').text
	# 	data.append(name)
	# 	data.append(tag)
	# 	for td in deets[1:]:
	# 		# print td.text.encode('ascii', 'ignore')
	# 		data.append(td.text.encode('ascii', 'ignore'))

		with open(filename, 'a') as f:
			writer = csv.writer(f)
			writer.writerow(data)
			data = []


	