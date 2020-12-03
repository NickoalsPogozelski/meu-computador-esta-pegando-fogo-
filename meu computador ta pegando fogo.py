import urllib
import requests
from bs4 import BeautifulSoup
import string
import time
import keyboard

url = 'https://www.ismycomputeronfire.com/'


while True:
    #wait a second
    time.sleep(1)
    #request the website url
    request = requests.get(url)
    #parse the url
    soup = BeautifulSoup(request.text, 'html.parser')
    #search for h1 tag
    content = str(soup.findAll("h1"))

    #filter the tag
    filter = content.split('<')
    filter = filter[1].split(">")
    print(filter[1])

    if keyboard.is_pressed('esc'):
        break


