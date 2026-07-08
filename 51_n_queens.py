class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        board = [["."] * n for _ in range(n)]
        ans = []
        
        def backtrack(col, row_set, diag_set, anti_diag):

            if col == n:
                ans.append(["".join(r) for r in board])
                return

            for row in range(n):

                difference = (row - col)
                anti_difference = row + col

                if difference not in diag_set and row not in row_set and anti_difference not in anti_diag:
                    board[row][col] = "Q"
                    row_set.add(row)
                    diag_set.add(difference)
                    anti_diag.add(anti_difference)
                    backtrack(col+1, row_set, diag_set, anti_diag)
                    board[row][col] = "."
                    row_set.remove(row)
                    diag_set.remove(difference)
                    anti_diag.remove(anti_difference)
        

        

        backtrack(0, set(), set(), set())
        

        return ans