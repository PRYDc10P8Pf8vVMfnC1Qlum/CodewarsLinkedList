class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def push(head, data):
    if head:
        return Node(data, head)
    else:
        return Node(data)

def build_one_two_three():
    base = None
    base = push(base, 3)
    base = push(base, 2)
    base = push(base, 1)
    return base