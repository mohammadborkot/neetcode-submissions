class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rows
        for r in range(0, len(board)):
            seen_rows = set()
            for c in range(0, len(board[r])):
                if board[r][c] == '.':
                    continue
                elif board[r][c] in seen_rows:
                    return False
                else:
                    seen_rows.add(board[r][c])

        # check rows
        for c in range(0, len(board[0])):
            seen_cols = set()
            for r in range(0, len(board)):
                if board[r][c] == '.':
                    continue
                elif board[r][c] in seen_cols:
                    return False
                else:
                    seen_cols.add(board[r][c])
        squares = {}
        # check squares
        for r in range(0, len(board)):
            for c in range(0, len(board[r])):
                i = (r//3) * 3 + (c//3) # which square it belongs to
                if board[r][c] == '.':
                    continue

                elif i not in squares:
                    squares[i] = set() 

                elif board[r][c] in squares[i]:
                    return False
                
                squares[i].add(board[r][c])

        return True