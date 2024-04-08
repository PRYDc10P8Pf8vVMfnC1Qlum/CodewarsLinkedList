class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def sorted_insert(head, data):
    node = head
    lst = []
    if not head:
        return Node(data)
    while True:
        lst.append(node.data)
        if node.data < data:
            try:
                if node.next.data >data:
                    lst.append(data)
                    next_ = node.next
                    result  = 0
                    for i in range(len(lst)-1, -1, -1):
                        if result:
                            result = Node(lst[i], result)
                        else:
                            result = Node(lst[i], next_)
                    return result
            except AttributeError:
                lst.append(data)
                next_ = node.next
                result  = 0
                for i in range(len(lst)-1, -1, -1):
                    if result:
                        result = Node(lst[i], result)
                    else:
                        result = Node(lst[i], next_)
                return result
            
        elif node.data > data:
            return Node(data,Node(node.data, node.next))
        node = node.next