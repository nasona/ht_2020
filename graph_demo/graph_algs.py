"""
Abby Nason
graph_algs.py
Honors Thesis

contains functions for the graph algorithms that will run to create
the playlists
"""

def aStar(graph, startVertex, endVertex):
    """implementing shortest paths algorithm"""
    playGraph = graph
    open = []
    closed = [startVertex]
    #set start vertex distance to zero
    for vertex in graph.vertices():
        if vertex != startVertex:
            open.append(vertex)
            if vertex in startVertex.neighboringVertices():
                print("needs work")
                #set row's distance cell to the edge's weight + dist to goal
                #set the row's path to cell to source vertex
            else:
                print("needs work")
                #set the row's distance cell to infinity
                #set the row's path cell to undefined
    while not open.isEmpty():
        #Find the vertex F that is not yet included and has the minimal distance
        #Pop F from the open list
        #If F is the goal, stop processing
        #For each other vertex T not included
            #If there is an edge from F to T
                #Calculate a new distance: 	F's distance + edge's weight + estimated distance to goal
            #If new distance < T's distance in the results list
                #Set T's distance to new distance
                #Set T's path to F
	            #Push F onto the closed list
