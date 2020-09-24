from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO
import os
import urllib.request

def startsearch():
    search = input('write image name for scraping:')
    params = {"q": search}
    dir_name = search.replace(" ", "-").lower()

    if not os.path.isdir(dir_name):
        os.makedirs(dir_name)
    """
    i don't use google.com for image scraping bcz its use javascript code and bypass auto search 
    and its solution i don't have.but i wish in future i solved this problem
    """
    r = requests.get("http://www.bing.com/images/search", params=params)

    soup = BeautifulSoup(r.text, "html5lib")
    links = soup.find_all("a", {"class": "thumb"})

    for item in links:
        try:
            image_object = requests.get(item.attrs['href'])
            print("getting links", item.attrs['href'])
            title = item.attrs['href'].split("/")[-1]
            try:
                urllib.request.urlretrieve(item.attrs['href'], dir_name+title)
                print("image saved")
            except:
                print("could not save image.")
        except:
            print("could not request image")
    startsearch()

startsearch()
