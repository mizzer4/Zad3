def valid_connection(graph, next_ver, curr_ind, path):
    if graph[path[curr_ind - 1]][next_ver] == 0:
        return False

    return not any(vertex == next_ver for vertex in path)


def util_hamilton_cycle(graph, path, curr_ind):
    if curr_ind == len(graph):
        return graph[path[curr_ind - 1]][path[0]] == 1

    for next in range(0, len(graph)):
        if valid_connection(graph, next, curr_ind, path):
            path[curr_ind] = next
            if util_hamilton_cycle(graph, path, curr_ind + 1):
                return True
            path[curr_ind] = -1
    return False


def hamilton_cycle(graph, start_index = 0):
    path = [-1] * (len(graph) + 1)
    path[0] = path[-1] = start_index

    return path if util_hamilton_cycle(graph, path, 1) else []