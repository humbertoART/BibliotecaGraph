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

        print(f'discovered: {discovered}')
        return bfs,layers
    
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
                explored[v.id] = True
                dfs.add_edge(Edge(u,v))
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

    def graphiViz(self,file):
        with open(file,'w') as file:
            if self.dirigido:
                file.write("digraph G {\n")
            else:
                file.write("graph G {\n")

            for i in self.V:
                file.write(f"  {i.id};\n")

            for i in self.E.values():
                u, v = i.id
                if self.dirigido:
                    connector = "->"
                else:
                    connector = "--"
                file.write(f"   {u} {connector} {v};\n")
            
            file.write("}\n")

    def __repr__(self):
        return f"id: {str(self.id)} \nnodes: {self.V} edges: [{self.E}] \n"
    

