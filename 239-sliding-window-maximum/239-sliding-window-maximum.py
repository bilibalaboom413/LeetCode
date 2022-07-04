class Solution:
    maxq = []
    
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        self.maxq = []
        res = []
        
        for i in range(len(nums)):
            if i < k - 1:
                self.push(nums[i])
            else:
                self.push(nums[i])
                res.append(self.maxV())
                self.popV(nums[i - k + 1])
                
        return res
    
    def push(self, n):
        while self.maxq and self.maxq[-1] < n:
            self.maxq.pop()
        self.maxq.append(n)
    
    def maxV(self):
        return self.maxq[0]
    
    def popV(self, n):
        if n == self.maxq[0]:
            self.maxq.pop(0)

        