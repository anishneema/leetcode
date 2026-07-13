class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(i, j):

            grid[i][j] = '#'

            directions = [(-1,0), (1,0), (0,-1), (0, 1)]

            for dc, dr in directions:

                nr = dr + j
                nc = dc + i

                if 0<= nc < len(grid) and 0<= nr < len(grid[0]) and grid[nc][nr] == "1":

                    dfs(nc, nr)
        
        ans = 0
        
        for i in range(len(grid)):

            for j in range(len(grid[0])):

                if grid[i][j] == "1":

                    ans +=1 
                    dfs(i,j)
        
        return ans