class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9
        valid = True

        rows = [set() for _ in range(n)]
        cols = [set() for _ in range(n)]
        boxes = [set() for _ in range(n)]

        #Lines
        for i in range(n):
            for j in range(n):
                num = board[i][j]
                if num == '.':
                    continue

                if num not in rows[i]:
                    rows[i].add(num)
                else:
                    valid = False
        
                if board[i][j] not in cols[j]:
                    cols[j].add(num)
                else:
                    valid = False

                box = (i // 3) * 3 + (j // 3)
                if board[i][j] not in boxes[box]:
                    boxes[box].add(num)
                else:
                    valid = False
        return valid

            
