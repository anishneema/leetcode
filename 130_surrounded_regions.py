class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        safe_coor = set()

        # seed border coordinates
        for i in range(n):
            safe_coor.add((0, i))
            safe_coor.add((m - 1, i))
        for i in range(m):
            safe_coor.add((i, 0))
            safe_coor.add((i, n - 1))

        def dfs(i, j):
            directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
            for r, c in directions:
                nr, nc = i + r, j + c
                if 0 <= nr < m and 0 <= nc < n:
                    if board[nr][nc] == "O" and (nr, nc) not in safe_coor:
                        safe_coor.add((nr, nc))
                        dfs(nr, nc)

        # only kick off dfs from border cells that are actually 'O'
        for (i, j) in list(safe_coor):
            if board[i][j] == "O":
                dfs(i, j)

        # flip any 'O' not reachable from the border
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O" and (i, j) not in safe_coor:
                    board[i][j] = "X"