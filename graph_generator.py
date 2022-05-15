import numpy, math
import random

def graph_generator(n, density):
    print('------>Started generating edges')
    edges = create_edges_all(n)
    print('------>Ended generating edges')
    print('------>Started densifying edges')
    edges_densify(n, edges, density)
    print('------>Ended densifying edges')

    #print(edges)

    if not euler_graph(n, edges):
        print('-->Not an Euler graph')
    else:
        print('-->Euler graph')

    return create_graph_from_edges(n, edges)

def create_edges_all(n):
    edges = []
    for i in range(n-1):
        for j in range(i+1, n):
            edges.append((i, j))

    return edges

def edges_densify(n, edges, density):
    max_num_edges = (n*n - n)/2
    required_num_edges = math.floor(max_num_edges * (density/100))

    while len(edges) > required_num_edges:
        vertices = [random.randint(0, n-1) for i in range(3)]
        vertices.sort()

        if vertices_correct(vertices[0], vertices[1], vertices[2], edges):
            edges.remove((vertices[0], vertices[1]))
            edges.remove((vertices[0], vertices[2]))
            edges.remove((vertices[1], vertices[2]))
            

def create_graph_from_edges(n, edges):
    graph = numpy.zeros((n,n), dtype=int)
    for i in range(len(edges)):
        graph[edges[i][0]][edges[i][1]] = 1
        graph[edges[i][1]][edges[i][0]] = 1
    return graph

def vertices_correct(vertex1, vertex2, vertex3, edges):
    not_equal = vertex1 != vertex2 and vertex2 != vertex3 and vertex1 != vertex3

    vertex1_count = degree_count(vertex1, edges)
    vertex2_count = degree_count(vertex2, edges)
    vertex3_count = degree_count(vertex3, edges)

    vertex1_correct = is_even(vertex1_count) and vertex1_count > 2
    vertex2_correct = is_even(vertex2_count) and vertex2_count > 2
    vertex3_correct = is_even(vertex3_count) and vertex3_count > 2

    not_removed = (vertex1, vertex2) in edges and (vertex2, vertex3) in edges and (vertex1, vertex3) in edges
    return not_equal and not_removed and vertex1_correct and vertex2_correct and vertex3_correct

def degree_count(vertex, edges):
    count = 0
    for item in edges:
        if item[0] == vertex or item[1] == vertex:
            count += 1
    return count

def is_even(num):
    return num % 2 == 0

def euler_graph(n, edges):
    for i in range(n):
        if not is_even(degree_count(i, edges)):
            return False
    return True

def path_toString(path):
    path_string = [str(v) for v in path]

    return " -> ".join(path_string)

    