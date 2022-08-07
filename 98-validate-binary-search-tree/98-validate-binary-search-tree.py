# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.traverse(root, None, None)        
    
    def traverse(self, root, lo, hi):
        if not root: return True
        
        if lo and root.val <= lo.val:
            return False
        
        if hi and root.val >= hi.val:
            return False
        
        return self.traverse(root.left, lo, root) and self.traverse(root.right, root, hi)
        
        
        