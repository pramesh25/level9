import csv
import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


with open('airport.csv' , 'w') as file1:
    head = ['IATA' , 'ICAO' , 'Airport Name' , 'Location' , 'Gps']
    writer = csv.writer(file1)

my_url = 'https://en.wikipedia.org/wiki/Jacksons_International_Airport'


uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html , "html.parser") #html parsing
containers = page_soup.findAll("table", {"class" : "infobox vcard"})
container = containers[0]
try:
    code = container.findAll("div",{"class" : "hlist hlist-separated"})
    code = code[0]
    code = code.findAll("span", {"class": "nickname"})
    iata = code[0].text
    icao = code[1].text
except:
    print('error')
try :
    airport_name = container.tr.th.div.text
except:
    print('error on airport name')
try :
    tr = container.findAll("tr")
    location = tr[8].td.text.split(",")
except:
    print('error on location')
# find_location = container.findAll("td" , {"class" : "label"})
# location= find_location[0].text
try:
    gps = container.find('span', {"class": "geo-dec"}).text
except:
    print('error on gps')
l = [iata,icao,airport_name,location,gps]
print(l)
with open('airport.csv','w') as file:
    writer = csv.writer(file)
    writer.writerow(l)