import random

class Solution:
    
    preSum = []
    
    
    def __init__(self, w: List[int]):
        n = len(w)
        self.preSum = [0 for _ in range(n + 1)]
        self.preSum[0] = 0
        for i in range(1, n + 1):
            self.preSum[i] = self.preSum[i - 1] + w[i - 1]
        
    def pickIndex(self) -> int:
        n = len(self.preSum)
        target = random.randint(1, self.preSum[n - 1])
        return self.left_bound(target, self.preSum) - 1

    def left_bound(self, target, nums):
        if not len(nums): return -1
        left = 0
        right = len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                right = mid;
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid
        
        return left;
    
# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()