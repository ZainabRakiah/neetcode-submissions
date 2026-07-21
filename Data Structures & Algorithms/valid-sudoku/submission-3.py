class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[] for _ in range(9)]
        cols = [[] for _ in range(9)]
        squares = [[] for _ in range(9)]
        for i in range(0,9):
            for j in range(0,9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in rows[i]:
                    return False
                else:
                    rows[i].append(board[i][j])
                if board[i][j] in cols[j]:
                    return False
                else:
                    cols[j].append(board[i][j])
                index_box = (i//3)*3+(j//3)
                if board[i][j] in squares[index_box]:
                    return False
                else:
                    squares[index_box].append(board[i][j])
        return True
