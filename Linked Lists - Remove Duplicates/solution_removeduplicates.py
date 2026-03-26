class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    prev = head
    while prev is not None and prev.next is not None:
        if prev.data == prev.next.data:
            prev.next = prev.next.next
        else:
            prev = prev.next
    return head
            