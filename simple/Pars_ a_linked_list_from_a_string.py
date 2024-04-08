class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def linked_list_from_string(s):
    s = s.replace(' -> ', ',')
    length = s.split(',')
    result  = 0
    for i in range(len(length)-1, -1, -1):
        prelast = length[i-1]
        if prelast == 'None':
            break
        else:
            prelast = int(length[i-1])
        if result:
            result = Node(prelast, result)
        else:
            result = Node(prelast)
    return result