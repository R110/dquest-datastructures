class Node:
    def __init__(self, keys=None, children=None):
        self.keys = keys or []
        self.children = children or []

    def is_leaf(self):
        return len(self.children) == 0

    def __repr__(self):
        # Helpful method to keep track of Node keys.
        return "<Node: {}>".format(self.keys)

class BTree():
    def __init__(self, t):
        self.t = t
        self.root = None

    def insert(self, key):
        self.insert_non_full(self.root, key)

    def insert_non_full(self, node, key):
        if node.is_leaf():
            index = 0
            for k in node.keys:
                if key > k: index += 1
                else: break
            node.keys.insert(index, key)
            return

        index = 0
        for k in node.keys:
            if key > k: index += 1
            else: break

        if len(node.children[index].keys) == 2*self.t - 1:
            left_node, right_node, new_key = self.split(node.children[index])
            node.keys.insert(index, new_key)
            node.children[index] = left_node
            node.children.insert(index+1, right_node)
            if key > new_key:
                index += 1

        self.insert_non_full(node.children[index], key)

    def split(self, node):
        left_node = Node(
            keys=node.keys[:len(node.keys)//2],
            children=node.children[:len(node.children)//2+1]
        )
        right_node = Node(
            keys=node.keys[len(node.keys)//2:],
            children=node.children[len(node.children)//2:]
        )
        key = right_node.keys.pop(0)
        return left_node, right_node, key


# We have initialized a sample BTree for you.
btree = BTree(4)
b_node = Node(keys=[8, 18])
b_node.children.append(Node(keys=[-3, -2, -1, 2, 3, 5, 7]))
b_node.children.append(Node(keys=[9, 10, 11, 12, 14, 18, ]))
b_node.children.append(Node(keys=[17, 20, 44]))
btree.root = b_node
btree.insert(1)
# - root node not leaf- 1<8 so index 0
# - split at 2 and because 1 !>2 per line 40 insert in first child node's key lst at recursive call 
# after 2 has bubbled up to root node

btree.insert(4)
btree.insert(6)
btree.insert(13)
btree.insert(17)
btree.insert(22)
print(btree.root.keys)
for i in range(5):
    print(btree.root.children[i].keys)

# l=[]
# lst = [l.append(child_keys + str(n) for n in range(3)]
# print(lst)
