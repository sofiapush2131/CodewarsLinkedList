from preloaded import Node

def linked_list_from_string(list_repr: str) -> Node | None:
    new_list_repr = list_repr.split(" -> ")
    node = None

    new_list_repr = new_list_repr[:-1]

    for i in reversed(new_list_repr):

        node = Node(int(i), node)
    return node
