# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 16:37:38 2019

@author: Pritam
please share your experience and error with me on github.
github.com/pritam-raj

"""

#important library for scraping
#if library not exists try pip3 install "library name"

from bs4 import BeautifulSoup
import requests
from PIL import Image 
from io import BytesIO

search = input('write image name for scraping:')
params = {"q": search}
"""
i don't use google.com for image scraping bcz its use javascript code and bypass auto search 
and its solution i don't have.but i wish in future i solved this problem
"""
r = requests.get("http://www.bing.com/images/search", params = params)

soup = BeautifulSoup(r.text, "html5lib")
links = soup.find_all("a", {"class": "thumb"})

for item in links:
    image_object = requests.get(item.attrs['href'])
    print("getting links", item.attrs['href'])
    title = item.attrs['href'].split("/")[-1]
    img = Image.open(BytesIO(image_object.content))
    img.save("./scraped_images/" + title, img.format)
    