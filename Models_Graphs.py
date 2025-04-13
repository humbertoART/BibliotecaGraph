from Edge import Edge
from Node import Node
from Graph import Graph

def grafoMalla(m,n,directed=False):
    if m < 1 or n < 1:
        return grafoMalla(m,n,directed=False)
    
    product = m * n
    graph = Graph(directed=True)
    # graph.V

    for i in range(product):
        graph.add_node(Node(i))

    for i in range(m):
        for j in range(n):
            print(f'[{i}][{j}]')
            current_position = (i * n) + j
            print(f'current: {current_position}')
            if i+1 < m: #dentro de los límites
                down_position = (i+1)*n +j
                graph.add_edge(Edge(graph.V[current_position],graph.V[down_position]))
            #     graph.add_edge(Edge(graph.V[current],graph.V[]))
            if j+1 < n:
                right_position = i * n + (j + 1)
                graph.add_edge(Edge(graph.V[current_position],graph.V[right_position]))
    return graph

g = grafoMalla(4,4,directed=False)
print(g)