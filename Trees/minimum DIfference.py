class Solution:
    def inorder(self, root, prev, min_diff):
        if not root:
            return prev, min_diff
        prev, min_diff = self.inorder(root.left, prev, min_diff)
        
        if prev is not None:
            min_diff = min(min_diff, root.val - prev)
        prev = root.val

        return self.inorder(root.right, prev, min_diff)
    
    def getMinimumDifference(self, root):
        _, min_diff = self.inorder(root, None, float('inf'))
        return min_diff
