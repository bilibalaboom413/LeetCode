class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        left, right = 0, 0
        count = 0
        window = 1
        
        while right < len(nums):
            window *= nums[right]
            right += 1
            
            while window >= k and left < right:
                window /= nums[left]
                left += 1
            
            count += right - left
            
        return count