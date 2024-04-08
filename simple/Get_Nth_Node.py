class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def get_nth(node, index):
    k = 0
    if index <0:
        raise TypeError
    while True:
        if k != index:
            node = node.next
            k+=1
        else:
            return Node(node.data)
