class Edge:
    def __init__(self,u,v):
        self.u = u
        self.v = v 
        self.attr = []
        self.id = (u.id, v.id)

    def __repr__(self):
        return f'u: {self.u} v: {self.v}'