class Node:
    def __init__(self, data):
        self.data = data
        self.next: Node | None = None

    def __repr__(self):
        return self.data
    

class LinkedList:
    def __init__(self):
        self.head: Node | None = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)


llist = LinkedList()
print(llist) # None

first_node = Node('a')
llist.head = first_node
print(llist) # a -> None

second_node = Node('B')
third_node = Node('c')

first_node.next = second_node
second_node.next = third_node
print(llist) # a -> B -> c -> None

