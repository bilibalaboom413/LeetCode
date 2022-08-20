class Solution(object):
    count = 0

    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        memo = {}
        def dfs(nums, target, index, total):
            if index == len(nums):
                if total == target:
                    return 1
                return 0
            
            key = str(index) + ',' + str(total)
            if key in memo:
                return memo[key]
            result = dfs(nums, target, index + 1, total + nums[index]) + dfs(nums, target, index + 1, total - nums[index])
            memo[key] = result
            return memo[key]

        return dfs(nums, target, 0, 0)
        