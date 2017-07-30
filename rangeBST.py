from baseBST import *
class BST(BaseBST):
    def greater_than(self, key):
        if not self.node:
            return []

        values = []
        if self.node.left:
            values += self.node.left.greater_than(key)
        if self.node.right:
            values += self.node.right.greater_than(key)
        if self.node.key > key:
            values.append(self.node.value)
        return values

bst = BST()
bst.insert_multiple(bst_values)
greater = bst.greater_than(5)
print(bst.node.value, greater) # 5 [6,7,8]

# bst_list = BST(index=2)
# bst_list.insert_multiple(bst_list_values)
# greater_list = bst_list.greater_than(5)

# bst = BST()
# with open('amounts.csv', 'r') as f:
#     reader = csv.reader(f)
#     next(reader)
#     amount_rows = list((r[0], float(r[1])) for r in reader)
#
# bst = BST(index=1)
# bst.insert_multiple(amount_rows)
# csv_query = bst.greater_than(10)
