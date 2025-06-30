class Graph:
    def __init__(self):
        self.graph = {}
    def add_edge(self, u , v):
        if u not in self.graph:
            self.graph[u]=[]
        self.graph[u].append(v)
    def display(self):
        for node in self.graph:
            print(node,"->",self.graph[node])
g = Graph()
g.add_edge('A','B')
g.add_edge('B','C')
g.add_edge('C','D')
g.add_edge('D','E')
g.display()