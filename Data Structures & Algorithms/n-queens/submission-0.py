class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."] * n for i in range(n)]
        def isPossible(board, r, c):
            #same column
            for i in range(r):
                if board[i][c] == 'Q':
                    return False

            #same right diagonal
            row = r -1 
            col = c -1
            while row >=0 and col >= 0:
                if board[row][col] == 'Q':
                    return False
                row -= 1
                col -= 1

            #same left diagonal
            row = r -1 
            col = c +1
            while row >=0 and col < n:
                if board[row][col] == 'Q':
                    return False
                row -= 1
                col += 1
            
            return True

        def dfs(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            for c in range(n):
                #check if possible
                if isPossible(board, r, c): 
                    board[r][c] = 'Q'
                    dfs(r + 1) #go forward
                    board[r][c] = '.'
            
        dfs(0)
        return res
        