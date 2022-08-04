# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums: return None
        
        return self.build(nums, 0, len(nums) - 1)
    
    def build(self, nums, lo, hi):
        if lo > hi or not nums: return None
        
        maxV = -float('inf')
        index = -1
        
        for i in range(lo, hi + 1):
            if nums[i] > maxV:
                maxV = nums[i]
                index = i
        
        root = TreeNode(maxV)
        root.left = self.build(nums, lo, index - 1)
        root.right = self.build(nums, index + 1, hi)
        
        return root