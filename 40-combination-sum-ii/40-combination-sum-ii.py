class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates: return []
        
        res = []
        track = []
        candidates.sort()
        trackSum = 0
        
        def backtrack(start, nums, target, trackSum):
            if trackSum == target:
                res.append(track[:])
                
            if trackSum > target: return
                
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                
                track.append(nums[i])
                trackSum += nums[i]
                backtrack(i + 1, nums, target, trackSum)
                trackSum -= nums[i]
                track.pop()
        
        backtrack(0, candidates, target, trackSum)
        return res
            