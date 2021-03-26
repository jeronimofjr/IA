from vertex import *

class Graph:
    def __init__(self):
        self.camp = {}

    def addVertex(self, city, value):
        vertex = Vertex(city, value)
        self.camp[city] = vertex
      
    def addEdge(self, city_a, city_b, distance, value_a=0, value_b=0):
        if city_a not in self.camp:
            self.addVertex(city_a, value_a)
        if city_b not in self.camp:
            self.addVertex(city_b, value_b)
        
        self.camp[city_a].addNeighbor(city_b, distance)
        self.camp[city_b].addNeighbor(city_a, distance)
    
    def getVertices(self):
        return  self.camp.keys()

    def getNeighbors(self, city):
        return self.camp[city].neighbors()

    def getCost(self, city):
        return self.camp[city].costValue()

    def getEdges(self, city):
        return self.camp[city].edges()