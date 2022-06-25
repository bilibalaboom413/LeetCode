class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        nums = sorted(map(lambda x : x * x, nums))
        return nums