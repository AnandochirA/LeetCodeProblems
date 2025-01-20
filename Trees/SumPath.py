# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def helper(self, root: Optional[TreeNode], currentSum: int, target: int) -> bool:
        if not root:
            return False
        currentSum += root.val
        if not root.left and not root.right:
            return currentSum == target
        return (self.helper(root.left, currentSum, target) or self.helper(root.right, currentSum, target))
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        ans = self.helper(root, 0, targetSum)
        return ans