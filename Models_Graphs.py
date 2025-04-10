from Edge import Edge
from Node import Node
from Graph import Graph

def grafoMalla(m,n,directed=False):
    if m < 1 or n < 1:
        return grafoMalla(m,n,directed=False)
    
    total_nodes = m * n
    graph = Graph()
    # graph.V

    for i in range(total_nodes):
        graph.add_node(Node(i))

    

    return graph

g = grafoMalla(20,20,directed=False)