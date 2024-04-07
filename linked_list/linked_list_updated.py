from typing import Any


class Node:
    def __init__(self, data: Any):
        self.data = data
        self.next: Node | None = None

    def __repr__(self):
        return self.data


class LinkedList:
    def __init__(self, nodes: Any | None = None):
        self.head: Node | None = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for element in nodes:
                node.next = Node(data=element)
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)
    
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def add_first(self, node: Node):
        node.next = self.head
        self.head = node

    def add_last(self, node: Node):
        if self.head is None:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node

    def add_after(self, target_node_data: Any, new_node: Node):
        if self.head is None:
            raise Exception("List is empty.")
        
        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return
        
        raise Exception("Node with data '%s' not found." % target_node_data)
    
    def add_before(self, target_node_data: Any, new_node: Node):
        if self.head is None:
            raise Exception("List is empty.")
        
        if self.head.data == target_node_data:
            return self.add_first(node=new_node)
        
        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node

        raise Exception("Node with data '%s' not found." % target_node_data)
    
    def remove_node(self, target_node_data: Any):
        if self.head is None:
            raise Exception("List is empty.")
        
        if self.head.data == target_node_data:
            self.head = self.head.next
            return
        
        previous_node = self.head
        for node in self:
            if node.data == target_node_data:
                previous_node.next = node.next
                return
            previous_node = node

        raise Exception("Node with data '%s' not found." % target_node_data)
    
    def get(self, index: int):
        if self.head is None:
            raise Exception("List is empty.")
        
        counter = 0
        if index == 0 and self.head is not None:
            return self.head
        
        if index > 0 and self.head is not None:
            current_node = self.head
            for node in self:
                if counter == index:
                    res = current_node
                    return res
                counter += 1
                current_node = node.next

        if index < 0 or index != counter or current_node is None:
            raise Exception("Provided index '%s' not in linked list." % index)
        
    def reverse(self):

        _temp_list = []

        if self.head is not None:
            for node in self:
                if node.next is not None:
                    _temp_list.append(node.data)
                else:
                    _temp_list.append(node.data)
                    break

            res = reversed(_temp_list)
            result = LinkedList(list(res))
            self.head = result.head
            return


        raise Exception("List is empty.")
    
    def pop_last(self):
        if self.head is None:
            raise Exception("List is empty.")
        
        prev_node = self.head
        if self.head is not None:
            for node in self:
                if node.next is not None:
                    prev_node = node
                else:
                    prev_node.next = None
                    return node
                
    def pop_first(self):
        if self.head is None:
            raise Exception("List is empty.")
        
        if self.head is not None:
            first_node = self.head
            self.head = self.head.next
            return first_node
        

class Queue(LinkedList):
    def dequeue(self):
        return super().pop_first()
    
    def enqueue(self, node: Node):
        return super().add_last(node=node)



queue = Queue(['a', 'b', 'c'])

print(queue) # a -> b -> c -> None

print(queue.dequeue()) # a
print(queue) # b -> c -> None

queue.enqueue(Node('z'))
print(queue) # b -> c -> z -> None






# llist = LinkedList(["a", "b", "c", "d", "e"])
# print(llist) # a -> b -> c -> d -> e -> None

# for node in llist:
#     print(node)
# # a
# # b
# # c
# # d
# # e
        
# llist = LinkedList()
# print(llist) # None

# llist.add_first(Node('b'))
# print(llist) # b -> None

# llist.add_first(Node('a'))
# print(llist) # a -> b -> None
        
# llist = LinkedList(["a", "b", "c", "d"])
# print(llist) # a -> b -> c -> d -> None

# llist.add_last(Node("e"))
# print(llist) # a -> b -> c -> d -> e -> None

# llist.add_last(Node("f"))
# print(llist) # a -> b -> c -> d -> e -> f -> None

# llist = LinkedList()
# try:
#     llist.add_after("a", Node("b"))
# except Exception as e:
#     print(e) # List is empty.

# llist = LinkedList(["a", "b", "c", "d"])
# print(llist) # a -> b -> c -> d -> None

# llist.add_after("c", Node("cc"))
# print(llist) # a -> b -> c -> cc -> d -> None

# try:
#     llist.add_after("f", Node("g"))
# except Exception as e:
#     print(e) # Node with data f not found.
    
# llist = LinkedList()
# try:
#     llist.add_before("a", Node("a"))
# except Exception as e:
#     print(e) # List is empty.

# llist = LinkedList(["b", "c"])
# print(llist) # b -> c -> None

# llist.add_before("b", Node("a"))
# print(llist) # a -> b -> c -> None

# llist.add_before("b", Node("aa"))
# llist.add_before("c", Node("bb"))
# print(llist) # a -> aa -> b -> bb -> c -> None

# try:
#     llist.add_before("n", Node("m"))
# except Exception as e:
#     print(e) # Node with data 'n' not found.
    
# llist = LinkedList()
# try:
#     llist.remove_node("a")
# except Exception as e:
#     print(e) # List is empty.

# llist = LinkedList(["a", "b", "c", "d", "e"])
# print(llist) # a -> b -> c -> d -> e -> None

# llist.remove_node("a")
# print(llist) # b -> c -> d -> e -> None

# llist.remove_node("e")
# print(llist) # b -> c -> d -> None

# llist.remove_node("c")
# print(llist) # b -> d -> None

# try:
#     llist.remove_node("a")
# except Exception as e:
#     print(e) # Node with data 'a' not found.
        
# llist = LinkedList()
# try:
#     llist.get(4)
# except Exception as e:
#     print(e) # List is empty.
    
# llist = LinkedList(["a", "b", "c", "d", "e"])
# print(llist) # a -> b -> c -> d -> e -> None

# print(llist.get(2)) # c
# print(llist.get(3)) # d
# print(llist.get(4)) # e

# try:
#     print(llist.get(5))
# except Exception as e:
#     print(e) # Provided index '5' not in linked list.
    

# llist = LinkedList()
# try:
#     llist.reverse()
# except Exception as e:
#     print(e) # List is empty.

# llist = LinkedList(["a", "b", "c", "d", "e"])
# print(llist) # a -> b -> c -> d -> e -> None

# llist.reverse()
# print(llist) # e -> d -> c -> b -> a -> None


# llist = LinkedList()
# try:
#     llist.pop_last()
# except Exception as e:
#     print(e) # List is empty.

# llist = LinkedList(["a", "b", "c", "d", "e"])
# print(llist) # a -> b -> c -> d -> e -> None

# print(llist.pop_last()) # e
# print(llist) # a -> b -> c -> d -> None


# llist = LinkedList()
# try:
#     llist.pop_first()
# except Exception as e:
#     print(e) # List is empty.

# llist = LinkedList(["a", "b", "c", "d", "e"])
# print(llist) # a -> b -> c -> d -> e -> None

# print(llist.pop_first()) # a
# print(llist) # b -> c -> d -> e -> None
