import urllib2
from bs4 import BeautifulSoup as soup 
import os.path
import csv

url = 'https://www.nytimes.com/'
response = urllib2.urlopen(url)
the_page = response.read()
page_soup = soup(the_page, "html.parser")

headlines = page_soup.find_all("h2", {"class" : "story-heading"})
i = 0;


for hl in headlines[0:10]:
	print headlines[i].text	
	aTags = headlines[i].findChildren('a')
	while aTags: 
		print aTags[0]['href']
		break
	i+=1
	print('\n' * 3)
