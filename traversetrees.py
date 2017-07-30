level_order = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return "<Node: {}>".format(self.value)

class BaseBinaryTree:
    def __init__(self, values=None):
        self.root = None
        if values:
            self.insert(values)

    def insert(self, values, index=0, leftright=''):
        node = None
        if index < len(values):
            node = Node(value=values[index])
            # print(leftright, node)
            if not self.root:
                self.root = node
            node.left = self.insert(values, index=index*2+1, leftright='L')
            node.right = self.insert(values, index=index*2+2, leftright='R')
            # print("left node of", node, "--", node.left)
            # print("right node of", node, "--", node.right)
        return node


class BinaryTree(BaseBinaryTree):
    def preorder_traverse(self, node):
        if not node:
            return []
        return (
            [node.value] +
            self.preorder_traverse(node.left) +
            self.preorder_traverse(node.right)
        )

    def inorder_traverse(self, node):
        if not node:
            return []
        #print(node.value) 2x
        return (
            self.inorder_traverse(node.left) +
            [node.value] +
            self.inorder_traverse(node.right)
        )

    def postorder_traverse(self, node):
        if not node:
            return []
        return (
            self.postorder_traverse(node.left) +
            self.postorder_traverse(node.right) +
            [node.value]
        )




# #[1, 2, 4, 8, 9, 5, 10, 3, 6, 7]
# Initial(1) preorder -> (2) + 1 + (3)
# To dictate --> 4 (node), 8, 9 --> base case returns empty list
# 2 -> 2 + (4) + (5)
# 4 -> 4 + (8) + (9)
# 8 -> 8 + [] + []...
#
# #[8, 9, 4, 10, 5, 2, 6, 7, 3, 1]
# Initial(1) postorder -> (2) + (3) + 1
# ---(Left)--
# 2 -> (4) + (5) + 2
# 4 -> (8) + (9) + 4
# 8 -> [] + [] + 8
# 9 -> [] + [] + 9
#
# --> [8,9,4,]
#
# (2 -> (4) + (5) + 2) execute (5)
# 5 -> (10) + [] + 5
# 10 -> [] + [] + 10
#
# -->[8,9,4,10,5,]
#
# --Right---
# 3 -> (6) + (7) + 3
# 6 -> [] + [] + 6
# 7 -> [] + [] + 7
#
# -->[8, 9, 4, 10, 5, 2, 6, 7, 3, 1]


tree = BinaryTree(level_order)
preorder = tree.preorder_traverse(tree.root)
inorder = tree.inorder_traverse(tree.root)
postorder = tree.postorder_traverse(tree.root)
print(preorder,'\n', inorder, '\n', postorder)
