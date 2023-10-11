# define tree
class Node:
    def __init__(self, data) -> None:
        self.left = None
        self.right = None
        self.data = data

# the aforementioned code represents an epty node with an ability to store data 
# and link to the adjacent left and right other nodes which are at the beginning equals to None
# Learning from https://www.youtube.com/watch?v=TezryjBe3Ts&list=PLMz1vLpcJgGDeVDybqQeZ0EewZcRF_1m_ video tutorial

# define insert method
    def insert(self, data):
        if self.data is None:
            self.data = data
        else:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)

# function printing tree in order
def in_order_print(r):
    if r is None:
        return
    else:
        in_order_print(r.left)
        print(r.data, end=' ')
        in_order_print(r.right)

# fucntion printing tree in PRE order
def pre_order_print(r):
    if r is None:
        return
    else:
        print(r.data, end=' ')
        pre_order_print(r.left)
        pre_order_print(r.right)

# fucntion printing tree in POST order
def post_order_print(r):
    if r is None:
        return
    else:
        print(r.data, end=' ')
        post_order_print(r.right)
        post_order_print(r.left)

#building a tree
if __name__ == "__main__":
    root = Node('g')
    root.insert('c')
    root.insert('b')
    root.insert('a')
    root.insert('e')
    root.insert('d')
    root.insert('f')
    root.insert('i')
    root.insert('h')
    root.insert('j')
    root.insert('k')
    root.insert('m')
    root.insert('l')

# printing all Nodes in order
# in_order_print(root)
# print()
#printting all Nodes in PRE order
# pre_order_print(root)
# print()
#printing all Nodes in POST order
# post_order_print(root)