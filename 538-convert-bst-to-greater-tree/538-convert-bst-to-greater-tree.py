# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    total = 0
    
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.traverse(root)
        
        return root
    
    def traverse(self, root):
        if not root:
            return
        
        self.traverse(root.right)
        self.total += root.val
        root.val = self.total
        self.traverse(root.left)