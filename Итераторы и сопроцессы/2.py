class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinTree:
    def __init__(self, root_value):
        self.root = TreeNode(root_value)

    def add(self, value):
        self._add_recursive(self.root, value)

    def _add_recursive(self, current_node, value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = TreeNode(value)
            else:
                self._add_recursive(current_node.left, value)
        else:
            if current_node.right is None:
                current_node.right = TreeNode(value)
            else:
                self._add_recursive(current_node.right, value)

    def __iter__(self):
        return self._depth_first_traversal()

    def _depth_first_traversal(self):
        if self.root is not None:
            stack = [self.root]
            while stack:
                node = stack.pop()
                yield node.value
                if node.right is not None:
                    stack.append(node.right)
                if node.left is not None:
                    stack.append(node.left)

tree = BinTree(5)
tree.add(3)
tree.add(8)
tree.add(1)
tree.add(4)
tree.add(7)
tree.add(9)

for value in tree:
    print(value)