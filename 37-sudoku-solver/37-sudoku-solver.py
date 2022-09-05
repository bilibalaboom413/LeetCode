class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        self.backtrack(board, 0, 0)
    
    def backtrack(self, board, i, j):
        m, n = 9, 9
        
        if i == m:
            return True
        
        if j == n:
            return self.backtrack(board, i + 1, 0)
        
        if board[i][j] != '.':
            return self.backtrack(board, i, j + 1)
        
        for ch in '123456789':
            if not self.isValid(board, i, j, ch):
                continue
            board[i][j] = ch
            if self.backtrack(board, i, j + 1): return True
            board[i][j] = '.'
                
    def isValid(self, board, r, c, n):
        for i in range(9):
            if board[r][i] == n: return False
            if board[i][c] == n: return False
            if board[(r // 3) * 3 + i // 3][(c // 3) * 3 + i % 3] == n:
                return False

        return True 