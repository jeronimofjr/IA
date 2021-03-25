from vertex import *

class Graph:
    def __init__(self):
        self.camp = {}

    def addVertex(self, city):
        #vertex = Vertex(city)
        self.camp[city] = Vertex(city)
      
    def addEdge(self, city_a, city_b, distance):
        self.camp[city_a].addNeighbor(city_b, distance)
        self.camp[city_b].addNeighbor(city_a, distance)
    
    def getVertices(self):
        return  self.camp.keys()

    def getNeighbors(self, city):
        return self.camp[city].neighbors()

    def getEdges(self, city):
        return self.camp[city].edges()
