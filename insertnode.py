    # Implement your `insert` method here.
level_order = [1, 2, 3, 4, 5, 6]#, 7, 8, 9, 10]

class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return "<Node: {}>".format(self.value)

class BinaryTree:
    def __init__(self, values=None):
        self.root = None
        if values:
            self.insert(values)

    def insert(self, values, index=0, leftright=''):
        node = None
        if index < len(values):
            node = Node(value=values[index])
            print(leftright, node)
            if not self.root:
                self.root = node
            node.left = self.insert(values, index=index*2+1, leftright='L')
            node.right = self.insert(values, index=index*2+2, leftright='R')
            print("left node of", node, "--", node.left)
            print("right node of", node, "--", node.right)
        return node


tree = BinaryTree(level_order)
root = tree.root.value
# child = tree.root.left.right.left.value

# insert(values, index=1) -->
# returns values[1], calls insert() 2x for L and R nodes
#
# Left Side-- insert(values, index=index*2+1)
#
#                                                         None- insert(values, index=7-> out of range)
#                             insert(values, index=3)---
# insert(values, index=1) ---                             None
#                                                         None
#                             insert(values, index=4)---
#                                                         None
