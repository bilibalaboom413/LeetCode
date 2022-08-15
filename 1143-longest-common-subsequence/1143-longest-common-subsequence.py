class Solution:
    
    memo = [[]]
    
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        
        if not m or not n: return 0
        
        self.memo = [[-1 for _ in range(n)] for _ in range(m)]
        
        return self.dp(text1, 0, text2, 0)
    
    def dp(self, s1, i, s2, j):
        if i == len(s1) or j == len(s2): return 0
        
        if self.memo[i][j] != -1: return self.memo[i][j]
        
        if s1[i] == s2[j]:
            self.memo[i][j] = self.dp(s1, i + 1, s2, j + 1) + 1
        else:
            self.memo[i][j] = max(self.dp(s1, i + 1, s2, j),
                                 self.dp(s1, i, s2, j + 1))
            
        return self.memo[i][j]