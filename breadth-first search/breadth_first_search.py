from queue import Queue
import sys

grafo = {'Arad' : [('Timisoara', 118), ('Zerind', 75), ('Sibiu', 140)],
    'Zerind': [('Arad', 75), ('Oradea', 71)], 
    'Oradea': [('Zerind', 71), ('Sibiu', 151)],
    'Timisoara' : [('Arad', 118), ('Lugoj',  111)],
    'Sibiu' : [('Arad', 140), ('Oradea', 151), ('Rimnicu Vilcea', 80), ('Fagaras', 99)], 
    'Lugoj' : [('Timisoara',  111), ('Mehadia', 70)], 
    'Mehadia': [(('Lugoj', 70)), ('Drobeta', 75)], 
    'Drobeta' : [('Mehadia', 75), ('Craiova', 120)],
    'Rimnicu Vilcea' : [('Sibiu', 80), ('Craiova', 146), ('Pitesti', 97)], 
    'Fagaras': [('Sibiu', 99), ('Bucharest', 211)], 
    'Pitesti' : [('Rimnicu Vilcea', 97), ('Craiova', 138), ('Bucharest', 101)], 
    'Craiova' : [('Pitesti', 138), ('Rimnicu Vilcea', 146), ('Drobeta', 120)], 
    'Giurgiu': [('Bucharest', 90)], 
    'Bucharest':[('Urziceni', 85), ('Giurgiu', 90), ('Pitesti', 101), ('Fagaras', 211)], 
    'Urziceni' : [('Bucharest', 85), ('Hirsova', 98), ('Vaslui', 142)],
    'Hirsova' : [('Eforie', 86), ('Urziceni', 98)], 
    'Eforie': [('Hirsova', 86)],
    'Vaslui' : [('Iasi', 92), ('Urziceni', 142)], 
    'Iasi' : [('Neamt', 87), ('Vaslui', 92)], 
    'Neamt': [('Iasi', 87)]}


def breadth_first_search(graph, start, end):
    
    if start == end:
        return 'Path:' + start

    exploited = []
    borda = Queue()
    borda.put(start)

    while not borda.empty():
        vertex = borda.get()
     
        if vertex not in exploited:
           exploited.append(vertex)
          
        for vt in graph[vertex]:
               if vt[0] not in exploited:
                    if vt[0] == end: 
                        return 'Path: ' + ' -> '.join(exploited + [end])
                    borda.put(vt[0])


print(breadth_first_search(grafo, sys.argv[1], sys.argv[2]))
