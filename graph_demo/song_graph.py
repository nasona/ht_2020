"""
Abby Nason
graph.py
Honors Thesis

Class to create a graph made up of songs

citations: Dr. Ken Lambert Project 12 graphs.py from CSCI 112
"""
class Edge(object):
    def __init__(self, vertex1, vertex2, weight = None):
        self._vertex1 = vertex1
        self._vertex2 = vertex2
        self._weight = weight
        self._mark = False

    def clearMark(self):
        self._mark = False

    def __eq__(self, other):
        if self is other: return True
        if type(self) != type(other):
            return False
        return (self._vertex1 == other._vertex1 and self._vertex2 == other._vertex2) or \
               (self._vertex1 == other._vertex2 and self._vertex2 == other._vertex1)

    def getOtherVertex(self,  thisVertex):
        if thisVertex == None or thisVertex == self._vertex2:
            return self._vertex1
        else:
            return self._vertex2

    def getWeight(self):
        return self._weight

    def isMarked(self):
        return self._mark

    def markEdge(self):
        self._mark = True

    def setWeight(self, weight):
        self._weight = weight

    def __str__(self):
        return str(self._vertex1) + "---" + str(self._vertex2)   + ":" + str(self._weight)

class Vertex(object):
    def __init__(self, label):
        self._label = label
        self._edges = []
        self._mark = False

    def clearMark(self):
        self._mark = False

    def getLabel(self):
        return self._label

    def isMarked(self):
        return self._mark

    # vvvvv check to make sure this is doing what you want
    def setLabel(self, label, graph):
        graph._vertices.pop(self._label, None)
        graph._vertices[label] = self
        self._label = label

    def markVertex(self):
        self._mark = True

    def __str__(self):
        return str(self._label)

    # Methods used by LinkedGraph

    def addEdgeTo(self, otherVertex, weight):
        edge = LinkedEdge(self, otherVertex, weight)
        self._edges.append(edge)

    def getEdgeTo(self, otherVertex):
        edge = Edge(self, otherVertex)
        try:
            return self._edges[self._edges.index(edge)]
        except:
            return None

    def incidentEdges(self):
        return iter(self._edges)

    def neighboringVertices(self):
        vertices = []
        for edge in self._edges:
            vertices.append(edge.getOtherVertex(self))
        return iter(vertices)

    def removeEdgeTo(self, toVertex):
        edge = LinkedEdge(self, toVertex)
        if edge in self._edges:
            self._edges.remove(edge)
            return True
        else:
            return False

class WeightedUndirectedGraph(object):

    def __init__(self, sourceCollection = None):
        self._vertexCount = 0
        self._edgeCount = 0
        self._vertices = {}
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)

    # Methods for clearing, marks, sizes, string rep

    def clear(self):
        self._vertexCount = 0
        self._edgeCount = 0
        self._vertices = {}

    def clearEdgeMarks(self):
        for edge in self.edges():
            edge.clearMark()

    def clearVertexMarks(self):
        for vertex in self.vertices():
            vertex.clearMark()

    def __len__(self):
        return self._vertexCount

    def sizeEdges(self):
        return self._edgeCount

    def sizeVertices(self):
        return len(self)

    def __str__(self):
        result = str(self.sizeVertices()) + " Vertices: "
        for vertex in self._vertices:
            result += " " + str(vertex)
        result += "\n";
        result += str(self.sizeEdges()) + " Edges: "
        for edge in self.edges():
            result += " " + str(edge)
        return result

    def add(self, label):
        """For compatibility with other collections."""
        self.addVertex(label)

    # Vertex related methods
    def addVertex(self, label):
        self._vertices[label] = Vertex(label)
        self._vertexCount += 1

    def containsVertex (self, label):
        return label in self._vertices

    def getVertex(self, label):
        return self._vertices[label]

    def removeVertex(self,  label):
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
        vertex1 = self.getVertex(vertex1Label)
        vertex2   = self.getVertex(vertex2Label)
        vertex1.addEdgeTo(vertex2, weight)
        self._edgeCount += 1

    def containsEdge(self, vertex1Label, vertex2Label):
        return self.getEdge(vertex1Label, vertex2Label) != None

    def getEdge(self, vertex1Label, vertex2Label):
        vertex1 = self._vertices[vertex1Label]
        vertex2  = self._vertices[vertex2Label]
        return vertex1.getEdgeTo(vertex2)

    def removeEdge (self, vertex1Label, vertex2Label):
        vertex1 = self.getVertex(vertex1Label)
        vertex2 = self.getVertex(vertex2Label)
        edgeRemovedResponse = fromVertex.removeEdgeTo(vertex2)
        if edgeRemovedResponse:
            self._edgeCount -= 1
        return edgeRemovedResponse

    # Iterators
    def edges(self):
        result = list()
        for vertex in self.vertices():
            result += list(vertex.incidentEdges())
        return iter(result)

    def vertices(self):
        return iter(self._vertices.values())

    def incidentEdges(self, label):
        return self._vertices[label].incidentEdges()

    def neighboringVertices(self, label):
        return self._vertices[label].neighboringVertices()

class Camelot(object):
    def __init__(self, hour, wheel):
        self._hour = hour
        self._wheel = wheel

    def isCompatible(self, other):
        if self._hour - other._hour >= -1 and self._hour - other._hour <= 1 and self._wheel == other._wheel:
            return True
        elif self._hour == other._hour:
            return True
        else:
            return False

class Song(object):
    def __init__(self, id, artist, title, album, trackNumber, deluxeOnly, single, genre, key, bpm, camelot, year):
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
        return self._camelot.isCompatible(other._camelot)

    def isBpmCompatible(self, other):
        if self._bpm - other._bpm >= -10 or self._bpm - other._bpm <= 10:
            return True
        else:
            return False

    def hasSameTrackNumber(self, other):
        if self._trackNumber == other._trackNumber:
            return True
        else:
            return False

    def singleStatus(self, other):
        if self._single == other._single and self._single == True:
            return True
        else:
            return False

    def onSameAlbum(self, other):
        if self._album == other._album:
            return True
        else:
            return False

    def similarYear(self, other):
        if self._year - other._year >= -3 and self._year <= 3:
            return True
        else:
            return False

    def hasSameGenre(self, other):
        if self._genre == self._other:
            return True
        else:
            return False

    def __str__(self):
        return self._metadata["title"] + " by " + self._metadata["artist"]

    def allSongInfo(self):
        songString = "id: " + self._id + "\ntitle: " + self._title + \
                    "\nartist: " + self._artist + "\nalbum: " + self._album + \
                    "\ntrack number: " + self._trackNumber + "\ngenre: " + self._genre + \
                    "\non deluxe album only: " + self._deluxeOnly + "\nsingle promotion: " + \
                    self._single + "key: " + self._key + "camelot: " + self._camelot + \
                    "\nbeats per minute: " + self._bpm

class SongVertex(Vertex):
    def __init__(self, song):
        self._song = song
        Vertex.__init__(self, self._song._id)

class SongGraph(WeightedUndirectedGraph):
    def __init__(self, songList=None):
        """initializes a song graph with the given parameters"""
        if songList != None:
            songLabels = []
            for song in songList:
                songLabels.append(song._id)
            WeightedUndirectedGraph.__init__(self, songLabels)
        else:
            WeightedUndirectedGraph.__init__(self, None)

    def addVertex(self, label):
        self._vertices[label] = SongVertex(label)
        self._vertexCount += 1

    def calculateWeightedEdges(self):
        for mainVertex in self._vertices:
            weight = 0
            for compVertex in self._vertices:
                if mainVertex != compVertex:
                    if mainVertex._song.isCamelotCompatible(compVertex._song):
                        weight += 7
                    if mainVertex._song.isBpmCompatible(compVertex._song):
                        weight += 5
                    if mainVertex._song.hasSameTrackNumber(compVertex._song):
                        weight += 3
                    if mainVertex._song.singleStatus(compVertex._song):
                        weight += 2
                    if mainVertex._song.onSameAlbum(compVertex._song):
                        weight += 1
                    if mainVertex._song.similarYear(compVertex._song) and mainVertex._song.hasSameGenre(compVertex._song):
                        weight += 1
            if weight > 0:
                self.addEdge(mainVertex, compVertex, 20 - weight)
