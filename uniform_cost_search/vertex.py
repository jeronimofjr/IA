class Vertex:
    def __init__(self, city):
        self.city = city
        self.adjacent = {}

    def addNeighbor(self, city, distance):
        self.adjacent[city] = distance

    def neighbors(self):
        return self.adjacent.keys()

    def edges(self):
        return self.adjacent.items()

    def __str__(self):
        return self.city