"""
Abby Nason
graph_algs.py
Honors Thesis

contains functions for the graph algorithms that will run to create
the playlists
"""
#percpetion of music, how people perceive music as similar, djs guide for setlist
#look for similar research like it but not the same topic
#the messenger metroidvania
MINIMUM_PLAYLIST_LENGTH = 5
BIG_NUMBER = 10000000
ARTIST_SELF_AVOIDANCE = True

def calculateEstimatedDistance(graph, layer):
    return graph.maxPossibleEdgeWeight()//2 * (MINIMUM_PLAYLIST_LENGTH - layer)

def aStar(graph):
    """implementing shortest paths algorithm"""
    open = []
    closed = [graph.getStartVertex()]
    tracker = {}
    for vertex in graph.vertices():
        if vertex == graph.getStartVertex():
            tracker[vertex.getLabel()] = {"included": True, "distance": 0, "path":[]}
        else:
            open.append(vertex)
            edge = vertex.getEdgeTo(graph.getStartVertex())
            if edge != None:
                if vertex.getSong().getArtist() != graph.getStartVertex().getSong().getArtist():
                    tracker[vertex.getLabel()] = {"included": False, "distance": edge.getWeight(), "path":[graph.getStartVertex().getLabel()]}
                else:
                    tracker[vertex.getLabel()] = {"included": False, "distance": (edge.getWeight()  + BIG_NUMBER//2), "path":[graph.getStartVertex().getLabel()]}
            else:
                tracker[vertex.getLabel()] = {"included": False, "distance": BIG_NUMBER, "path":[]}

    while not len(open) == 0:
        #Find the vertex F that is not yet included and has the minimal distance
        minLabel = None
        for vertex in open:
            if minLabel == None:
                minLabel = vertex.getLabel()
            elif tracker[minLabel]["distance"] > tracker[vertex.getLabel()]["distance"]:
                minLabel = vertex.getLabel()
        #Pop F from the open list
        chosenVertex = graph.getVertex(minLabel)
        open.remove(chosenVertex)

        #If F is the goal, stop processing
        if chosenVertex == graph.getEndVertex():
            break

        #For each other vertex T not included
        #when calculating new distance add a bunch for where I have been
        for vertex in open:
            edge = chosenVertex.getEdgeTo(vertex)
            #If there is an edge from F to T
            if edge != None:
                #Calculate a new distance: 	F's distance + edge's weight + estimated distance to goal
                #tracker[vertex.getLabel()]["distance"]
                if songAlreadyInPlaylist(vertex, graph, graph.getStartVertex(), chosenVertex, tracker):
                    #add biggest number
                    newDistance = tracker[chosenVertex.getLabel()]["distance"] + edge.getWeight() + calculateEstimatedDistance(graph, chosenVertex._layer) + BIG_NUMBER
                elif ARTIST_SELF_AVOIDANCE and artistAlreadyInPlaylist(vertex, graph, graph.getStartVertex(), chosenVertex, tracker):
                    #add big number (less than if song is already in playlist because less similar)
                    newDistance = tracker[chosenVertex.getLabel()]["distance"] + edge.getWeight() + calculateEstimatedDistance(graph, chosenVertex._layer) + BIG_NUMBER//2
                else:
                    newDistance = tracker[chosenVertex.getLabel()]["distance"] + edge.getWeight() + calculateEstimatedDistance(graph, chosenVertex._layer)
                #If new distance < T's distance in the results list
                if newDistance < tracker[vertex.getLabel()]["distance"]:
                    #Set T's distance to new distance
                    tracker[vertex.getLabel()]["distance"] = newDistance
                    #Set T's path to F
                    #tracker[vertex.getLabel()]["path"] = tracker[choosenVertex.getLabel()]["path"]
                    #tracker[vertex.getLabel()]["path"].append(chosenVertex.getLabel())
                    tracker[vertex.getLabel()]["path"] = [chosenVertex.getLabel()]
	                #Push F onto the closed list
                    closed.append(vertex)
                    tracker[vertex.getLabel()]["included"] = True
    return tracker

def prettyPath(graph, tracker):
    try:
        prettyPrint = ""
        path = getPath(graph.getStartVertex(), graph.getEndVertex(), tracker)
        for vertexLabel in path:
            prettyPrint += str(graph.getVertex(vertexLabel).getSong()) + "\n"
        return prettyPrint
    except:
        print("There is no path between these songs.")

def getPath(startVertex, endVertex, tracker):
    currentSong = endVertex.getLabel()
    path = [currentSong]
    while currentSong != startVertex.getLabel():
        currentSong = tracker[currentSong]["path"][0]
        path = [currentSong] + path
    return path

def songAlreadyInPlaylist(compVertex, graph, startVertex, endVertex, tracker):
    path = getPath(startVertex, endVertex, tracker)
    for vertex in path:
        if graph.getVertex(vertex).getSong() == compVertex.getSong():
            return True
    return False

def artistAlreadyInPlaylist(compVertex, graph, startVertex, endVertex, tracker):
    path = getPath(startVertex, endVertex, tracker)
    for vertex in path:
        if graph.getVertex(vertex).getSong().getArtist() == compVertex.getSong().getArtist():
            return True
    return False
