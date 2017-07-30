# class BST(BaseBST):
#     def left_rotate(self):
#         if not self.node.right.node:
#             return
#
#         old_node = self.node
#         new_node = self.node.right.node
#         new_right_sub = new_node.left.node
#         self.node = new_node
#         old_node.right.node  = new_right_sub
#         new_node.left.node = old_node
#
# #      3
# # 2---- ----5
# #        4-- --7
# #            6- -8
# #Store references to 3,5,4
# # 5 -> new BST
# # 4 -> new right of 3
# # 3 -> new left of 5
#
#     def right_rotate(self):
#         old_node = self.node
#         new_node = self.node.left.node
#         if not new_node:
#             return
#
#         new_left_sub = new_node.right.node
#         self.node = new_node
#         old_node.left.node = new_left_sub
#         new_node.right.node = old_node
#
#
# bst = BST()
# bst.insert_multiple(bst_values)
# bst.left_rotate()
# left_balanced = bst.is_balanced()
# bst.right_rotate()
# right_balanced = bst.is_balanced()
# -----------
#
# class BS(BaseBST):
#     def insert(self, value=None):
#         node = Node(value=value)
#         if not self.node:
#             self.node = node
#             self.node.left = BST()
#             self.node.right = BST()
#             return
#
#         if value > self.node.value:
#             if self.node.right:
#                 self.node.right.insert(value=value)
#             else:
#                 self.node.right.node = node
#         else:
#             if self.node.left:
#                 self.node.left.insert(value=value)
#             else:
#                 self.node.left.node = node
#
#         difference = self.depth(self.node.left.node) - self.depth(self.node.right.node)
#
#         # Left side case.
#         if difference > 1:
#             # Left-right case.
#             if value > self.node.right.node.value:
#                 self.node.left.left_rotate()
#             # Left-left case.
#             self.right_rotate()
#
#         # Right side case.
#         if difference < -1:
#             # Right-left case.
#             if value <= self.node.left.node.value:
#                 self.node.left.right_rotate()
#             self.left_rotate()
#
#
# bst = BST()
# bst.insert_multiple(bst_values)
# inorder = bst.inorder(bst)
# is_bst_balanced = bst.is_balanced()
#
# ------

class Node:
    def __init__(self, key=None, value=None):
        self.left = None
        self.right = None
        self.key = key
        self.value = value

    def __str__(self):
        return "<node: {}="">".format(self.value)

class BaseBST():
    def __init__(self, index=None):
        self.node = None
        self.index = index
    def left_rotate(self):
        if not self.node.right.node:
            return

        old_node = self.node
        new_node = self.node.right.node
        new_right_sub = new_node.left.node
        self.node = new_node
        old_node.right.node  = new_right_sub
        new_node.left.node = old_node

    def right_rotate(self):
        old_node = self.node
        new_node = self.node.left.node
        if not new_node:
            return

        new_left_sub = new_node.right.node
        self.node = new_node
        old_node.left.node = new_left_sub
        new_node.right.node = old_node
    def depth(self, node):
        if not node:
            return 0
        if not node.left and not node.right:
            return 1

        return max(self.depth(node.left.node), self.depth(node.right.node)) + 1

    def is_balanced(self):
        if not self.node:
            return True

        left_subtree = self.depth(self.node.left.node)
        right_subtree = self.depth(self.node.right.node)

        return abs(left_subtree - right_subtree) < 2

    def inorder(self, tree):
        if not tree or not tree.node:
            return []
        # print(self.inorder(tree.node.left) +
        # [tree.node.value] +
        # self.inorder(tree.node.right))
        return (
            self.inorder(tree.node.left) +
            [tree.node.value] +
            self.inorder(tree.node.right)
        )

    def insert_multiple(self, values):
        for value in values:
            self.insert(value)

    def insert(self, value=None):
        key = value
        if self.index:
            key = value[self.index]
        node = Node(key=key, value=value)

        if not self.node:
            self.node = node
            self.node.left = type(self)(index=self.index)
            self.node.right = self.__class__(index=self.index)
            return
                            # type(self) - self.__class__ - BST()

        if key > self.node.key:
            if self.node.right:
                self.node.right.insert(value=value)
            else:
                self.node.right.node = node
        else:
            if self.node.left:
                self.node.left.insert(value=value)
            else:
                self.node.left.node = node

        difference = self.depth(self.node.left.node) - self.depth(self.node.right.node)

        # Left side case.
        if difference > 1:
            # Left-right case.
            if key > self.node.right.node.key:
                self.node.left.left_rotate()
            # Left-left case.
            self.right_rotate()

        # Right side case.
        if difference < -1:
            # Right-left case.
            if key <= self.node.left.node.key:
                self.node.left.right_rotate()
            self.left_rotate()

    def search(self, key):
        if not self.node:
            return False
        if key == self.node.key:
            return True

        result = False
        if self.node.left:
            result = self.node.left.search(key)
        if self.node.right:
            result = self.node.right.search(key)
        return result

bst_values = [3, 2, 5, 4, 7, 6, 8]
#  change to bst_values = [8, 3, 2, 5, 4, 7, 6]
# File .. in insert_multiple
#     self.insert(value)
#   File .. in insert
#     if self.node.right.node.key and key > self.node.right.node.key:
# AttributeError: 'NoneType' object has no attribute 'key'

bst_list_values = [['hello', 'world', 3], ['goodbye', 'world', 2], ['foo', 'bar', 5],
['fizz', 'buzz', 4], ['lorem', 'ipsum', 7], ['this', 'that', 6],
['enough', 'programming', 8]]
#
bst = BaseBST()
bst.insert_multiple(bst_values)
print(bst.node.value)
inorder = bst.inorder(bst)
print(inorder)

bst_list = BaseBST(index=2)
bst_list.insert_multiple(bst_list_values)
inorder_list = bst_list.inorder(bst_list)
print(bst_list.node.value, '\n', inorder_list)
