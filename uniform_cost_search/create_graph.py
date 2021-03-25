from vertex import *
from graph import *

def create_graph():
    citys_romania = ['Arad', 'Zerind', 'Oradea', 'Timisoara', 'Sibiu', 'Lugoj', 'Mehadia', 'Drobeta',
    'Rimnicu Vilcea', 'Fagaras', 'Pitesti', 'Craiova', 'Giurgiu', 'Bucharest', 'Urziceni',
    'Hirsova', 'Eforie','Vaslui', 'Iasi', 'Neamt']

    graph = Graph()

    for city in citys_romania:
        graph.addVertex(city)

    graph.addEdge('Arad', 'Timisoara', 118)
    graph.addEdge('Arad', 'Zerind', 75)
    graph.addEdge('Arad', 'Sibiu', 140)
    graph.addEdge('Timisoara', 'Lugoj',  111)
    graph.addEdge('Zerind', 'Oradea', 71)
    graph.addEdge('Oradea', 'Sibiu', 151)
    graph.addEdge('Sibiu', 'Fagaras', 99)
    graph.addEdge('Sibiu', 'Rimnicu Vilcea', 80)
    graph.addEdge('Lugoj', 'Mehadia', 70)
    graph.addEdge('Mehadia', 'Drobeta', 75)
    graph.addEdge('Drobeta', 'Craiova', 120)
    graph.addEdge('Craiova', 'Rimnicu Vilcea', 146)
    graph.addEdge('Craiova', 'Pitesti', 138)
    graph.addEdge('Rimnicu Vilcea', 'Pitesti', 97)
    graph.addEdge('Fagaras', 'Bucharest', 211)
    graph.addEdge('Pitesti', 'Bucharest', 101)
    graph.addEdge('Giurgiu', 'Bucharest', 90)
    graph.addEdge('Urziceni', 'Bucharest', 85)
    graph.addEdge('Urziceni', 'Hirsova', 98)
    graph.addEdge('Urziceni', 'Vaslui', 142)
    graph.addEdge('Hirsova', 'Eforie', 86)
    graph.addEdge('Vaslui', 'Iasi', 92)
    graph.addEdge('Iasi', 'Neamt', 87)
    return graph