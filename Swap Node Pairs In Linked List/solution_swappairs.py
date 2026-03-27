from preloaded import Node

def swap_pairs(head):
    if not head or not head.next:
        return head

    new_s = head.next

    d = Node(0)
    d.next = head
    before = d

    while before.next and before.next.next:
        left = before.next
        right = before.next.next

        left.next = right.next
        right.next = left
        before.next = right

        before = left

    head = new_s
    return head
