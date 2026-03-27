class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head):
    if not head or not head.next:
        raise ValueError

    first_head = head
    second_head = head.next
    curr_f = first_head
    curr_s = second_head

    while curr_s and curr_s.next:
        curr_f.next = curr_s.next
        curr_f = curr_f.next
        curr_s.next = curr_f.next
        curr_s = curr_s.next

    curr_f.next = None

    return Context(first_head, second_head)
