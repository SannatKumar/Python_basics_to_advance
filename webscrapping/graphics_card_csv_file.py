# web scrapping based on tutorial
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

#assign url link to the variable
my_url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card'

# opening up the link, grabbing the page

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

#Now lets call the soup function

mypage_soup = soup(page_html, "html.parser")

print(mypage_soup.h1)

#This grabs each products

containers = mypage_soup.findAll("div",{"class":"item-container"})

#just check what is the length of the data
print(len(containers))

filename = "products.csv"
f = open(filename, "w")

headers = "brand\n"
f.write(headers)


"""container = containers[0]
my_data = container.findAll("a")
my_dat = my_data[0]
"""
for container in containers:
    my_data = container.findAll("a")
    for my_dat in my_data:
        brand = my_dat.img["title"]
        print("brand" + brand)
        f.write(brand  + "\n")
f.close()        




