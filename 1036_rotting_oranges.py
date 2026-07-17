class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        count = 0
        queue = deque()
        
        for i in range(len(grid)):

            for j in range(len(grid[0])):

                if grid[i][j] == 1:
                    count+=1
                if grid[i][j] == 2:
                    queue.append((i,j,0))
                
        
        directions = [(-1,0), (1,0), (0, -1), (0, 1)]

        if count == 0:
            return 0
    
        while queue:

            r, c, level = queue.popleft()

            for x, y in directions:

                nx = r + x
                ny = y + c

                if 0<=nx<len(grid) and 0<=ny<len(grid[0]):

                    if grid[nx][ny] == 1:
                        count -= 1
                        grid[nx][ny] = 2
                        queue.append((nx,ny, level+1))
                    
                    if count == 0:

                        return level + 1
        

        return -1