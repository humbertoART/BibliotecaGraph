from Edge import Edge
from Node import Node
from Graph import Graph
import random, math

def grafoMalla(m,n,directed=False):
    product = m * n
    graph = Graph(directed=True)

    for i in range(product):
        graph.add_node(Node(i))

    for i in range(m):
        for j in range(n):
            current_position = (i * n) + j
            if i+1 < m: #dentro de los límites
                down_position = (i+1)*n +j
                graph.add_edge(Edge(graph.V[current_position],graph.V[down_position]))
            if j+1 < n:
                right_position = i * n + (j + 1)
                graph.add_edge(Edge(graph.V[current_position],graph.V[right_position]))
    return graph

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
            # print(f'i:[{i[0]}][{i[1]}]')
            graph.add_edge(Edge(i[0],i[1]))
    return graph

def grafoGilbet(n,p,directed=False):
    graph = Graph(directed)
    for i in range(n):
        graph.add_node(Node(i))

    for i in graph.V:
        for j in graph.V:
            if i != j and random.random() <= p:
                graph.add_edge(Edge(i,j))
    return graph

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
                #elección de dos tuplas distintas que no se hayan seleccionado previamente
                n1, x1, y1 = i #tupla 1
                n2, x2, y2 = j #tupla 2

                distance = math.sqrt((x2 - x1)**2 + (y2-y1)**2) 
                if distance <= r:
                    graph.add_edge(Edge(n1,n2))
    return graph

def grafoBarabasiAlbert(n,d,directed=False):
    graph = Graph(directed)
    nodes_list = []

    for i in range(n):
        graph.add_node(Node(i))

    for i in graph.V:
        nodes_list.append((i,0))

    if len(nodes_list) > 1:
        graph.add_edge(Edge(nodes_list[0][0],nodes_list[1][0]))
        nodes_list[0] = (nodes_list[0][0],nodes_list[0][1]+1)
        nodes_list[1] = (nodes_list[1][0],nodes_list[1][1]+1)

    for i in nodes_list:
        for j in nodes_list:
            if i != j:
                n1,d1 = i #tupla 1
                n2,d2 = j #tupla 2
                total_degree = 0
                for n, degree in nodes_list:
                    total_degree += degree
                if total_degree > 0:
                    p = d/total_degree
                else:
                    p = 0
                
                if random.random() < p and d1 < d:
                    if graph.add_edge(Edge(n1,n2)):
                        # print(f'{n1}--->{n2}')
                        for k in range(len(nodes_list)):
                            if nodes_list[k][0] == n1:
                                nodes_list[k] = (nodes_list[k][0], nodes_list[k][1]+1)
                            if nodes_list[k][0] == n2:
                                nodes_list[k] = (nodes_list[k][0], nodes_list[k][1]+1)
    return  graph

def grafoDorogovtsevMendes(n,directed=False):
    graph = Graph(directed)
    for i in range(3):
        graph.add_node(Node(i))

    graph.add_edge(Edge(graph.V[0],graph.V[1]))
    graph.add_edge(Edge(graph.V[1],graph.V[2]))
    graph.add_edge(Edge(graph.V[2],graph.V[0]))

    for i in range(3,n):
        graph.add_node(Node(i))
        edge_random = random.choice(list(graph.E))

        current_node = graph.V[i]
        u, v = edge_random
        graph.add_edge(Edge(current_node,Node(u)))
        graph.add_edge(Edge(current_node,Node(v)))

    return graph