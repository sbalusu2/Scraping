import urllib2
from bs4 import BeautifulSoup as soup
import os.path
import csv

data = []
#headers = "Season, Team, Games Played, Games Started, Minutes Played, FGM-A, FG%, 3PM-A, 3P%, FTM-A, FT%, OR, DR, REB, AST, BLK, STL, PF, TO, PTS\n"
# headers = "Season", "Team","Games Played", "Games Started","Minutes Played", "FGM-A","FG%", "3PM-A","3P%", "FTM-A",
# "FT%", "OR","DR", "REB","AST", "BLK","STL", "PF","TO", "PTS"

#creating a players file if not made
filename = "players.csv"
if not os.path.exists(filename):
	with open('players.csv', 'wb') as f:
		writer = csv.writer(f)
		writer.writerow(["Player Name", "Season", "Team","Games Played", "Games Started","Minutes Played", "FGM-A","FG%", "3PM-A","3P%", "FTM-A","FT%", "OR","DR", "REB","AST", "BLK","STL", "PF","TO", "PTS"])

	# with open('players.csv', 'wb') as csvfile:
	#     writer = csv.writer(csvfile, delimiter=' ',
	#                             quotechar='|', quoting=csv.QUOTE_MINIMAL)
	#     writer.writerow(headers)


# if not os.path.exists(filename):
# 	with open("players.csv", "wb") as csv_file:
# 	# f = file(filename, 'w')
# 		writer.writerow(headers)


# 	writer.writerow(["Season", "Team","Games Played", "Games Started","Minutes Played", "FGM-A","FG%", "3PM-A","3P%", "FTM-A","FT%", "OR","DR", "REB","AST", "BLK","STL", "PF","TO", "PTS"])
# 	f.write(headers)
	#headers = ""
#create a file
# filename = 'lebron.csv'
# f = open(filename, "w")
# headers = "TRB, AST, PTS\n"
# f.write(headers)


#opening up connection - grabbing the page
req = urllib2.Request("http://www.espn.com/nba/player/stats/_/id/3975/stephen-curry")
response = urllib2.urlopen(req)

#read HTML content into a variable
the_page = response.read()
#print the_page

#HTML parsing
page_soup = soup(the_page, "html.parser")
# print page_soup.find_all('li')

print page_soup.title.text # = Karl-Anthony Towns Stats - Minnesota Timberwolves - ESPN
#getting title of html which happens to be output above and manipulating to produce only name and team  
name = page_soup.title.text
name = name[:18] + name[24:49]
print name  # Karl-Anthony Towns - Minnesota Timberwolves

name = page_soup.h1.text
# rows = page_soup.find_all('tr')
# for tr in rows[5:8]:
# 	i=0
# 	for td in tr.find_all('td'):
# 		print td.text
# 		data.append((headers[i], td.text))
# 		list1, list2 = zip(*data)
# 		print list1 
# 		print list2
# 		i=i+1
# 	with open("players.csv", "a") as csv_file:
# 		writer = csv.writer(csv_file)
# 		writer.writerow(list2)
		
body = page_soup.find_all('table')
my_body = body[1]
rows = my_body.findChildren(['tr'])


num_rows = len(rows)
del rows[num_rows - 1]
del rows[1]
del rows[0]

# # with list instead of tuple		
# rows = page_soup.find_all('tr')
for tr in rows:
	i=0
	data.append(name)
	print  data
	for td in tr.find_all('td'):
		print td.text
		data.append(td.text)
		print data
		# list1, list2 = zip(*data)
		# print list1 
		# print list2
		i=i+1
	with open("players.csv", "a") as csv_file:
		writer = csv.writer(csv_file)
		writer.writerow(data)
		data = []



# print data
# print data[2]
# list1, list2 = zip(*data)
# print list1 
# print list2

# with open("players.csv", "a") as csv_file:
#  	writer = csv.writer(csv_file)
#  	writer.writerow(list2)

# with open(filename, "a") as csv_file:
# writer = csv.writer(csv_file) 
# for name, price in data:
# writer.writerow([name, price, today.strftime('%I:%M:%S %p --- %b/%d/%Y')])
# for tr in page_soup.find_all('tr'):
# 	print tr[]


# for tr in page_soup.find_all('tr')[2:]:
#   tds = tr.find_all('td')
#   if len(tds) >= 2:
#     print tds[0].text, tds[1].text


# for tbody in page_soup.find_all('tbody'):
#     trs = tbody.find_all('tr')
#     print trs
#    # for tr in trs:
#     #    tds = tr.find_all('td')
#      #   print(tds[0].text, tds[1].text, tds[2].text)


#working one
# for tr in page_soup.find_all('tr')[2:]:
#   for td in tr.find_all('td'):
#     print td.text
# for tr in page_soup.find_all('tr')[3:]:
# 	print tr
#      for td in tr.find_all('td'):
#     	print td.text



#<tr id="per_game.2004" class="full_table" data-row="0"><th scope="row" class="left " data-stat="season"><a href="/players/j/jamesle01/gamelog/2004/">2003-04</a></th><td class="center " data-stat="age">19</td><td class="left " data-stat="team_id"><a href="/teams/CLE/2004.html">CLE</a></td><td class="left " data-stat="lg_id"><a href="/leagues/NBA_2004.html">NBA</a></td><td class="center " data-stat="pos">SG</td><td class="right " data-stat="g">79</td><td class="right " data-stat="gs">79</td><td class="right " data-stat="mp_per_g">39.5</td><td class="right " data-stat="fg_per_g">7.9</td><td class="right " data-stat="fga_per_g">18.9</td><td class="right " data-stat="fg_pct">.417</td><td class="right " data-stat="fg3_per_g">0.8</td><td class="right " data-stat="fg3a_per_g">2.7</td><td class="right " data-stat="fg3_pct">.290</td><td class="right " data-stat="fg2_per_g">7.1</td><td class="right " data-stat="fg2a_per_g">16.1</td><td class="right " data-stat="fg2_pct">.438</td><td class="right " data-stat="efg_pct">.438</td><td class="right " data-stat="ft_per_g">4.4</td><td class="right " data-stat="fta_per_g">5.8</td><td class="right " data-stat="ft_pct">.754</td><td class="right " data-stat="orb_per_g">1.3</td><td class="right " data-stat="drb_per_g">4.2</td><td class="right " data-stat="trb_per_g">5.5</td><td class="right " data-stat="ast_per_g">5.9</td><td class="right " data-stat="stl_per_g">1.6</td><td class="right " data-stat="blk_per_g">0.7</td><td class="right " data-stat="tov_per_g">3.5</td><td class="right " data-stat="pf_per_g">1.9</td><td class="right " data-stat="pts_per_g">20.9</td></tr>

'''
#find all divs that has the class (could also be id) "item-container"
containers = page_soup.findAll("div",{"class" : "item-container"})
#returns the number of containers - the number of divs with class "item-container" that we extracted
print len(containers)

#prints first containers value - so the HTML of that div
containers[0]
#copy the result. put it in JSbeautifier for spacing stuff. copy that into a text file and see what you want to extract from that html data. Ex: brand, price, ratings

container = containers[0]
container.a #brings back a from that div
container.div.div #brings back the second div from that div
#print container.div.div.li #brings back the li tag from the second div from that div
print container.div.div.li.text.strip()#brings back the text from the li tag from the second div from that div
#print container.div.div.img['title'] - brings back the text from the li tag from the second div from that div
'''