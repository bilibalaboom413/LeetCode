class Solution(object):
    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        
        n, total = len(nums), sum(nums)
        left, right = 0, 0
        target = total - x
        windowSum = 0
        maxLen = -float('inf')
        
        while right < n:
            windowSum += nums[right]
            right += 1
            
            while windowSum > target and left < right:
                windowSum -= nums[left]
                left += 1
            
            if windowSum == target:
                maxLen = max(maxLen, right - left)
        
        return -1 if maxLen == -float('inf') else n - maxLen