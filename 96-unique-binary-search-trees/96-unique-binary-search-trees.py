class Solution:
    
    memo = []
    
    def numTrees(self, n: int) -> int:
        self.memo = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        
        return self.count(1, n)
    
    def count(self, lo, hi):
        if lo > hi:
            return 1
        
        if self.memo[lo][hi]:
            return self.memo[lo][hi]
        
        res = 0
        for i in range(lo, hi + 1):
            left = self.count(lo, i - 1)
            right = self.count(i + 1, hi)
            res += left * right
            
        self.memo[lo][hi] = res
        
        return res