# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    res = []
    memo = {}
    
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        self.res = []
        self.memo = {}
        self.traverse(root)
        
        return self.res
    
    def traverse(self, root):
        if not root:
            return '#'
        
        left = self.traverse(root.left)
        right = self.traverse(root.right)
        
        myself = left + ',' + right + ',' + str(root.val)
        
        if myself in self.memo:
            if self.memo[myself] == 1:
                self.res.append(root)
            self.memo[myself] += 1
        else:
            self.memo[myself] = 1
            
        return myself