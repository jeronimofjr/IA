class Vertex:
    def __init__(self, city, value):
        self.city = city
        self.adjacent = {}
        self.value = value

    def addNeighbor(self, city, distance):
        self.adjacent[city] = distance

    def neighbors(self):
        return self.adjacent.keys()

    def edges(self):
        return self.adjacent.items()

    def costValue(self):
        return self.value

    def __str__(self):
        return self.city