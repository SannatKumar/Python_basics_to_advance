# lets import the necessary library
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

my_url = 'https://scholarshipfellow.com/internship-report-internship-report-sample-format-example/'


uClient = uReq(my_url)
page_html= uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")

# print(page_soup)
page_soup.prettify()

containers = page_soup.find("div", {"class": "entry-content entry clearfix"})
#print(len(containers))
   
container = containers.findAll('p')
# print(len(container))
# print(container)

filename = "internshipreport.txt"
f = open(filename, "w")

for x in container:
    par = x.text
    f.write(par + "\n")

f.close()



