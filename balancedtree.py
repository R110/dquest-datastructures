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
        return (
            self.preorder_traverse(node.left) +
            [node.value] +
            self.preorder_traverse(node.right)
        )

    def postorder_traverse(self, node):
        if not node:
            return []
        return (
            self.postorder_traverse(node.left) +
            self.postorder_traverse(node.right) +
            [node.value]
        )

    def depth(self, node):
        if not node:
            return 0
        return max(self.depth(node.left), self.depth(node.right)) + 1

    def tree_size(self, node):
        if not node:
            return 0
        return self.tree_size(node.left) + self.tree_size(node.right) + 1

    def num_nodes(self, node):
        return len(self.preorder_traverse(node))

class BinaryTree(BaseBinaryTree):
    def is_balanced(self, node):
        if not node:
            return True

        left_height = self.depth(node.left)
        right_height = self.depth(node.right)

        if (abs(right_height - left_height) <= 1
               and self.is_balanced(node.left)
               and self.is_balanced(node.right)):
            return True
        return False


# Level Order list is provided for you
tree = BinaryTree(level_order)
balanced = tree.is_balanced(tree.root)
print(balanced)
