class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums: return []
        
        res = []
        track = []
        nums.sort()
        used = [False for _ in range(len(nums))]
        
        def backtrack(nums, used, track):
            if len(track) == len(nums):
                res.append(track[:])
                return
            
            for i in range(len(nums)):
                if used[i]: continue
                
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                
                used[i] = True
                track.append(nums[i])
                backtrack(nums, used, track)
                track.pop()
                used[i] = False
        
        backtrack(nums, used, track)
        return res