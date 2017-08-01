
def brute_search():
    with open('amounts.csv') as f:
        reader = csv.reader(f)
        rows = []
        for row in reader:
            if reader.line_num in [4, 41231, 284400]:
                rows.append(row)
        return rows

def cache_search():
    return list(csv.reader(linecache.getline('amounts.csv', i) for i in [4, 41231, 284400]))

print(timeit.timeit('brute_search()', 'from __main__ import brute_search', number=50))
print(timeit.timeit('cache_search()', 'from __main__ import cache_search', number=50))
brute = brute_search()
cache = cache_search()

class Node:
    def __init__(self, keys=None, children=None):
        self.keys = keys or []
        self.children = children or []

    def is_leaf(self):
        return len(self.children) == 0

    def __repr__(self):
        # Helpful method to keep track of Node keys.
        return "<Node: {}>".format(self.keys)

class BTree:
    def __init__(self, t):
        self.t = t
        self.root = None

b_node = Node(keys=[1, 4, 8])
node_is_leaf = b_node.is_leaf()
btree = BTree(3)
btree.root = b_node
keys = btree.root.keys
