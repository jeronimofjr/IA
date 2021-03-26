from create_graph import create_graph
from vertex import *
from graph import *
import queue
import os
import sys 



def a_star(graph, start, end):
    cost = 0

    borda = queue.PriorityQueue()
    borda.put((0, 0, [start]))
    explorados = []

    while not borda.empty():
        u = borda.get()
        
        if end in u[2]:
            return ' -> '.join(u[2]) + '\ncost: ' + str(u[1])

        cost = u[1]
        explorados.append(u[2][-1])
        for neighbor in graph.getEdges(u[2][-1]):
            if neighbor[0] not in explorados:
                path = u[2][:]
                path.append(neighbor[0])
                borda.put((graph.getCost(neighbor[0]) + neighbor[1], cost + neighbor[1], path))


graph = create_graph()
print(a_star(graph, sys.argv[1], sys.argv[2]))
