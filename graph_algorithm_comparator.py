import euler_path, hamilton_path
import graph_generator

def main():
    n = 11
    density = 30

    graph = graph_generator.graph_generator(n, density)
    #graph_generator.graph_toString(graph)

    path = euler_path.find_Euler(graph, n)
    print(graph_generator.path_toString(path))

    path = hamilton_path.hamilton_cycle(graph)
    print(graph_generator.path_toString(path))

if __name__=="__main__":
    main()
