from Node import Node
from Edge import Edge

class Graph:
    def __init__(self, directed = False):
        self.id = id(id)
        self.V = []
        self.E = {}
        self.attr = []
        self.dirigido = directed

    def add_node(self,node):
        # print(f'node.id {node}')
        if node not in self.V:
            self.V.append(node)
        # print(F'V:',self.V)

    def check_edge(self,id_edge):
        u, v =  id_edge
        if self.dirigido:
            return (u,v) in self.E
        return (u,v) in self.E or (v,u) in self.E

    def add_edge(self,edge):
        if self.check_edge(edge.id):
            return False
        self.E[edge.id] = edge
        return True

    # def __str__(self):
    #     str_nodes = ""
    #     node_visited = True
    #     for i in self.V:
    #         if not node_visited:
    #             str_nodes += ", "
    #         str_nodes += str(i)
    #         node_visited = False

    #     str_edges = ""
    #     edge_visited = True
    #     for i in self.E.values():
    #         if not edge_visited:
    #             str_edges += ", "
    #         str_edges += str(i)
    #         edge_visited = False
    #     return f"id: {str(self.id)} \nnodes: {str_nodes} edges: [{str_edges}] \n"

    def __repr__(self):
        return f"id: {str(self.id)} \nnodes: {self.V} edges: [{self.E}] \n"

# newGraph = Graph()
# print('new id',newGraph.id)
# newGraph.add_edge
# print(f'Graph E: {newGraph.E}')
# print(f'Graph V: {newGraph.V}')

# node1 = Node(1)
# node2 = Node(2)
# node3 = Node(3)
# node4 = Node(4)

# edge1 = Edge(node1,node2)
# graph = Graph(directed=True)
# graph.add_node(node1)
# graph.add_node(node2)
# graph.add_node(node3)
# graph.add_node(node4)

# graph.add_edge(edge1)

# print(graph)