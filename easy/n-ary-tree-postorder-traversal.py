# Given the root of an n-ary tree, return the postorder traversal of its nodes' values.

from typing import List

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def helper(self, root: Node, res: List[int]): 
        if root.children:
            for node in root.children:
                self.helper(node, res)

        res.append(root.val)

    def postorder(self, root: Node) -> List[int]:
        if root is None:
            return []
        res = []
        self.helper(root, res)
        return res


# root = Node(1, [Node(2), Node(3, [Node(6), Node(7, [Node(11, [Node(14)])])]), Node(4, [Node(8, [Node(12)])]), Node(5, [Node(9, [Node(13)]), Node(10)])])
# root = Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)])
# root = Node(1, [Node(3), Node(2), Node(4)])

root = None

print(Solution().postorder(root))