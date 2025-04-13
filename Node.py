class Node(object):
    def __init__(self,id):
        self.id = id
        self.attr = []
        # print(id)

    def __repr__(self):
        return f'Node {self.id}'


new_Node = Node(45)
# print(f'New Node {new_Node.id}')