class Graph():

    def __init__(self):
        self.representation ={}
  
    def add_nodes(self, nodes):
        for node in nodes:
            self.representation[node] = {}
     
    def add_edge(self, tail, head, weight = None):
        self.representation[tail][head] = weight

    def remove_edge(self, tail, head):
        self.representation[tail][head] =  None

    def create_residual_graph(self, path):
        path_flow = float('Inf')
        for i in range(len(path)-1):
            u, v = path[i], path[i+1]
            path_flow = min(self.representation[u][v], path_flow)
        return path_flow
    
    def update_residual_graph(self, path, flow):
        for i in range(len(path)-1):
            u, v = path[i], path[i+1]
            self.representation[u][v] -= flow
            if u not in self.representation[v]:
                self.representation[v][u] = 0
            self.representation[v][u] += flow

    def __repr__(self):
        return str(self.representation)