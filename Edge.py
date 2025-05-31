class Edge:
    def __init__(self,u,v, weight=1, attr=None):
        self.u = u
        self.v = v 
        self.weight = weight
        self.attr = attr if attr is not None else [weight]
        self.id = (u.id, v.id)

    def __repr__(self):
        return f'u: {self.u} v: {self.v}'