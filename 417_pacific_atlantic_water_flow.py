class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        cells_pacific = [[False] * len(heights[0]) for _ in range(len(heights))]
        cells_atlantic =[[False] * len(heights[0]) for _ in range(len(heights))]

        pacific_coor = [(0, c) for c in range(len(heights[0]))] + [(r, 0) for r in range(len(heights))]
        m, n = len(heights), len(heights[0])
        atlantic_coor = [(m - 1, c) for c in range(n)] + [(r, n - 1) for r in range(m)]

        def dfs(i, j, visited):

            visited[i][j] = True

            directions = [(-1,0), (1,0), (0,1), (0,-1)]

            for r, c in directions:

                nx = i + r
                ny = j + c

                if 0<=nx<len(heights) and 0<=ny<len(heights[0]) and not visited[nx][ny]:

                    if heights[nx][ny] >= heights[i][j]:
                        
                        dfs(nx, ny, visited)


        for i, j in pacific_coor:

            dfs(i, j, cells_pacific)
        
        for i,j in atlantic_coor:

            dfs(i, j, cells_atlantic)
        
        ans = []

        for i in range(len(heights)):

            for j in range(len(heights[0])):

                if cells_pacific[i][j] and cells_atlantic[i][j]:
                    ans.append([i,j])
        

        return ans