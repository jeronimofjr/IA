from create_graph import create_graph
from vertex import *
from graph import *
import queue
import os
import sys 


def uniform_cost_search(graph, start, end):
    cost = 0
    explorados = []

    borda = queue.PriorityQueue()
    borda.put((0, [start]))

    while not borda.empty():
        u = borda.get()
    
        if end in u[1]:
            return ' -> '.join(u[1]) + '\ncost: ' + str(u[0])

        cost = u[0]
        explorados.append(u[1][-1])
        for neighbor in graph.getEdges(u[1][-1]):
            if neighbor[0] not in explorados:
                path = u[1][:]
                path.append(neighbor[0])
                borda.put((cost + neighbor[1], path))

graph = create_graph()
print(uniform_cost_search(graph, sys.argv[1], sys.argv[2]))

