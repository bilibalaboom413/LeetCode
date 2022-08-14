class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        
        if not n:
            return 0
        
        dp = [-1 for _ in range(n)]
        dp[0] = nums[0]
        
        for i in range(1, n):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
            
        return max(dp)