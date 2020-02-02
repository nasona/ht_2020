import requests
import json
import csv
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


SONGCSV = "songs.csv"
TAGCSV = "tags.csv"

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
        searchString = self._artist + " " + self._song
        params = {"q": searchString}
        songIDresponse = requests.get(url = "https://api.genius.com/search", params = params, headers = self._header)
        #song id for the first response
        self._songID = songIDresponse.json()["response"]["hits"][0]["result"]["id"]

    def findSongUrl(self):
        response = requests.get(url = "https://api.genius.com/songs/" + str(self._songID), headers = self._header)
        self._url = response.json()["response"]["song"]["url"]

    def getTags(self):
        driver = webdriver.Chrome(executable_path="/Users/abbynason/Desktop/ht_2020/graph_demo/chromedriver")
        driver.implicitly_wait(30)
        driver.get(self._url)
        #need to scroll down far enough to load the elements
        elements = driver.find_elements(By.XPATH, "//div[@class='metadata_with_icon-tags']/span/a[@class='metadata_with_icon-link']")
        for element in elements:
            self._tags.append(element.get_attribute("href"))

    def returnTags(self):
        return self._tags

    def writeTagsToCSV(self):
        pass

    def tagSongs(self):
        self.searchSong()
        self.findSongUrl()
        self.getTags()
        self.writeTagsToCSV()

def main():
    tagFile = open(TAGCSV, "r")
    tagData = csv.reader(tagFile, delimiter=',')
    #firstRow = next(songData)
    artistWithSong = {}
    for row in tagData:
        artistWithSong[(row[0], row[1], row[2])] = row[3]

    songFile = open(SONGCSV, "r")
    songData = csv.reader(songFile, delimiter=',')
    firstRow = next(songData)
    newCount = 0
    for line in songData:
        if newCount >= 25:
            break
        if not (line[0], line[1], line[2]) in artistWithSong:
            scrape = SongTagScraper(line[1], line[2])
            scrape.tagSongs()
            artistWithSong[(line[0], line[1], line[2])] = scrape.returnTags()
            print(str(newCount), ".", line[2],  "by", line[1], "complete.")
            newCount += 1
        else:
            print(line[2],  "by", line[1], "already exists.")

    tagFile.close()
    songFile.close()

    tagFile = open(TAGCSV, "w")
    tagwriter = csv.writer(tagFile, delimiter=',')
    for item in artistWithSong:
        tagwriter.writerow([item[0], item[1], item[2], artistWithSong[item]])
    tagFile.close()

if __name__ == "__main__":
    main()
