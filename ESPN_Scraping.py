import urllib2
from bs4 import BeautifulSoup as soup
import os.path
import csv

#creating a list to put the data in 
data = []

#creating a players file if not made
filename = "players.csv"
if not os.path.exists(filename):
	with open('players.csv', 'wb') as f:
		writer = csv.writer(f)
		writer.writerow(["Name", "Season", "Team","GP", "GS","MP", "FGM-A","FG%", "3PM-A","3P%", "FTM-A","FT%", "OR","DR", "REB","AST", "BLK","STL", "PF","TO", "PTS"])

#URLs to open
quote_pages = ["http://www.espn.com/nba/player/stats/_/id/1966/lebron-james",
"http://www.espn.com/nba/player/stats/_/id/3202/kevin-durant",
"http://www.espn.com/nba/player/stats/_/id/3992/james-harden",
"http://www.espn.com/nba/player/stats/_/id/3468/russell-westbrook", 
"http://www.espn.com/nba/player/stats/_/id/3975/stephen-curry", 
"http://www.espn.com/nba/player/stats/_/id/6583/anthony-davis"]

for pg in quote_pages: 
	response = urllib2.urlopen(pg)
	the_page = response.read()
	page_soup = soup(the_page, "html.parser")

	# getting the name of the player
	name = page_soup.h1.text

	#extracting the rows via getting the table
	table = page_soup.find_all('table')
	my_table = table[1]
	rows = my_table.findChildren(['tr'])

	#data processing - want to delete the headers and the summary stats rows
	num_rows = len(rows)
	del rows[num_rows - 1]
	del rows[1]
	del rows[0]

	#go through all the rows and extract the tds. add the tds to the list. 
	for tr in rows:
		data.append(name)
		for td in tr.find_all('td'):
			data.append(td.text)
		# open the csv file and add the data to the row and then reset the data list for the next year 	
		with open("players.csv", "a") as csv_file:
			writer = csv.writer(csv_file)
			writer.writerow(data)
			data = []

