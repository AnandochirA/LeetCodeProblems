# Definition for a binary tree node.
from typing import Optional

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def depth(self, root):
        if not root: return 0
        return 1 + max(self.depth(root.left), self.depth(root.right))

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        if abs(self.depth(root.right) - self.depth(root.left)) > 1:
            return False

        return self.isBalanced(root.right) and self.isBalanced(root.left)
