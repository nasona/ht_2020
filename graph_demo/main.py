from song_graph import Song
from song_graph import Camelot
from song_graph import SongGraph
import csv
import graph_algs
import random

SONGCSV = "songs.csv"
TAGCSV = "tags.csv"

def createSongs():
    songFile = open(SONGCSV)
    songData = csv.reader(songFile, delimiter=',')
    firstRow = next(songData)
    songList = []

    tagFile = open(TAGCSV, "r")
    tagData = csv.reader(tagFile, delimiter=',')
    tagDict = {}
    for row in tagData:
        tagDict[row[0]] = row[3][2:len(row[3])-2].split("', '")
    #print(tagDict)


    for line in songData:
        cleanTags = None
        for thing in tagDict:
            if thing == line[0]:
                cleanTags = tagDict[thing]

        if len(line[10]) == 2:
            camelot = Camelot(int(line[10][0]), line[10][1])
        if len(line[10]) == 3:
            camelot = Camelot(int(line[10][:2]), line[10][2])
        song = Song(line[0], line[1], line[2], line[3], int(line[4]), line[5], line[6], line[7], line[8], int(line[9]), camelot, int(line[11]), cleanTags, line[12])
        songList.append(song)
    return songList

def chooseTheSongs(songList, startSong, endSong, bagSize):
    potentialPlaylist = []
    potentialPlaylist.append(startSong)
    songList.remove(startSong)
    potentialPlaylist.append(endSong)
    songList.remove(endSong)
    for i in range(bagSize):
        newSong = random.choice(songList)
        songList.remove(newSong)
        potentialPlaylist.append(newSong)
    return potentialPlaylist

def generateRandomPlaylist(songList, startSong, endSong, size):
    randomPlaylist = []
    randomPlaylist.append(startSong)
    songList.remove(startSong)
    songList.remove(endSong)
    for i in range(size):
        newSong = random.choice(songList)
        songList.remove(newSong)
        randomPlaylist.append(newSong)
    randomPlaylist.append(endSong)
    return randomPlaylist


def main():

    print("Creating Song Objects...")
    songList = createSongs()
    oldList = createSongs()

    startSong = songList[393] #Graveyard by Halsey
    endSong = songList[183] #The Bones by Maren Morris
    #random = generateRandomPlaylist(songList, startSong, endSong, 4)
    #for song in random:
    #    print(str(song))

    chooseList = chooseTheSongs(songList, startSong, endSong, 200)
    #print(chooseList)
    #print(len(chooseList))
    #print(len(songList))
    print("complete!")


    print()
    print("Constructing Graph...")
    graph = SongGraph(chooseList, chooseList[0], chooseList[1])
    #print(str(graph))
    #print(songList)
    #graph.editGraphForSearch(76,46)
    #print(str(graph))
    print("complete!")

    print()
    print("Calculating best playlist with:")
    print("Start Song: " + str(startSong))
    print("End Song: " + str(endSong))
    result = graph_algs.aStar(graph)
    #print(result)
    print()
    print(graph_algs.prettyPath(graph, result))





if __name__ == "__main__":
    main()
