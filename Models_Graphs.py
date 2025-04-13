from Edge import Edge
from Node import Node
from Graph import Graph
import random

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

# g = grafoMalla(4,4,directed=False)
# print(g)

def grafoErdosRenyi(n,m,directed=False):
    graph = Graph(directed=directed)
    for i in range(n):
        graph.add_node(Node(i))

    nodes_list = []
    for i in graph.V:
        nodes_list.append(i)

    random_list = []

    if not directed:
        max_pairs = (n* (n-1)) // 2 #(conexiones alcanzables // duplicados)
    else:
        max_pairs = n * (n-1)

    if m > max_pairs:
        return 

    while len(random_list) < m:
        pair = random.sample(nodes_list,k=2)
        if pair not in random_list and pair[::-1] not in random_list:
            random_list.append(pair)

        for i in random_list:
            print(f'i:[{i[0]}][{i[1]}]')
            graph.add_edge(Edge(i[0],i[1]))


    print(f'list:{nodes_list}')
    print(f'random: {random_list}')
    return graph

g = grafoErdosRenyi(20,7,directed=False)
print(g)