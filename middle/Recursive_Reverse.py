class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest

def move_node(source, dest):
    dest_1 = source.data
    source = source.next
    dest = Node(dest_1, dest)
    return Context(source, dest)