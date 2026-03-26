from preloaded import Node

'''
Node is defined in preloaded like this:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

def push(head, data):
    # Your code goes here.
    new_node = Node(data)
    new_node.next = head
    return new_node

def build_one_two_three():
    node = None
    node = push(node, 3)
    node = push(node, 2)
    node = push(node, 1)
    return node
    