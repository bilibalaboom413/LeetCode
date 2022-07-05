#
# @lc app=leetcode id=1438 lang=python3
#
# [1438] Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
#

# @lc code=start
import collections


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        mx, mn = collections.deque([0]), collections.deque([0])
        ans = 1
        left = 0
        for i in range(1, len(nums)):
            # max monotonic queue
            while mx and nums[mx[-1]] < nums[i]:
                mx.pop()
            mx.append(i)
            # min monotonic queue
            while mn and nums[mn[-1]] > nums[i]:
                mn.pop()
            mn.append(i)
            # shorten window
            while mx and mn and nums[mx[0]] - nums[mn[0]] > limit:
                left += 1
                # invalid index
                if mx[0] < left:
                    mx.popleft()
                # invalid index
                if mn[0] < left:
                    mn.popleft()
            # length of nums
            ans = max(ans, i - left + 1)

        return ans
        # @lc code=end
