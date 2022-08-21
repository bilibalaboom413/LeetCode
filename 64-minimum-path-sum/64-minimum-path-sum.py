class Solution:
    memo = [[]]

    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        self.memo = [[-1 for _ in range(n)] for _ in range(m)]

        return self.dp(grid, m - 1, n - 1)

    def dp(self, nums, i, j):
        if i == 0 and j == 0:
            return nums[0][0]   
        
        if i < 0 or j < 0:
            return float('inf')
        
        if self.memo[i][j] != -1:
            return self.memo[i][j]
        
        self.memo[i][j] = min(self.dp(nums, i - 1, j),
                        self.dp(nums, i, j - 1)) + nums[i][j]
        
        return self.memo[i][j]