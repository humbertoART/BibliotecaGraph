class Node(object):
    def __init__(self,id):
        self.id = id
        self.attr = []

    def __repr__(self):
        return f'Node {self.id}'