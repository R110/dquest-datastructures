insert(values, index=1)
returns values[1], calls insert 2x  for L and R nodes

Left Side-- insert(values, index=index*2+1)

                                                        None- insert(values, index=7-> out of range)
                            insert(values, index=3)---
insert(values, index=1) ---                             None
                                                        None
                            insert(values, index=4)---
                                                        None

class BinaryTree(BaseBinaryTree):
    def is_parent(self, node):
        return bool(node.left or node.right)

    def is_interior(self, node):
        return (not node == self.root) and self.is_parent(node)

    def is_leaf(self, node):
        return (not node == self.root) and not self.is_parent(node)
