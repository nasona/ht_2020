import requests
import json
import csv
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#def getSongID():
#songs = []
#for song in songs:
#artist = song[1]
#title = song[2]

class SongTagScraper(object):
    def __init__(self, artist, song):
        self._artist = artist
        self._song = song
        self._header = {"Authorization": "Bearer JrzrS0fgfIZA2czamVGY2rBDjMM1pVbszoRfHszvPxtIm4xsH83wmTYyDUtX6EC2",
                        "User-Agent": ""}
        self._songID = None
        self._url = None
        self._tags = []

    def searchSong(self):
        params = {"q": "Delicate Taylor Swift"}
        songIDresponse = requests.get(url = "https://api.genius.com/search", params = params, headers = self._header)
        #song id for the first response
        self._songID = songIDresponse.json()["response"]["hits"][0]["result"]["id"]

    def findSongUrl(self, songID):
        response = requests.get(url = "https://api.genius.com/songs/" + str(songID), headers = self._header)
        self._url = response.json()["response"]["song"]["url"]

    def getTags(self, url):
        driver = webdriver.Chrome(executable_path="/Users/abbynason/Desktop/ht_2020/graph_demo/chromedriver")
        driver.implicitly_wait(30)
        driver.get(url)
        #need to scroll down far enough to load the elements
        elements = driver.find_elements(By.XPATH, "//div[@class='metadata_with_icon-tags']/span/a[@class='metadata_with_icon-link']")
        for element in elements:
            self._tags.append(element.get_attribute("href"))

    def writeTagsToCSV(self):
        pass

    def tagSongs(self):
        self.searchSong()
        self.findSongUrl()
        self.getTags()
        self.writeTagsToCSV()

#params = {"q": "Delicate Taylor Swift"}
#header = {"Authorization": "Bearer JrzrS0fgfIZA2czamVGY2rBDjMM1pVbszoRfHszvPxtIm4xsH83wmTYyDUtX6EC2",
#          "User-Agent": ""}
#songIDresponse = requests.get(url = "https://api.genius.com/search", params = params, headers = header)
#song id for the first response
#songID = songIDresponse.json()["response"]["hits"][0]["result"]["id"]
#response = requests.get(url = "https://api.genius.com/songs/" + str(songID), headers = header)
#print(response.json())
#with open('example_meta.json', 'w') as outfile:
#    json.dump(response.json(), outfile, indent=2)

#url = response.json()["response"]["song"]["url"]

#driver = webdriver.Chrome(executable_path="/Users/abbynason/Desktop/ht_2020/graph_demo/chromedriver")
#driver.implicitly_wait(30)
#driver.get(url)
#elements = driver.find_elements(By.XPATH, "//div[@class='metadata_with_icon-tags']/span/a[@class='metadata_with_icon-link']")
#tags = []
#for element in elements:
#    tags.append(element.get_attribute('href'))
#print(tags)
