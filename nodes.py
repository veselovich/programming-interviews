class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

    def __repr__(self) -> str:
        return f"Node {self.data}"

class BinaryTree:
    def __init__(self, root_data):
        self.root = TreeNode(root_data)

    def insert_left(self, parent_data, child_data):
        parent = self.find(parent_data, self.root)
        if parent is None:
            print(f"Parent node with data {parent_data} not found.")
            return
        if parent.left is None:
            parent.left = TreeNode(child_data)
            parent.left.parent = parent
        else:
            print(f"Parent node {parent_data} already has a left child.")

    def insert_right(self, parent_data, child_data):
        parent = self.find(parent_data, self.root)
        if parent is None:
            print(f"Parent node with data {parent_data} not found.")
            return
        if parent.right is None:
            parent.right = TreeNode(child_data)
            parent.right.parent = parent
        else:
            print(f"Parent node {parent_data} already has a right child.")

    def find(self, data, node):
        if node is None:
            return None
        if node.data == data:
            return node
        left_result = self.find(data, node.left)
        if left_result is not None:
            return left_result
        right_result = self.find(data, node.right)
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