class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def remove_duplicates(head):
    lst = []
    if not head:
        return None
    while head.next:
        if head.data not in lst:
            lst.append(head.data)
        head = head.next
    if head.data not in lst:
        lst.append(head.data)
    length = len(lst)
    lst = lst[::-1]
    result = 0
    for i in range(length):
        if result:
            result = Node(lst[i], result)
        else:
            result = Node(lst[i])
    return result