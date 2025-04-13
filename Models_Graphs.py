from Edge import Edge
from Node import Node
from Graph import Graph
import random, math

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

# g = grafoErdosRenyi(20,7,directed=False)
# print(g)

def grafoGilbet(n,p,directed=False):
    graph = Graph(directed)
    for i in range(n):
        graph.add_node(Node(i))

    for i in graph.V:
        for j in graph.V:
            if i != j and random.random() <= p:
                graph.add_edge(Edge(i,j))

    # print(f'list:{nodes_list}')

    return graph

# g = grafoGilbet(6,0.5,directed=False)
# print(g)

def grafoGeograficoSimple(n,r,directed=False):
    graph = Graph(directed)
    for i in range(n):
        graph.add_node(Node(i))

    nodes_list = []
    for i in graph.V:
        x = round(random.random(),4)
        y = round(random.random(),4)
        nodes_list.append((i,x,y))

    for i in nodes_list:
        for j in nodes_list:
            if i != j:
                n1, x1, y1 = i
                n2, x2, y2 = j

                distance = math.sqrt((x2 - x1)**2 + (y2-y1)**2) 
                if distance <= r:
                    graph.add_edge(Edge(n1,n2))

    print(f'{nodes_list}')
    return graph

g = grafoGeograficoSimple(500,1,directed=False)
print(g)