class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        rows = len(board)
        cols = len(board[0])
        
        
        def markborders(r, c):
            if (r < 0 or r == rows or
            c < 0 or c == cols or board[r][c] != "O"):
                return
            
            board[r][c] = "T"
            
            markborders(r, c +1)
            markborders(r, c -1)
            markborders(r+1, c)
            markborders(r-1, c)
        
        for r in range(rows):
            for c in range(cols):
                if ((r in [0, rows -1] or c in [0, cols - 1]) and
                    board[r][c] == "O"):
                        markborders(r,c)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"
