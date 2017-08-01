from insert3btree import *

class BSTree(BTree):
    def search(self, node, term):
        if not self.root:
            return False
        index = 0
        for key in node.keys:
            if key == term:
                return True
            if term > key:
                index += 1
        if node.is_leaf():
            return False

        return self.search(node.children[index], term)

btree_keys = range(100)
btree = BSTree(5)
btree.insert_multiple(btree_keys)
print(btree.root.keys)
print(btree.root.children[2].keys)
search_6 = btree.search(btree.root, 6)
search_73 = btree.search(btree.root, 73)
search_101 = btree.search(btree.root, 101)
print(search_101)
