import urllib2 
import csv
import os.path
from bs4 import BeautifulSoup as soup 


filename = "tripleDoubles.csv"
if not os.path.exists(filename):
	with open('tripleDoubles.csv', 'wb') as f:
		writer = csv.writer(f)
		writer.writerow(["Name", "Season", "GP", "GS", "DBL", "TBL", "PF", "PFPG", "PF/4.8" "Flag", "Tech", "Eject", "DQ", "+/-"])


data = []
url = "https://www.foxsports.com/nba/russell-westbrook-player-stats",
"https://www.foxsports.com/nba/lebron-james-player-stats",
""
""
""
""

for pg in urls: 
	response = urllib2.urlopen(url)
	the_page = response.read()
	page_soup = soup(the_page, "html.parser")

	fName = page_soup.find("span", {"class": "wisbb_firstName"}).text
	lName = page_soup.find("span", {"class": "wisbb_lastName"}).text
	name = fName + " " + lName

	my_table = page_soup.find_all("table")
	#print my_table[9]
	rows = my_table[9].findChildren(['tr'])
	num = len(rows)
	for row in rows[0:num-2]:
		data.append(name)
		for td in row.find_all('td'):
			data.append(td.text)
		with open("tripleDoubles.csv", "a") as csv_file:
			writer = csv.writer(csv_file)
			writer.writerow(data)
			data = []




