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