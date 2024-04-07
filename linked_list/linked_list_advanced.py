from typing import Any


class Node:
    def __init__(self, data: Any):
        self.data = data
        self.next: Node | None = None
        self.previous: Node | None = None

    def __repr__(self):
        return self.data


class LinkedList:
    def __init__(self, nodes: Any | None = None):
        self.head: Node | None = None
        self.tail: Node | None = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for element in nodes:
                node.next = Node(data=element)
                node = node.next
                if node.next == None:
                    self.tail = node

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        res = " <-> ".join(nodes)
        return "head-> " + res + " <- tail"
    
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def check_if_empty_list(self):
        if self.head is None:
            raise Exception("List is empty.")

    def add_first(self, node: Node):
        node.next = self.head
        self.head.previous = node
        self.head = node

    def add_last(self, node: Node):
        if self.head is None:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node
        node.previous = current_node
        self.tail = node

    def add_after(self, target_node_data: Any, new_node: Node):
        self.check_if_empty_list()
        
        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                new_node.previous = node
                node.next = new_node
                return
            if new_node.next is None:
                self.tail = new_node
        
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

    #     raise Exception("Node with data '%s' not found." % target_node_data)
    
    # def remove_node(self, target_node_data: Any):
    #     if self.head is None:
    #         raise Exception("List is empty.")
        
    #     if self.head.data == target_node_data:
    #         self.head = self.head.next
    #         return
        
    #     previous_node = self.head
    #     for node in self:
    #         if node.data == target_node_data:
    #             previous_node.next = node.next
    #             return
    #         previous_node = node

    #     raise Exception("Node with data '%s' not found." % target_node_data)
    
    # def get(self, index: int):
    #     if self.head is None:
    #         raise Exception("List is empty.")
        
    #     counter = 0
    #     if index == 0 and self.head is not None:
    #         return self.head
        
    #     if index > 0 and self.head is not None:
    #         current_node = self.head
    #         for node in self:
    #             if counter == index:
    #                 res = current_node
    #                 return res
    #             counter += 1
    #             current_node = node.next

    #     if index < 0 or index != counter or current_node is None:
    #         raise Exception("Provided index '%s' not in linked list." % index)
        
    # def reverse(self):

    #     _temp_list = []

    #     if self.head is not None:
    #         for node in self:
    #             if node.next is not None:
    #                 _temp_list.append(node.data)
    #             else:
    #                 _temp_list.append(node.data)
    #                 break

    #         res = reversed(_temp_list)
    #         result = LinkedList(list(res))
    #         self.head = result.head
    #         return


    #     raise Exception("List is empty.")
    
    # def pop_last(self):
    #     if self.head is None:
    #         raise Exception("List is empty.")
        
    #     prev_node = self.head
    #     if self.head is not None:
    #         for node in self:
    #             if node.next is not None:
    #                 prev_node = node
    #             else:
    #                 prev_node.next = None
    #                 return node
                
    # def pop_first(self):
    #     if self.head is None:
    #         raise Exception("List is empty.")
        
    #     if self.head is not None:
    #         first_node = self.head
    #         self.head = self.head.next
    #         return first_node
        

# class Queue(LinkedList):
#     def dequeue(self):
#         return super().pop_first()
    
#     def enqueue(self, node: Node):
#         return super().add_last(node=node)
            
llist = LinkedList(['a', 'b', 'c', 'd'])
print(llist) # head-> a <-> b <-> c <-> d <- tail
print(llist.head) # a
print(llist.tail) # d

llist.add_first(Node('z'))
print(llist.head) # z
print(llist) # head-> z <-> a <-> b <-> c <-> d <- tail

llist.add_last(Node('e'))
print(llist.tail) # e
print(llist) # head-> z <-> a <-> b <-> c <-> d <-> e <- tail

