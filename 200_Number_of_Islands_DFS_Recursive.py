class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid:
            return 0
        
        island = 0
        isvisited = set()
        
        rows = len(grid)
        cols = len(grid[0])
        
        def dfs(r, c):
            if (r not in range(rows) or c not in range(cols)
                or grid[r][c] != "1" or ((r,c) in isvisited)):
                return
            isvisited.add((r,c))            
            dfs(r,c-1)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r+1,c)
                        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in isvisited:
                    dfs(r, c)
                    island +=1
        
        return island
