import csv
import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


def read_file():
    with open('airportcode_1.csv','a') as file:
        reader = csv.reader(file)
        next(file)
        row = list(reader)
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

scrap()









