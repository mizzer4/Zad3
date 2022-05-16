import graph_util

from time import time
from graph import Graph 
from copy import deepcopy 

def main(option):
    if option == 1:
        zad1()
    else:
        zad2()

def zad1():
    n = 11
    density = 30

    graph = graph_util.graph_generator(n, density)
    print(graph)
    graphEuler = deepcopy(graph)
    g1 = Graph(n)
    g1.graph = graphEuler

    starttime_euler = time()
    path = g1.eulerCycle()
    stoptime_euler = time()
    totaltime_euler = int((stoptime_euler - starttime_euler) * 1000)

    print('-> euler [' + str(n) + ']:' + str(totaltime_euler) + 'ms')    
    print(graph_util.path_toString(path))

    graphHamilton = deepcopy(graph)
    g2 = Graph(n)
    g2.graph = graphHamilton

    starttime_hamilton = time()
    path = g2.hamCycle()
    stoptime_hamilton = time()
    totaltime_hamilton = int((stoptime_hamilton - starttime_hamilton) * 1000)

    print('-> hamilton [' + str(n) + ']:' + str(totaltime_hamilton) + 'ms')
    print(graph_util.path_toString(path))


def zad2():
    n = 15
    density = 50

    graph = graph_util.graph_generator(n, density)
    g = Graph(n)
    g.graph = graph

    starttime_hamilton = time()
    path = g.hamCycle_AllPaths()
    stoptime_hamilton = time()
    totaltime_hamilton = int((stoptime_hamilton - starttime_hamilton) * 1000)

    print('-> hamilton [' + str(n) + ']:' + str(totaltime_hamilton) + 'ms')
    print(graph_util.path_toString(path))


if __name__=="__main__":
    main()
