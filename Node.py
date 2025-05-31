class Node(object):
    def __init__(self,id):
        self.id = id
        self.attr = []

    def __repr__(self):
        return f'Node {self.id}'
    
    def __eq__(self, value):
        return isinstance(value, Node) and self.id == value.id
    

    def __hash__(self):
        return hash(self.id)