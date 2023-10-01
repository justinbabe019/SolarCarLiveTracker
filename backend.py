#----GET LOC W STARLINK ADDRESS


import socket
import requests
from ip2geotools.databases.noncommercial import DbIpCity
from geopy.distance import distance

comp = socket.gethostname()
IPAddr = socket.gethostbyname(comp)

import geocoder
g = geocoder.ipinfo('me')
print(f"my current location: {g.latlng}")

def printDetails(ip):
    res = DbIpCity.get(ip, api_key="free")
    print(f"IP Address: {res.ip_address}")
    print(f"IP Address of router: {res.ip_address}")
    print(f"Location: {res.city}, {res.region}, {res.country}")
    print(f"Coordinates: (Lat: {res.latitude}, Lng: {res.longitude})")

printDetails(IPAddr)

import webbrowser
webbrowser.open('http://google.com/maps')

#Accessing google share location and get latlng?
#log into google
'''
from bs4 import BeautifulSoup
import requests
form_data={'Email': 'justinbabe019@gmail.com', 'Passwd': 'ilovekabcliforever'}
post = "https://accounts.google.com/signin/challenge/sl/password"

with requests.Session() as s:
    soup = BeautifulSoup(s.get("https://mail.google.com").text)
    for inp in soup.select("#gaia_loginform input[name]"):
        if inp["name"] not in form_data:
            form_data[inp["name"]] = inp["value"]
    s.post(post, form_data)
    html = s.get("https://mail.google.com/mail/u/0/#inbox").content
'''

#Device location
'''
import urllib.request as urllib2
import json
'''

# Automatically geolocate the connecting IP
'''
f = urllib2.urlopen('http://freegeoip.net/json/')
json_string = f.read()
f.close()
location = json.loads(json_string)
print(location)
location_city = location['city']
location_state = location['region_name']
location_country = location['country_name']
location_zip = location['zipcode']
'''