# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if not n: return []
        
        return self.build(1, n)
    
    def build(self, lo, hi):
        res = []
        
        if lo > hi:
            res.append(None)
            return res
        
        for i in range(lo, hi + 1):
            leftTree = self.build(lo, i - 1)
            rightTree = self.build(i + 1, hi)
            
            for left in leftTree:
                for right in rightTree:
                    root = TreeNode(i)
                    root.left = left
                    root.right = right
                    res.append(root)
                    
        return res
        