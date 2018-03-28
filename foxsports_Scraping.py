import csv
import os.path
import urllib2
from bs4 import BeautifulSoup as soup
from tabulate import tabulate

filename = "playerForm.csv"
if not os.path.exists(filename):
	with open("playerForm.csv", 'wb') as f:
		writer = csv.writer(f)
		writer.writerow(["Name", "Season", "GP", "GS", "DBL", "TBL", "PF", "PFPG", "PF/4.8" "Flag", "Tech", "Eject", "DQ", "+/-"])

data = []
name = raw_input("Whose stats would you like to see (firstname-lastname)? ")

page_url = "https://www.foxsports.com/nba/" + name+"-player-game-log"

response = urllib2.urlopen(page_url)
the_page = response.read()
page_soup = soup(the_page, "html.parser")

season_stats = page_soup.find_all("div", {"class" : "wisbb_bioStatVal"})
pts = season_stats[0].text
rbds = season_stats[1].text
asts = season_stats[2].text
print pts, rbds, asts

table = page_soup.find('table', {"class" : "wisbb_standardTable"})
rows = table.findChildren('tr', {"class" : "wisbb_fvStand "})
print len(rows)
num_rows = len(rows)

del rows[0:num_rows-5]
print len(rows)

for tr in rows: 
	for td in tr.find_all('td'):
		data.append(td.text)
	with open("playerForm.csv", "a") as csv_file:
		writer = csv.writer(csv_file)
		writer.writerow(data)
		data = []
			

#print data
with open("playerForm.csv") as f:
    reader = csv.reader(f)
    formGames = list(reader)
    print formGames[0]
    num = len(formGames)
    print formGames[num-5:num]