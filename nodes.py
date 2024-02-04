# Definition for a binary tree node.
class TreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"Node {self.data}"


root_tree = TreeNode(1)
root_tree.left = TreeNode(0)
root_tree.right = TreeNode(1)
root_tree.left.left = TreeNode(0)
root_tree.left.right = TreeNode(1)
root_tree.right.left = TreeNode(0)
root_tree.right.right = TreeNode(1)
