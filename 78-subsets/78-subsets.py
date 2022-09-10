class Solution:
    res = []
        
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        track = []
        self.backtrack(nums, 0, track)
        return self.res
    
    def backtrack(self, nums, start, track):
        self.res.append(track[:])
        
        for i in range(start, len(nums)):
            track.append(nums[i])
            self.backtrack(nums, i + 1, track)
            track.pop()
            