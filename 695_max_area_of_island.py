class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        candidate = 0
        
        def dfs(i, j):

            nonlocal candidate

            grid[i][j] = '#'
            candidate += 1

            directions = [(-1,0), (1,0), (0,1), (0, -1)]

            for dr, dc in directions:

                nr = i + dr
                nc = j + dc

                if  0<= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 1:
                    dfs(nr, nc)

                
        ans = 0
        for i in range(len(grid)):

            for j in range(len(grid[0])):

                if grid[i][j] == 1:
                    dfs(i,j)
                    ans = max(ans, candidate)
                    candidate = 0
        
        return ans