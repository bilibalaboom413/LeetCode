#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    maxDiameter = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxDepth(root)
        return self.maxDiameter

    def maxDepth(self, root):
        if not root:
            return 0

        leftMax = self.maxDepth(root.left)
        rightMax = self.maxDepth(root.right)
        myDiameter = leftMax + rightMax
        self.maxDiameter = max(myDiameter, self.maxDiameter)

        return 1 + max(leftMax, rightMax)
        # @lc code=end
