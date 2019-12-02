"""
Abby Nason
graph.py
Honors Thesis

Class to create a graph made up of songs

Citations: Dr. Ken Lambert Project 12 graphs.py from CSCI 112
"""
WEIGHTS = {"camelot": 4, "bpm": 4, "track number": 0, "single": 2, "album": 1, "year and genre": 4}
MINIMUM_PLAYLIST_LENGTH = 8
BPM_RANGE = 20
MIN_BPM_CHANGE = 5
#fully connected graph and need to figure out a way to force a path of a minimum length
#mulitple levels of the same songs
#don't include intermediate level in the final song
#prevent going back between two songs that are similar
#or keep track of which songs you've seen and add a larger weight to songs we've already seen
#minimum amount of distance two songs could have minus the number of songs left
#place all the songs in a row, unique color per song
class Edge(object):
    def __init__(self, vertex1, vertex2, weight = None):
        """initializes an edge object given the vertices and the weight"""
        self._vertex1 = vertex1
        self._vertex2 = vertex2
        self._weight = weight
        self._mark = False

    def clearMark(self):
        """removes the mark from the edge"""
        self._mark = False

    def __eq__(self, other):
        """equality checker"""
        if self is other: return True
        if type(self) != type(other):
            return False
        #print(self._vertex1 + " and " + other._vertex1 + " + " +  self._vertex2 + " and " + other._vertex2)
        return (self._vertex1 == other._vertex1 and self._vertex2 == other._vertex2) or \
               (self._vertex1 == other._vertex2 and self._vertex2 == other._vertex1)

    def getOtherVertex(self,  thisVertex):
        """given one of the endpoints of an edge, returns the other"""
        if thisVertex == None or thisVertex == self._vertex2:
            return self._vertex1
        else:
            return self._vertex2

    def getWeight(self):
        """returns the weight of the edge"""
        return self._weight

    def isMarked(self):
        """returns true if the edge is marked and
        false otherwise"""
        return self._mark

    def markEdge(self):
        """marks the edge"""
        self._mark = True

    def setWeight(self, weight):
        """assigns the edge the given weight"""
        self._weight = weight

    def __str__(self):
        """returns the string representation of an edge"""
        return str(self._vertex1) + "---" + str(self._vertex2)   + ":" + str(self._weight)

class Vertex(object):
    def __init__(self, label):
        """initializes a vertex object given the label"""
        self._label = label
        self._edges = []
        self._mark = False

    def clearMark(self):
        """removes the mark from a vertex"""
        self._mark = False

    def getLabel(self):
        """returns the label of the vertex"""
        return self._label

    def isMarked(self):
        """returns true if a vertex is marked and
        false otherwise"""
        return self._mark

    # vvvvv check to make sure this is doing what you want
    def setLabel(self, label, graph):
        """sets the label of a vertex given the graph"""
        graph._vertices.pop(self._label, None)
        graph._vertices[label] = self
        self._label = label

    def markVertex(self):
        """marks a vertex"""
        self._mark = True

    def __str__(self):
        """returns string representation of the vertex"""
        return str(self._label)

    # Methods used by WeightedUndirectedGraph

    def addEdgeTo(self, otherVertex, weight):
        """add and edge to the graph given the other endpoint
        and the weight of the edge"""
        edge = Edge(self, otherVertex, weight)
        self._edges.append(edge)

    def getEdgeTo(self, otherVertex):
        """get the edge from the vertex to another vertex"""
        for edge in self._edges:
            if edge.getOtherVertex(self) == otherVertex:
                return edge
        return None
        #for i in range(0, 20):
        #    edge = Edge(self, otherVertex, i)
        #    try:
        #        return self._edges[self._edges.index(edge)]
        #    except:
                #return None
        #        continue
        #return None

    def incidentEdges(self):
        """removes the edges connected to the vertex"""
        return iter(self._edges)

    def neighboringVertices(self):
        """removes the neighboring vertices to the vertex"""
        vertices = []
        for edge in self._edges:
            vertices.append(edge.getOtherVertex(self))
        return iter(vertices)

    def removeEdgeTo(self, toVertex):
        """removes an edge given the other endpoint"""
        edge = LinkedEdge(self, toVertex)
        if edge in self._edges:
            self._edges.remove(edge)
            return True
        else:
            return False

class WeightedUndirectedGraph(object):

    def __init__(self, sourceCollection = None):
        """intializes a weighted, undirected graph object"""
        self._vertexCount = 0
        self._edgeCount = 0
        self._vertices = {}
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)

    # Methods for clearing, marks, sizes, string rep

    def clear(self):
        """clears the graph of the vertices and edges and
        resets vertex and edge counts to 0"""
        self._vertexCount = 0
        self._edgeCount = 0
        self._vertices = {}

    def clearEdgeMarks(self):
        """clear the marks on the edges (for running algorithms)"""
        for edge in self.edges():
            edge.clearMark()

    def clearVertexMarks(self):
        """clear the marks on the vertices (for running algorithms)"""
        for vertex in self.vertices():
            vertex.clearMark()

    def __len__(self):
        """measures length by the number of vertices"""
        return self._vertexCount

    def sizeEdges(self):
        """returns the number of edges in a graph"""
        return self._edgeCount

    def sizeVertices(self):
        """returns the number of vertices in the graph"""
        return len(self)

    def __str__(self):
        """string representation of the graph"""
        result = str(self.sizeVertices()) + " Vertices: "
        for vertex in self._vertices:
            result += " " + str(vertex)
        result += "\n";
        result += str(self.sizeEdges()) + " Edges: "
        for edge in self.edges():
            result += "\n" + str(edge)
        return result

    def add(self, label):
        """add function for compatibility with other collections"""
        self.addVertex(label)

    # Vertex related methods
    def addVertex(self, label):
        """adds a vertex to the graph given the label"""
        self._vertices[label] = Vertex(label)
        self._vertexCount += 1

    def containsVertex (self, label):
        """returns true if the graph contains a vertex and
        false otherwise"""
        return label in self._vertices

    def getVertex(self, label):
        """returns a vertex given its label"""
        return self._vertices[label]

    def removeVertex(self,  label):
        """removes a vertex from the graph and the edges coming from it"""
        removedVertex = self._vertices.pop(label, None)
        if removedVertex is None:
            return False
        # Remove edges connected to vertex
        for vertex in self.vertices():
            if vertex.removeEdgeTo(removedVertex):
                self._edgeCount -= 1
        self._vertexCount -= 1
        return True

    # Methods related to edges
    def addEdge(self, vertex1Label, vertex2Label, weight):
        """adds an edge to the graph given the endpoints and
        the weight of the edge"""
        vertex1 = self.getVertex(vertex1Label)
        vertex2   = self.getVertex(vertex2Label)
        vertex1.addEdgeTo(vertex2, weight)
        self._edgeCount += 1

    def containsEdge(self, vertex1Label, vertex2Label):
        """returns true if a graph contains an edge and
        false otherwise"""
        return self.getEdge(vertex1Label, vertex2Label) != None

    def getEdge(self, vertex1Label, vertex2Label):
        """returns an edge in a graph given the endpoints"""
        vertex1 = self._vertices[vertex1Label]
        vertex2  = self._vertices[vertex2Label]
        return vertex1.getEdgeTo(vertex2)

    def removeEdge (self, vertex1Label, vertex2Label):
        """removes an edge in the graph give the endpoints"""
        vertex1 = self.getVertex(vertex1Label)
        vertex2 = self.getVertex(vertex2Label)
        edgeRemovedResponse = fromVertex.removeEdgeTo(vertex2)
        if edgeRemovedResponse:
            self._edgeCount -= 1
        return edgeRemovedResponse

    # Iterators
    def edges(self):
        """returns the edges in the graph"""
        result = list()
        for vertex in self.vertices():
            result += list(vertex.incidentEdges())
        return iter(result)

    def vertices(self):
        """returns the vertices in the graph"""
        return iter(self._vertices.values())

    def incidentEdges(self, label):
        """returns the edges connected to self"""
        return self._vertices[label].incidentEdges()

    def neighboringVertices(self, label):
        """returns the verticies connected to self"""
        return self._vertices[label].neighboringVertices()

class Camelot(object):
    def __init__(self, hour, wheel):
        """initializes the camelot object with the hour position on the wheel
        and if its on the major or minor wheel"""
        self._hour = hour
        self._wheel = wheel

    def isCompatible(self, other):
        """determines if two camelot labels are compatible"""
        #number part of the label must be within the one of each other
        if self._hour - other._hour >= -1 and self._hour - other._hour <= 1 and self._wheel == other._wheel:
            return True
        #or if numbers are the same hour then they can move between
        #the minor (A) and major(B) wheels
        elif self._hour == other._hour:
            return True
        else:
            return False

    def __str__(self):
        """string representation of camelot object"""
        return str(self._hour) + self._wheel

class Song(object):
    def __init__(self, id, artist, title, album, trackNumber, deluxeOnly, single, genre, key, bpm, camelot, year):
        """initializes the song object with the provided information"""
        self._id = id
        self._artist = artist
        self._title = title
        self._album = album
        self._trackNumber = trackNumber
        self._deluxeOnly = deluxeOnly
        self._single = single
        self._genre = genre
        self._key = key
        self._bpm = bpm
        self._camelot = camelot
        self._year = year

    def isCamelotCompatible(self, other):
        """returns true if two songs follow the correct
        camelot rules for compatibility and false otherwise"""
        return self._camelot.isCompatible(other._camelot)

    def isBpmCompatible(self, other):
        """returns true if two songs are within 20 bpm of each other
        and false otherwise"""
        if self._bpm - other._bpm >= -BPM_RANGE and self._bpm - other._bpm <= BPM_RANGE:
            if self._bpm - other._bpm >= MIN_BPM_CHANGE and self._bpm - other._bpm <= -MIN_BPM_CHANGE:
                return True
        else:
            return False

    def hasSameTrackNumber(self, other):
        """returns true if two songs have the same track number
        and false otherwise"""
        if self._trackNumber == other._trackNumber:
            return True
        else:
            return False

    def singleStatus(self, other):
        """returns true if the song was a radio single
        and false otherwise"""
        if self._single == other._single and self._single == True:
            return True
        else:
            return False

    def onSameAlbum(self, other):
        """returns true if two songs are on the same _album
        and false otherwise"""
        if self._album == other._album:
            return True
        else:
            return False

    def similarYear(self, other):
        """returns true if the year the song was released within
        three years of each other or false otherwise"""
        if self._year - other._year >= -2 and self._year <= 2:
            return True
        else:
            return False

    def hasSameGenre(self, other):
        """returns true if the genres of two songs are the same
        and false otherwise"""
        if self._genre == self._other:
            return True
        else:
            return False

    def __str__(self):
        """displays the song title and artist"""
        return self._title + " by " + self._artist

    def allSongInfo(self):
        """displays all the info for a song"""
        songString = "id: " + self._id + "\ntitle: " + self._title + \
                    "\nartist: " + self._artist + "\nalbum: " + self._album + \
                    "\ntrack number: " + self._trackNumber + "\ngenre: " + self._genre + \
                    "\non deluxe album only: " + self._deluxeOnly + "\nsingle promotion: " + \
                    self._single + "key: " + self._key + "camelot: " + self._camelot + \
                    "\nbeats per minute: " + self._bpm
        return songString

class SongVertex(Vertex):
    def __init__(self, song, layer=""):
        """initializes a song vertex"""
        self._song = song
        self._layer = layer
        Vertex.__init__(self, str(self._song._id) + "x" + str(layer))

    def setLayer(self, layer):
        """sets the layer of a song vertex"""
        self._layer = layer

    def getSong(self):
        return self._song

    def __str__(self):
        """returns string representation of the vertex"""
        return str(self._label) + " (" + str(self._song) + ")"

class SongGraph(WeightedUndirectedGraph):
    def __init__(self, songList=None, startSong=None, endSong=None):
        """initializes a song graph with the given parameters"""
        self._startSong = startSong
        self._endSong = endSong
        self._layers = {}
        self._edgeInfo = []
        for i in range(1, MINIMUM_PLAYLIST_LENGTH):
            self._layers[i] = []
        WeightedUndirectedGraph.__init__(self, songList)
        self.calculateWeightedEdges()
        self.createLayerFormation()

    def addVertex(self, song):
        """adds a vertex as a song vertex"""
        if song != self._startSong and song != self._endSong:
            for layer in range(1, MINIMUM_PLAYLIST_LENGTH):
                currentSong = SongVertex(song, layer)
                self._vertices[str(song._id) + "x" + str(layer)] = currentSong
                self._layers[layer].append(currentSong)
                self._vertexCount += 1
        elif song == self._startSong:
            startSong = SongVertex(song, 0)
            self._vertices[str(song._id) + "x" + str(0)] = startSong
            self._layers[0] = [startSong]
            self._vertexCount += 1
        elif song == self._endSong:
            endSong = SongVertex(song, MINIMUM_PLAYLIST_LENGTH)
            self._vertices[str(song._id) + "x" + str(MINIMUM_PLAYLIST_LENGTH)] = endSong
            self._layers[MINIMUM_PLAYLIST_LENGTH] = [endSong]
            self._vertexCount += 1

    def createLayerFormation(self):
        """makes the appropriate connections between the vertecies in layers"""
        for i in range(len(self._layers)-1):
            for aboveVertex in self._layers[i]:
                for belowVertex in self._layers[i+1]:
                    for entry in self._edgeInfo:
                        if entry._vertex1 == aboveVertex.getLabel().split()[0] and entry._vertex2 == belowVertex.getLabel().split()[0]:
                            #print(aboveVertex.getLabel() + "---" + belowVertex.getLabel())
                            self.addEdge(aboveVertex._label, belowVertex._label, entry._weight)

    def maxPossibleEdgeWeight(self):
        """gets the max possible weight that an edge could have"""
        total = 0
        for key in WEIGHTS:
            total += WEIGHTS[key]
        return total

    def increaseRestOfEdges(self, vertex1, vertex2):
        """increases the edge weights of the successive layers between the two
        songs given by the two vertices"""
        song1 = vertex1._song
        song2 = vertex2._song
        layer1 = vertex1._layer
        layer2 = vertex2._layer
        if layer1 > 0:
            for i in range(layer2, MINIMUM_PLAYLIST_LENGTH - 1):
                aboveSong = self._layers[i][str(song1._id) + "x" + str(i)]
                belowSong = self._layers[i+1][str(song2._id) + "x" + str(i+1)]
                aboveSong.getEdgeTo(belowSong).setWeight(10000)


    def calculateWeightedEdges(self):
        """connects the graph and calculates the weight edges"""
        ##put the magic weight numbers in a dictionary at top of the file
        weight = 0
        for mainVertex in self.vertices():
            for compVertex in self.vertices():
                if mainVertex._label.split("x")[0] != compVertex._label.split("x")[0] and (mainVertex._layer - compVertex._layer == -1 or mainVertex._layer - compVertex._layer == 1):
                #and not self.containsEdge(compVertex._label, mainVertex._label):
                    if mainVertex._song.isCamelotCompatible(compVertex._song):
                        weight += WEIGHTS["camelot"]
                    if mainVertex._song.isBpmCompatible(compVertex._song):
                        weight += WEIGHTS["bpm"]
                    if mainVertex._song.hasSameTrackNumber(compVertex._song):
                        weight += WEIGHTS["track number"]
                    if mainVertex._song.singleStatus(compVertex._song):
                        weight += WEIGHTS["single"]
                    if mainVertex._song.onSameAlbum(compVertex._song):
                        weight += WEIGHTS["album"]
                    if mainVertex._song.similarYear(compVertex._song) and mainVertex._song.hasSameGenre(compVertex._song):
                        weight += WEIGHTS["year and genre"]
                if weight > 0:
                    self.addEdge(mainVertex._label, compVertex._label, self.maxPossibleEdgeWeight() + 1 - weight)
                weight = 0

    def getStartVertex(self):
        """returns the start vertex in the playlist"""
        return self._layers[0][0]

    def getEndVertex(self):
        """returns the end vertex in the playlist"""
        return self._layers[MINIMUM_PLAYLIST_LENGTH][0]
