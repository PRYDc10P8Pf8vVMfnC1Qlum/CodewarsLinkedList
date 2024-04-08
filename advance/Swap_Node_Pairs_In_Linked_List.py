class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def swap_pairs(head):
    lst = []
    while head.next:
        lst.append(head.data)
        head = head.next
    lst.append(head.data)

    result = 0
    length = len(lst)
    for i in range(0, length-1, 2):
        if i == length-1:
            break
        first = lst[i]
        sec = lst[i+1]
        lst[i] = sec
        lst[i+1] = first
    lst= lst[::-1]
    for i in range(length):
        if result:
            result = Node(lst[i], result)
        else:
            result = Node(lst[i])
    return result