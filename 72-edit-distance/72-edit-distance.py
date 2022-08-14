class Solution:
    
    memo = [[]]
    
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        
        self.memo = [[-1 for _ in range(n)] for _ in range(m)]
        
        return self.dp(word1, m - 1, word2, n - 1)
    
    def dp(self, s1, i, s2, j):
        if i == -1: return j + 1
        if j == -1: return i + 1
        
        if self.memo[i][j] != -1: return self.memo[i][j]
        
        if s1[i] == s2[j]: return self.dp(s1, i - 1, s2, j - 1)
        
        self.memo[i][j] = min(self.dp(s1, i - 1, s2, j) + 1,
                        self.dp(s1, i, s2, j - 1) + 1,
                        self.dp(s1, i - 1, s2, j - 1) + 1)
        
        return self.memo[i][j] 