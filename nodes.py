# Definition for a binary tree node.
class TreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"Node {self.data}"


root_tree = TreeNode(1)
root_tree.left = TreeNode(2)
root_tree.right = TreeNode(2)
root_tree.left.left = TreeNode(4)
root_tree.left.right = TreeNode(5)
root_tree.right.left = TreeNode(5)
root_tree.right.right = TreeNode(4)
