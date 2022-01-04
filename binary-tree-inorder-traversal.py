# Given the root of a binary tree, return the inorder traversal of its nodes' values.

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Algorithm Inorder(tree)
#    1. Traverse the left subtree, i.e., call Inorder(left-subtree)
#    2. Visit the root.
#    3. Traverse the right subtree, i.e., call Inorder(right-subtree)
class Solution:

    def helper(self, root: Optional[TreeNode], response: List[int]):
        if root:
            self.helper(root.left, response)
            response.append(root.val)
            self.helper(root.right, response)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        response = []
        self.helper(root, response)
        return response


tree = TreeNode(1, None, TreeNode(2, TreeNode(3), None))

# tree = TreeNode(1)

print(Solution().inorderTraversal(tree))