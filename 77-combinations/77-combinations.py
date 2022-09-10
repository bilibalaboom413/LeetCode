class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        track = []
        
        def backtrack(start, n, k):
            if k == len(track):
                res.append(track[:])
                
            for i in range(start, n + 1):
                track.append(i)
                backtrack(i + 1, n, k)
                track.pop()
                
        backtrack(1, n, k)
        return res