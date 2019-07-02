# lets import the necessary library
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

my_url = 'https://www.amazon.com/s?k=msi+laptops+new&crid=1K8AZGU02RFZB&sprefix=msi+laptops%2Caps%2C798&ref=nb_sb_ss_i_4_11'


uClient = uReq(my_url)
page_html= uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")

# print(page_soup)

containers = page_soup.findAll("span", {"class": "a-size-medium a-color-base a-text-normal"})

container = containers[0]
print(container)

