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

#update to github
'''
from git import Repo
PATH = 'https://github.com/justinbabe019/SolarCarLiveTracker.git'
COMMITMSG = 'location update'

def git_push():
    try: 
        repo = Repo(PATH)
        repo.git.add(update=True)
        repo.index.commit(COMMITMSG)
        origin = repo.remote(name='origin')
        origin.push()
    except:
        print('Some error occured while pushing the code')    
'''

#try to use google maps location sharing instead
#open google maps
import webbrowser
import pyautogui 
import pyperclip
import time
import json
webbrowser.open('http://google.com/maps')
while True:
    time.sleep(5)
    pyautogui.hotkey('command','l')
    time.sleep(2)
    pyautogui.hotkey('command','l')
    pyautogui.hotkey('command','c')
    webAddr = pyperclip.paste()
    webAddrAt = webAddr.split("@",1)
    print(webAddr)
    myLoc = webAddrAt[1].split(",",2)
    myLoc = [myLoc[0], myLoc[1]]
    print(myLoc)
    with open("location.json", "w") as outfile:
        json.dump(myLoc, outfile)
    time.sleep(5)
    pyautogui.hotkey('command','r')
    #git_push()
    time.sleep(5)
    '''
    from pythonmonkey import require as js_require
    js_lib = js_require('./LiveTrackerScript.js')
    js_lib.getAstrumPos()
    '''



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
