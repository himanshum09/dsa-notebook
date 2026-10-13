class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Traverse rows
        for row in range(9):
            seen = set()
            for i in range(9):
                if board[row][i] == ".":
                    continue
                if board[row][i] in seen:
                    return False
                seen.add(board[row][i])
        
        for col in range(9):
            seen = set()
            for i in range(9):
                if board[i][col] == ".":
                    continue
                if board[i][col] in seen:
                    return False
                seen.add(board[i][col])
        
        for box in range(9):
            seen = set()
            rowStart = (box // 3) * 3
            colStart = (box % 3) * 3

            for r in range(rowStart, rowStart + 3):
                for c in range(colStart, colStart + 3):
                    if board[r][c] == ".":
                        continue
                    if board[r][c] in seen:
                        return False
                    seen.add(board[r][c])
        return True
