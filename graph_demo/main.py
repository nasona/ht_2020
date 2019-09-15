from song_graph import Song
from song_graph import Camelot
from song_graph import SongGraph

def main():
    one = Song("1", "Taylor Swift", "New Romantics", "1989", 16, True, True, "Pop", "F Major", 122, Camelot(7,"B"), 2014)
    two = Song("2", "Taylor Swift", "I Knew You Were Trouble", "Red", 4, False, True, "Country", "F# Major", 154, Camelot(2,"B"), 2012)
    three = Song("3", "Taylor Swift", "Enchanted", "Speak Now", 9, False, False, "Country", "Ab Major", 164, Camelot(4,"B"), 2010)
    four = Song("4", "Taylor Swift", "Style", "1989", 3, False, True, "Pop", "D Major", 95, Camelot(10,"B"), 2014)
    five = Song("5", "Taylor Swift", "Haunted", "Speak Now", 12, False, False, "Country", "F Major", 162, Camelot(7,"B"), 2010)
    six = Song("6", "Taylor Swift", "I Almost Do", "Red", 7, False, False, "Country", "E Major", 146, Camelot(12,"B"), 2012)
    seven = Song("7", "Taylor Swift", "Wildest Dreams", "1989", 9, False, True, "Pop", "Ab Major", 140, Camelot(4,"B"), 2014)
    eight = Song("8", "Taylor Swift", "Delicate", "reputation", 5, False, True, "Pop", "A Minor", 95, Camelot(8,"A"), 2017)
    nine = Song("9", "Taylor Swift", "Miss Americana & the Heartbreak Prince", "Lover", 7, False, False, "Pop", "B Minor", 150, Camelot(10,"A"), 2019)
    ten = Song("10", "Taylor Swift", "Forever & Always", "Fearless", 11, False, False, "Country", "Bb Major", 128, Camelot(6,"B"), 2008)
    songList = [one, two, three, four, five, six, seven, eight, nine, ten]
    graph = SongGraph(songList)
    print(str(graph))

if __name__ == "__main__":
    main()
