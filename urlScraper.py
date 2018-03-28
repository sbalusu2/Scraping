import urllib2
from bs4 import BeautifulSoup as soup

#creating a file
filename = 'products.csv'
f = open(filename, "w")
headers = "brand, product_name, shipping\n"
f.write(headers)

#opening up connection, grabbing the page
req = urllib2.Request('https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card')
response = urllib2.urlopen(req)

#reads html content into a variable
the_page = response.read()
#print the_page

#html parsing
page_soup = soup(the_page, "html.parser")
# print page_soup.p - prints the paragraphs in that url

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

