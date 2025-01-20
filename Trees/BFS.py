from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: 
            return []
        
        queue = [root]
        result = []

        while len(queue) > 0:
            level = []
            for _ in range(len(queue)): 
                element = queue.pop(0)
                level.append(element.val)
                if element.left:
                    queue.append(element.left)
                if element.right: 
                    queue.append(element.right)
            result.append(level)
        return result
