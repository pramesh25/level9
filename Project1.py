import csv
import pandas as pd
import requests
import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import urllib.parse
def site(iata_code):
    my_url = 'https://en.wikipedia.org/wiki/' + iata_code + '_Airport'
    uClient = requests.get(my_url)
    return uClient






def Scrap():
    with open('airportcode_1.csv','r') as read_file:
        reader = csv.reader(read_file)
        next(reader)
        row = list(reader)
        for i in row:
            iata_code = i[0]
            print(iata_code)
            respond = site(iata_code).url
            source = requests.get(respond)
            s = soup(source.text, 'lxml')
            try:
                table = s.findAll("table", {"class": "infobox vcard"})
                table = table[0]
            except:
                print('not found')


            try:
                code = table.findAll("div", {"class": "hlist hlist-separated"})
                code = code[0]
                code = code.findAll("span", {"class": "nickname"})
                iata = code[0].text
                icao = code[1].text
            except:
                print('error in iata or icao')
                iata = 'none'
                icao = 'none'
            try:
                airport_name = table.tr.th.div.text
            except:
                print('error on airport name')
                airport_name = 'none'
            try:
                tr = table.findAll("tr")
                location = tr[8].td.text.split(",")
            except:
                print('error on location')
                location = 'none'
            # find_location = container.findAll("td" , {"class" : "label"})
            # location= find_location[0].text
            try:
                gps = table.find('span', {"class": "geo-dec"}).text
            except:
                print('error on gps')
                gps = 'none'
            l = [iata, icao, airport_name, location, gps]
            print(l)
with open('airport.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(['IATA', 'IACO', 'Airport name', 'Location', 'Gps'])
        writer.writerow(Scrap())



