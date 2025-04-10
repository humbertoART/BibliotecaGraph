class Graph:
    def __init__(self, directed = False):
        self.id = id(id)
        self.V = {}
        self.E = {}
        self.attr = {}
        self.dirigido = False

    def add_node(self,node):
        # print(f'node.id {node}')
        self.V[node.id] = node
        # print(F'V:',self.V)

    def check_edge(self,id_edge):
        u, v =  id_edge
        return (u,v) in self.E or (v,u) in self.E

    def add_edge(self,edge):
        if self.check_edge(edge.id):
            return False
        self.E[edge.id] = edge
        return True


# newGraph = Graph()
# print('new id',newGraph.id)
# newGraph.add_edge
# print(f'Graph E: {newGraph.E}')
# print(f'Graph V: {newGraph.V}')