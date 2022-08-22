class Solution:
    memo = [[]]
    
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m = len(dungeon)
        n = len(dungeon[0])
        
        self.memo = [[-1 for _ in range(n)] for _ in range(m)]
        
        return self.dp(dungeon, 0, 0)
    
    def dp(self, grid, i, j):
        m = len(grid)
        n = len(grid[0])
        
        if i == m - 1 and j == n - 1:
            return 1 if grid[i][j] >= 0 else -grid[i][j] + 1
        
        if i == m or j == n:
            return float('inf')
        
        if self.memo[i][j] != -1:
            return self.memo[i][j]
        
        res = min(self.dp(grid, i, j + 1),
                 self.dp(grid, i + 1, j)) - grid[i][j]
        
        self.memo[i][j] = 1 if res <= 0 else res
        
        return self.memo[i][j]