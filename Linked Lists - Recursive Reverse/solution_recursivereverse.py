class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse(head):
    previous = None
    curr = head

    while curr is not None:
        next_n = curr.next
        curr.next = previous
        previous = curr
        curr = next_n


    return previous
