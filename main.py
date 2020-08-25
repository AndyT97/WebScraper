from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    #xpos,ypos,width,height
    win.setGeometry(500,500,300,300)
    win.setWindowTitle("Newegg Scraper")
    win.show()
    sys.exit(app.exec_())

window()


cpu_url = "https://www.newegg.ca/Processors-Desktops/SubCategory/ID-343?Tid=7670"
ssd_url = "https://www.newegg.ca/Internal-SSDs/SubCategory/ID-636?Tid=11700"

uClient = uReq(cpu_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")

#Find all items
containers = page_soup.find_all("div",{"class":"item-container"})
#How many items found
print(len(containers))

# items = page_soup.find_all("a",{"class":"item-title"})
# price = page_soup.find_all("li", {"class":"price-current"})
# print(len(items))
# print(len(price))

filename = "products.csv"
f = open(filename,"w")
headers = "Title and price"

for item in containers:
    #item.find_all returns only one element
    items = item.find_all("a", {"class": "item-title"})
    item_name = items[0].string

    price_list = item.find_all("li", {"class": "price-current"})
    price_dollar = price_list[0].strong.string
    price_cents = price_list[0].sup.string

    print(item_name)
    print("${}{}".format(price_dollar, price_cents))
    f.write(item_name +"\n"+"$"+price_dollar + price_cents)

f.close()
#print(items[0].string)

#Print price of item
#print("${}{}".format(price[0].strong.string,price[0].sup.string))

# item1 = containers[0]
# print(item1.div)