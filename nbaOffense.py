import urllib2 
import os.path
import csv
from bs4 import BeautifulSoup as soup 
import pandas as pd

data = []
url = ["https://www.foxsports.com/nba/team-stats?season=2016&category=SCORING&group=1&sort=1&time=0&pos=0&team=1&qual=1&sortOrder=0&opp=0",
"https://www.foxsports.com/nba/team-stats?season=2015&category=SCORING&group=1&sort=1&time=0&pos=0&team=1&qual=1&sortOrder=0&opp=0",
"https://www.foxsports.com/nba/team-stats?season=2014&category=SCORING&group=1&sort=1&time=0&pos=0&team=1&qual=1&sortOrder=0&opp=0",
"https://www.foxsports.com/nba/team-stats?season=2013&category=SCORING&group=1&sort=1&time=0&pos=0&team=1&qual=1&sortOrder=0&opp=0",
"https://www.foxsports.com/nba/team-stats?season=2012&category=SCORING&group=1&sort=1&time=0&pos=0&team=1&qual=1&sortOrder=0&opp=0",
"https://www.foxsports.com/nba/team-stats?season=2011&category=SCORING&group=1&sort=1&time=0&pos=0&team=1&qual=1&sortOrder=0&opp=0",
"https://www.foxsports.com/nba/team-stats?season=2010&category=SCORING&group=1&sort=1&time=0&pos=0&team=1&qual=1&sortOrder=0&opp=0",
"https://www.foxsports.com/nba/team-stats?season=2009&category=SCORING&group=1&sort=1&time=0&pos=0&team=1&qual=1&sortOrder=0&opp=0",
"https://www.foxsports.com/nba/team-stats?season=2008&category=SCORING&group=1&sort=1&time=0&pos=0&team=1&qual=1&sortOrder=0&opp=0",
"https://www.foxsports.com/nba/team-stats?season=2007&category=SCORING&group=1&sort=1&time=0&pos=0&team=1&qual=1&sortOrder=0&opp=0",
"https://www.foxsports.com/nba/team-stats?season=2006&category=SCORING&group=1&sort=1&time=0&pos=0&team=1&qual=1&sortOrder=0&opp=0",
"https://www.foxsports.com/nba/team-stats?season=2005&category=SCORING&group=1&sort=1&time=0&pos=0&team=1&qual=1&sortOrder=0&opp=0",
"https://www.foxsports.com/nba/team-stats?season=2004&category=SCORING&group=1&sort=1&time=0&pos=0&team=1&qual=1&sortOrder=0&opp=0",
"https://www.foxsports.com/nba/team-stats?season=2003&category=SCORING&group=1&sort=1&time=0&pos=0&team=1&qual=1&sortOrder=0&opp=0",
"https://www.foxsports.com/nba/team-stats?season=2002&category=SCORING&group=1&sort=1&time=0&pos=0&team=1&qual=1&sortOrder=0&opp=0",
"https://www.foxsports.com/nba/team-stats?season=2001&category=SCORING&group=1&sort=1&time=0&pos=0&team=1&qual=1&sortOrder=0&opp=0",
"https://www.foxsports.com/nba/team-stats?season=2000&category=SCORING&group=1&sort=1&time=0&pos=0&team=1&qual=1&sortOrder=0&opp=0",
"https://www.foxsports.com/nba/team-stats?season=1999&category=SCORING&group=1&sort=1&time=0&pos=0&team=1&qual=1&sortOrder=0&opp=0",
"https://www.foxsports.com/nba/team-stats?season=1998&category=SCORING&group=1&sort=1&time=0&pos=0&team=1&qual=1&sortOrder=0&opp=0",
"https://www.foxsports.com/nba/team-stats?season=1997&category=SCORING&group=1&sort=1&time=0&pos=0&team=1&qual=1&sortOrder=0&opp=0",
"https://www.foxsports.com/nba/team-stats?season=1996&category=SCORING&group=1&sort=1&time=0&pos=0&team=1&qual=1&sortOrder=0&opp=0"]

filename = "offenses.csv"
if not os.path.exists(filename):
	with open("offenses.csv", 'wb') as f:
		writer = csv.writer(f)
		writer.writerow(["Season", "Team", "Ranking", "Other", "GP", "PPG", "PPG Allow", "PPG Diff", "PTS OFF TO", "PTS in Paint", "SEC Chance PTS", "FG%", "FG% Allow",  "3FG%", "3FG% Allow", "FT%", "FT% Allow", "PPS", "PTS/POSS"])

for pg in url:
	response = urllib2.urlopen(pg)
	the_page = response.read()
	page_soup = soup(the_page, "html.parser")

	season = page_soup.find("span", {"class" : "wisbb_pageInfoPrimaryText"}).text.strip()
	season = season[0:7]

	table = page_soup.find_all("table")
	rows = table[0].findChildren("tr")

	for tr in rows[1:]:
		td = tr.findChildren("td")
		ranking =  td[0].findChildren("span", {"class" : "wisbb_rank"})[0].text
		teamName = td[0].findChildren("span")[1].text
		data.append(season)
		data.append(teamName)
		data.append(ranking)
		for td in tr.find_all("td"):
			#print td.text.strip()
			data.append(td.text.strip())
		with open("offenses.csv", "a") as csv_file:
			writer = csv.writer(csv_file)
			writer.writerow(data)
			data = []

# for tr in rows:
# 	for td in tr.find_all("td")[2]:
# 		print td.text
