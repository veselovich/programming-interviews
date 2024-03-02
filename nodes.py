class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def __repr__(self) -> str:
        return f"Node {self.value}"

class BinaryTree:
    def __init__(self, root_value):
        self.root = TreeNode(root_value)

    def insert_left(self, parent_value, child_value):
        parent = self.find(parent_value, self.root)
        if parent is None:
            print(f"Parent node with value {parent_value} not found.")
            return
        if parent.left is None:
            parent.left = TreeNode(child_value)
            parent.left.parent = parent
        else:
            print(f"Parent node {parent_value} already has a left child.")

    def insert_right(self, parent_value, child_value):
        parent = self.find(parent_value, self.root)
        if parent is None:
            print(f"Parent node with value {parent_value} not found.")
            return
        if parent.right is None:
            parent.right = TreeNode(child_value)
            parent.right.parent = parent
        else:
            print(f"Parent node {parent_value} already has a right child.")

    def find(self, value, node):
        if node is None:
            return None
        if node.value == value:
            return node
        left_result = self.find(value, node.left)
        if left_result is not None:
            return left_result
        right_result = self.find(value, node.right)
        return right_result

# Example usage
tree = BinaryTree('A')
tree.insert_left('A', 'B')
tree.insert_right('A', 'C')
tree.insert_left('B', 'D')
tree.insert_right('B', 'E')
tree.insert_left('C', 'F')
tree.insert_right('C', 'G')

# This tree now represents the structure:
#          A
#        /   \
#       B     C
#      / \   / \
#     D   E F   G