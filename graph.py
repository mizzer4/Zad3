class Graph():
    def __init__(self, vertices):
        self.graph = [[0 for column in range(vertices)]
                            for row in range(vertices)]
        self.V = vertices
 
    def isSafe(self, v, pos, path):
        if self.graph[ path[pos-1] ][v] == 0:
            return False
 
        for vertex in path:
            if vertex == v:
                return False
 
        return True
 

    def hamCycleUtil(self, path, pos):
        if pos == self.V:
            if self.graph[ path[pos-1] ][ path[0] ] == 1:
                return True
            else:
                return False
 
        for v in range(1,self.V):
 
            if self.isSafe(v, pos, path) == True:
 
                path[pos] = v
 
                if self.hamCycleUtil(path, pos+1) == True:
                    return True
 
                path[pos] = -1
 
        return False
 
    def hamCycle(self):
        path = [-1] * self.V
 
        path[0] = 0
 
        if self.hamCycleUtil(path,1) == False:
            return None

        path.append(path[0])
        return path
 
    def hamCycleUtil_AllPaths(self, path, pos):
        if pos == self.V:
            if self.graph[ path[pos-1] ][ path[0] ] == 1:
                return True
            else:
                return False
 
        for v in range(1,self.V):
 
            if self.isSafe(v, pos, path) == True:
 
                path[pos] = v
 
                self.hamCycleUtil_AllPaths(path, pos+1)  

                path[pos] = -1

        return
 
    def hamCycle_AllPaths(self):
        path = [-1] * self.V
 
        path[0] = 0
 
        if self.hamCycleUtil_AllPaths(path,1) == False:
            return False

        return True

    def eulerCycle(self):        
        stack = []
        path = []
        cur = 0
    
        while (len(stack) > 0 or sum(self.graph[cur])!= 0):
            
            if (sum(self.graph[cur]) == 0):
                path.append(cur)
                cur = stack[-1]
                del stack[-1]
    
            else:
                for i in range(self.V):
                    if (self.graph[cur][i] == 1):
                        stack.append(cur)
                        self.graph[cur][i] = 0
                        self.graph[i][cur] = 0
                        cur = i
                        break
    
        path.append(cur)
        return path