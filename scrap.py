from bs4 import BeautifulSoup
import requests
from urllib.request import *
import sys

def save_media(url,videos=True):
    soap = BeautifulSoup(requests.get(url).text, "html5lib")
    images = soap.find_all(class_="post__image")
    print("Starting downloading " + str(len(images)) + " items.")
    count = str(len(images))
    for indx,i in enumerate(images):
        image = i.find(class_="desktop")['href']
        imgname = (sys.argv[1] + image[image.rfind('/') + 1:]) if len(sys.argv) == 2 else  image[image.rfind('/') + 1:] 
        urlretrieve("https://2ch.hk" + image, imgname)
        sys.stdout.write(str(indx + 1) + "/" + count + "\r")
    print("Downloading finished.")

while True:
    url = input()
    if url == 'q':
        break
    else:
        save_media(url)
