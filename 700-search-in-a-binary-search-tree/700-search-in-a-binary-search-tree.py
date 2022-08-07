# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        return self.traverse(root, val)
    
    def traverse(self, root, target):
        if not root:
            return None
        
        if root.val == target:
            return root
        
        if root.val > target:
            return self.traverse(root.left, target)
        
        if root.val < target:
            return self.traverse(root.right, target)