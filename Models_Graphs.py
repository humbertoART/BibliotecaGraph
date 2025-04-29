from Edge import Edge
from Node import Node
from Graph import Graph
import random, math

def grafoMalla(m,n,directed=False):
    """
        Genera grafo de malla
        :param m: número de columnas (> 1)
        :param n: número de filas (> 1)
        :param dirigido: el grafo es dirigido?
        :return: grafo generado
    """
    if m < 2 or n < 2:
        raise Exception("El número debe ser mayor a 1")
    
    product = m * n
    graph = Graph(directed)

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
    """
    Genera grafo aleatorio con el modelo Erdos-Renyi
    :param n: número de nodos (> 0)
    :param m: número de aristas (>= n-1)
    :param dirigido: el grafo es dirigido?
    :return: grafo generado
    """   
    if n < 1:
        raise Exception("El valor de n debe ser mayor a 0")
    
    if m < n - 1:
        raise Exception("El valor de m debe ser mayor o igual a n-1")

    graph = Graph(directed)
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
            graph.add_edge(Edge(i[0],i[1]))
    return graph

def grafoGilbet(n,p,directed=False):
    """
    Genera grafo aleatorio con el modelo Gilbert
    :param n: número de nodos (> 0)
    :param p: probabilidad de crear una arista (0, 1)
    :param dirigido: el grafo es dirigido?
    :return: grafo generado
    """  
    if n < 1:
        raise Exception("El valor de n debe ser mayor a 0")
    
    if p < 0 or p > 1:
        raise Exception("El valor de p debe estar entre [0,1]")

    graph = Graph(directed)
    for i in range(n):
        graph.add_node(Node(i))

    for i in graph.V:
        for j in graph.V:
            if i != j and random.random() <= p:
                graph.add_edge(Edge(i,j))
    return graph

def grafoGeograficoSimple(n,r,directed=False):
    """
    Genera grafo aleatorio con el modelo geográfico simple
    :param n: número de nodos (> 0)
    :param r: distancia máxima para crear un nodo (0, 1)
    :param dirigido: el grafo es dirigido?
    :return: grafo generado
    """  

    if n < 1:
        raise Exception("El valor de n debe ser mayor a 0")
    if r < 0 or r > 1:
        raise Exception("El valor de r debe estar entre [0,1]")

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
    """
    Genera grafo aleatorio con el modelo Barabasi-Albert
    :param n: número de nodos (> 0)
    :param d: grado máximo esperado por cada nodo (> 1)
    :param dirigido: el grafo es dirigido?
    :return: grafo generado
    """   

    if n < 1:
        raise Exception("El valor de n debe ser mayor a 0")
    if d < 2:
        raise Exception("El valor de d debe ser mayor a 1")

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
                        for k in range(len(nodes_list)):
                            if nodes_list[k][0] == n1:
                                nodes_list[k] = (nodes_list[k][0], nodes_list[k][1]+1)
                            if nodes_list[k][0] == n2:
                                nodes_list[k] = (nodes_list[k][0], nodes_list[k][1]+1)
    return  graph

def grafoDorogovtsevMendes(n,directed=False):
    """
    Genera grafo aleatorio con el modelo Barabasi-Albert
    :param n: número de nodos (≥ 3)
    :param dirigido: el grafo es dirigido?
    :return: grafo generado
    """

    if n < 3:
        raise Exception("El valor de n debe ser mayor o igual que 3")

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


g = grafoMalla(12,2,directed=False)
print(f'GRAPH***\n')
print(f'bfs tree: {g}')
# print(g)
bfs_tree, layers = g.BFS(0)
print(f'BFS***\n')
print(f'bfs tree: {bfs_tree}')