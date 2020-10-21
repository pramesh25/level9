import csv
import bs4
import urllib
from bs4 import BeautifulSoup as soup
import urllib.parse
from urllib.request import urlopen as uReq


url = 'https://en.wikipedia.org/wiki/'
with open('airportcode_1.csv' , 'r') as read_file:
    reader = csv.reader(read_file)
    row = list(reader)
    code = []
    for i in range(1,len(row)-1):
        code.append(row[i][0])
repeat = True
i = 0
data = {}
while repeat == True :
    data['airportcode'] = code[i]
    print(data)
    url_values =  urllib.parse.urlencode(data)
    print(url_values)
    full_url = url + '?' + url_values
    try: data = uReq(full_url)
    except urllib.error.URLError as e:
        print(e.reason)
    print(data)
    r = input('Do you want to repeat again')
    r = r.lower()
    if r == 'y' or r == 'Y':
        repeat = True
        i = i +1
    else:
        r = False

# values
#
my_url = 'https://en.wikipedia.org/wiki/Jacksons_International_Airport'
def scrap():
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
    tr = container.findAll("tr")
    location = tr[8].td.text.split(",")
    airport_name = container.tr.th.div.text
    find_location = container.findAll("td" , {"class" : "label"})
    location= find_location[0].text
    gps = container.find('span', {"class": "geo-dec"}).text
    l = [iata,icao,airport_name,location,gps]
    return l

def add_text():
    with open('airport.csv','a') as file:
        writer = csv.writer(file)
        writer.writerow(scrap())









