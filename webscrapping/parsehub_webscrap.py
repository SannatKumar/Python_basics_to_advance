# web scraping

import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
my_url = 'https://www.parsehub.com/'
print(my_url)

#Now actual thing
# openinig up the connection grabbing the webpage
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

##Now calling the soup function
#Html parser
page_soup = soup(page_html, "html.parser")

print(page_soup.h1)
everything = page_soup.find("div",{"class":"col-md-2"})
division = everything.p
print(division)

