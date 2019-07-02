# install anaconda
#pip install beautiful soup

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = "https://en.wikipedia.org/wiki/Lists_of_singers"

uClient = uReq(my_url) # its gonna download whole page

# Now storing it into a variable and closing the page

mypage_html = uClient.read()
uClient.close()

#This parse the page as html and store into mypage_soup
mypage_soup = soup(mypage_html, "html.parser")

#This code brings the header 1 tag data from the page
print(mypage_soup.h1)

#Now lets see whats in P tag

print(mypage_soup.p)

# lets see the body tag

print(mypage_soup.body.span)
