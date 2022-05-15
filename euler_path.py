from copy import deepcopy 

def find_Euler(graph, n):
    local_graph = deepcopy(graph)
    stack = []
    path = []
    cur = 0
  
    while (len(stack) > 0 or sum(local_graph[cur])!= 0):
          
        if (sum(local_graph[cur]) == 0):
            path.append(cur)
            cur = stack[-1]
            del stack[-1]
  
        else:
            for i in range(n):
                if (local_graph[cur][i] == 1):
                    stack.append(cur)
                    local_graph[cur][i] = 0
                    local_graph[i][cur] = 0
                    cur = i
                    break
  
    path.append(cur)
    return path


