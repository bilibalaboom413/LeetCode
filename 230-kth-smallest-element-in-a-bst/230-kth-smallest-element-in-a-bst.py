# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    res = 0
    rank = 0
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.traverse(root, k)
        return self.res
    
    def traverse(self, root, k):
        if not root:
            return
        
        self.traverse(root.left, k)
        self.rank += 1
        
        if self.rank == k:
            self.res = root.val
            return self.res
        
        self.traverse(root.right, k)