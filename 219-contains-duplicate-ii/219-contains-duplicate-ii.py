class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        left, right = 0, 0
        
        window = set()
        
        while right < len(nums):
            if nums[right] in window:
                return True
            
            window.add(nums[right])
            right += 1
            
            while right - left > k:
                window.remove(nums[left])
                left += 1
            
        return False
        