class Solution:
    res = []
    
    def generateParenthesis(self, n: int) -> List[str]:
        if not n: return []
        track = ''
        self.res = []
        self.backtrack(n, n, track, self.res)
        return self.res
    
    def backtrack(self, left, right, track, res):
        if right < left: return
        
        if left < 0 or right < 0:
            return 
        
        if left == 0 and right == 0:
            self.res.append(track)
            return
        
        track += '('
        self.backtrack(left - 1, right, track, self.res)
        track = track[:-1]
        
        track += ')'
        self.backtrack(left, right - 1, track, self.res)
        track = track[:-1]