from typing import Optional
from LeetCodeProblems.Trees.BalancedBinaryTree import TreeNode

class Solution:
    def check(self, root: Optional[TreeNode], arr):
        if not root:
            return 
        self.check(root.left, arr)
        arr.append(root.val)
        self.check(root.right, arr)
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        arr = []
        self.check(root, arr)
        for i in range (1, len(arr)):
            if arr[i] <= arr[i - 1]:
                return False
        return True