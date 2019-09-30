"""
Abby Nason
graph_algs.py
Honors Thesis

contains functions for the graph algorithms that will run to create
the playlists
"""

MINIMUM_PLAYLIST_LENGTH = 5
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
                tracker[vertex.getLabel()] = {"included": False, "distance": edge.getWeight(), "path":[vertex.getLabel()]}
            else:
                tracker[vertex.getLabel()] = {"included": False, "distance": 0, "path":[]}
    while not open.isEmpty():
        #Find the vertex F that is not yet included and has the minimal distance
        minLabel = None
        for label in tracker:
            if minLabel == None:
                minLabel = tracker[label]
            else:
                if tracker[minLabel] > tracker[label]:
                    #Pop F from the open list
                    chosenVertex = open.pop(graph.getVertex(minLabel))
        #If F is the goal, stop processing
        if chosenVertex = graph.getEndVertex():
            break
        #For each other vertex T not included
        for vertex in open:
            edge = chosenVertex.getEdgeTo(vertex)
            #If there is an edge from F to T
            if edge != None:
                #Calculate a new distance: 	F's distance + edge's weight + estimated distance to goal
                #tracker[vertex.getLabel()]["distance"]
                newDistance = tracker[chosenVertex.getLabel()] + edge.getWeight() + calculateEstimatedDistance(graph, chosenVertex._layer)
                #If new distance < T's distance in the results list
                if newDistance < tracker[vertex.getLabel()]["distance"]:
                    #Set T's distance to new distance
                    tracker[vertex.getLabel()]["distance"] = newDistance
                    #Set T's path to F
                    tracker[vertex.getLabel()]["path"] = tracker[choosenVertex.getLabel()]["path"]
                    tracker[vertex.getLabel()]["path"].append(choosenVertex.getLabel())
	                #Push F onto the closed list
                    closed.append(vertex)
                    tracker[vertex.getLabel()]["included"] = True
