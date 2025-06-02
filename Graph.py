from random import randrange
import random
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
        if node not in self.V:
            self.V.append(node)

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
    
    def BFS(self,s):
        bfs = Graph(directed=self.dirigido) #tree
        start_node = None
        discovered = {}
        for i in self.V:
            discovered[i.id] = False

            if i.id == s:
                start_node = i

        if start_node is None:
            raise Exception("Nodo source no existente")
            return None
            
        discovered[start_node.id] = True
        bfs.add_node(start_node)

        counter_layer = 0
        layers = []
        layers.append([start_node])

        while len(layers[counter_layer]) > 0:
            next_layer = []
            for u in layers[counter_layer]:
                for edge in self.E.values(): #todas las aristas
                    if edge.u == u: #si nodo es origen
                        v = edge.v #v es vecino
                    elif not self.dirigido and edge.v == u: #si u es destino de arista
                        v = edge.u #v es vecino
                    else: #uno conectado con arista
                        continue
                    if not discovered[v.id]:
                        discovered[v.id] = True
                        bfs.add_node(v)
                        bfs.add_edge(Edge(u,v))
                        next_layer.append(v)

            layers.append(next_layer)
            counter_layer += 1
        return bfs
    
    def DFS_R(self,s):
        dfs = Graph(directed=self.dirigido) #tree
        start_node = None
        explored = {}

        for i in self.V:
            explored[i.id] = False #todos nno explorados

            if i.id == s:
                start_node = i

        if start_node is None:
            raise Exception("Node source no existente")
        
        self.DFS_RECURSIVE(start_node,explored,dfs)
        return dfs
    
    def DFS_RECURSIVE(self,u,explored,dfs):
        explored[u.id] = True
        dfs.add_node(u)

        for edge in self.E.values():
            if edge.u == u: #si nodo es origen 
                v = edge.v
            elif not self.dirigido and edge.v == u: #si no es dirigido y u es destino
                v = edge.u
            else:
                continue
            if not explored[v.id]:
                dfs.add_edge(Edge(u,v))
                explored[v.id] = True
                self.DFS_RECURSIVE(v,explored,dfs)

    def DFS_I(self,s):
        dfs = Graph(directed=self.dirigido) #tree
        start_node = None
        explored = {}

        for i in self.V:
            explored[i.id] = False #todos no explorados

            if i.id == s:
                start_node = i

        if start_node is None:
            raise Exception("Node source no existente")

        stack = [start_node]

        while stack:
            u = stack.pop()
            if not explored[u.id]:
                explored[u.id] = True
                dfs.add_node(u)   

            for edge in self.E.values():
                if edge.u == u:
                    v = edge.v
                elif not self.dirigido and edge.v == u:
                    v = edge.u
                else:
                    continue
                
                if not explored[v.id]:
                    stack.append(v)
                    dfs.add_edge(Edge(u,v))                 
        return dfs 
    
    def Dijkstra(self,s):
        tree = Graph(directed=self.dirigido)
        start_node = None
        priority_queue = []
        distance = {}
        prev = {}
        S = []
        
        for i in self.V:
            if i.id == s:
                start_node = i

        if start_node is None:
            raise Exception("Node source no existente")
        
        print('start node: ',start_node)

        for edge in self.E.values():
            if not edge.attr:
                edge.attr = [randrange(1,100)]
            edge.weight = edge.attr[0]

        for n in self.V:
            # print(f'n:{n}')
            distance[n] = float("inf")
            prev[n] = None
            
        distance[start_node] = 0
        # print(distance)
        
        priority_queue = [n for n in self.V]

        while priority_queue:
            u = min(priority_queue, key=distance.get)
            # print(f"u:{u}")
            priority_queue.remove(u)
            S.append(u)

            for edge in self.E.values():
                if edge.u == u or (not self.dirigido and edge.v == u):
                    v = edge.v if edge.u == u else edge.u
                    
                    if v not in S:
                        w = edge.weight
                    
                        if distance[v] > distance[u] + w:
                            distance[v] = distance[u] + w
                            prev[v] = u

                            tree.add_node(v)
                            tree.add_node(u)
                            tree.add_edge(Edge(u,v,weight=w,attr=[w]))
        return tree, distance
    
    def KruskalD(self):
        mst = Graph(directed=self.dirigido)

        for edge in self.E.values():
            if not edge.attr:
                edge.attr = [randrange(1,100)]
            edge.weight = edge.attr[0]

        edges_list_sorted = [edge for edge in self.E.values()]
        edges_list_sorted.sort(key=lambda edge: edge.weight)

        component_connected = {n.id: n.id for n in self.V}
        weight_MST = 0

        for edge in edges_list_sorted:
            u, v = edge.u, edge.v

            if component_connected[u.id] != component_connected[v.id]:
                mst.add_node(u)
                mst.add_node(v)
                mst.add_edge(edge)

                weight_MST += edge.weight

                old_component = component_connected[v.id]
                new_component = component_connected[u.id]

                for n in component_connected:
                    if component_connected[n] == old_component:
                        component_connected[n] = new_component

            if len(mst.E) == len(self.V) -  1:
                break

        print(f'Peso MST: {weight_MST}')
        return mst
    
    def KruskalI(self):
        mst = Graph(directed=self.dirigido)

        for node in self.V:
            mst.add_node(node)

        for edge in self.E.values():
            if not edge.attr:
                edge.attr = [randrange(1,100)]
            edge.weight = edge.attr[0]
            mst.add_edge(edge)

        edges_list_sorted = [edge for edge in self.E.values()]
        edges_list_sorted.sort(key=lambda edge: edge.weight, reverse=True)

        for edge in edges_list_sorted:
            u, v = edge.u, edge.v

            if (u.id, v.id) in mst.E:
                key = (u.id, v.id)
            elif not self.dirigido and (v.id, u.id) in mst.E:
                key = (v.id, u.id)
            else:
                continue #edge not found

            edge_removed = mst.E[key]
            del mst.E[key]

            if len((mst.BFS(u.id)).V) != len(mst.V): #desconectado?
                mst.E[key] = edge_removed

            if len(mst.E) == len(mst.V) - 1:
                break
        return mst
    
    def Prim(self):
        mst = Graph(directed=self.dirigido)
        distance = {}
        parent_node = {} #desde que nodo se llegó

        for n in self.V:
            distance[n] = float("inf")
            parent_node[n] = None

        # random_start = self.V[0]
        random_start = random.choice(self.V)
        distance[random_start] = 0

        Q = [n for n in self.V]

        while Q:
            node_less = min(Q, key=lambda node: distance[node])
            Q.remove(node_less)
            mst.add_node(node_less)

            if parent_node[node_less] is not None: #no está vacío
                pn = parent_node[node_less]
                key = (pn.id, node_less.id)
                if key not in self.E: #sentido contrario
                    key = (node_less.id, pn.id)
                mst.add_edge(self.E[key])

            for neighbor in Q:
                key = (node_less.id, neighbor.id)
                key_other = (neighbor.id, node_less.id)

                if key in self.E or key_other in self.E:
                    if key in self.E:
                        new_key = key
                    else:
                        new_key = key_other
                    edge = self.E[new_key]

                    if edge.weight < distance[neighbor]:
                        distance[neighbor] = edge.weight
                        parent_node[neighbor] = node_less
        return mst

    def graphiViz(self,file, distance=None):
        with open(file,'w') as file:
            if self.dirigido:
                file.write("digraph G {\n")
            else:
                file.write("graph G {\n")

            for i in self.V:
                if distance and i in distance:
                    # label = f"{i.id} "
                    file.write(f'  {i.id} [label="{i.id} ({round(distance[i],2)})"];\n')
                else:
                    file.write(f"  {i.id};\n")

            for i in self.E.values():
                u, v = i.id
                weight = i.weight
                if self.dirigido:
                    connector = "->"
                else:
                    connector = "--"
                file.write(f'   {u} {connector} {v} [label="{weight}"];\n')
            
            file.write("}\n")

    def __repr__(self):
        return f"id: {str(self.id)} \nnodes: {self.V} edges: [{self.E}] \n"
    