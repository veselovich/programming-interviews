# Definition for a binary tree node.
class TreeNode:
    def __init__(self, data=None, left=None, right=None, size=0):
        self.data = data
        self.left = left
        self.right = right
        self.size = size

    def __repr__(self) -> str:
        return f"Node {self.data}"


root_tree = TreeNode(1, size=7)
root_tree.left = TreeNode(2, size=3)
root_tree.right = TreeNode(3, size=3)
root_tree.left.left = TreeNode(4, size=1)
root_tree.left.right = TreeNode(5, size=1)
root_tree.right.left = TreeNode(6, size=1)
root_tree.right.right = TreeNode(7, size=1)