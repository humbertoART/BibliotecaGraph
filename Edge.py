# from Node import Node
class Edge:
    def __init__(self,u,v):
        self.u = u
        self.v = v 
        self.attr = []
        self.id = (u.id, v.id)

    def __repr__(self):
        return f'u: {self.u} v: {self.v}'
    

# new_edge = Edge(Node(23),Node(33))
# print(new_edge)