class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        track = []
        
        def backtrack(nums, track):
            if len(track) == len(nums):
                res.append(track[:])
                
            for i in range(len(nums)):
                if nums[i] in track:
                    continue
                
                track.append(nums[i])
                backtrack(nums, track)
                track.pop()
        
        backtrack(nums, track)
        return res