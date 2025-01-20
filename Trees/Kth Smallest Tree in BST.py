# Definition for a binary tree node.
from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorder(self, root: Optional[TreeNode], ans: List[int]):
        if not root:
            return
        self.inorder(root.left, ans)
        ans.append(root.val)
        self.inorder(root.right, ans)
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = []
        self.inorder(root, ans)
        return ans[k - 1]