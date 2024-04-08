class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def stringify(node):
    str_ = ''
    if isinstance(node, Node):
        while node.next:
            next = node.next
            inf = node.data
            # print(inf)
            str_ += str(inf) + ' -> '
            node = next
        str_ += str(node.data) + ' -> '
        str_  += 'None'
    else:
        str_ += str(node)
    return str_