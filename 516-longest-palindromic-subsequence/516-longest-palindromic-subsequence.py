class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        if not n: return 0
        
        dp = [[0 for _ in range(n)] for _ in range(n)]
        memo = [[-1 for _ in range(n)] for _ in range(n)]
        
        for i in range(n):
            dp[i][i] = 1
            memo[i][i] = 1
            
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if memo[i][j] != -1: return memo[i][j]
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])
                
                memo[i][j] = dp[i][j]
                
        return dp[0][n - 1]