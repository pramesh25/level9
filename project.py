import csv
import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


my_url = input('enter url :')
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html , "html.parser") #html parsing
containers = page_soup.findAll("table", {"class" : "infobox vcard"})
container = containers[0]
code = container.findAll("div",{"class" : "hlist hlist-separated"})
code = code[0]
code = code.findAll("span", {"class": "nickname"})
iata = code[0].text
icao = code[1].text
airport_name = container.tr.th.div.text
tr = container.findAll("tr")
location = tr[8].td.text.split(",")
# find_location = container.findAll("td" , {"class" : "label"})
# location= find_location[0].text
gps = container.find('span', {"class": "geo-dec"}).text
l = [iata,icao,airport_name,location,gps]
print(l)
with open('airport.csv','a') as file:
    writer = csv.writer(file)
    writer.writerow(l)