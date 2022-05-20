class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        if not grid or not grid[0]:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        
        visited = set()
        
        maxarea = 0
        
        def dfs(r,c):
            
            s = []
            s.append((r,c))
            visited.add((r,c))
            
            localisland = 1
            while s:
                
                r, c = s.pop()
                directions = [[0,-1], [-1, 0], [0,1], [1,0]]
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    
                    if (nr in range(rows) and nc in range(cols) and 
                        grid[nr][nc] == 1 and (nr,nc) not in visited):
                        s.append((nr,nc))
                        visited.add((nr,nc))
                        localisland += 1
            
            return localisland                      
        
        
        for r in range(rows):
            for c in range(cols):
                
                if grid[r][c] == 1 and (r,c) not in visited:
                    currentarea = 0
                    currentarea = dfs(r,c)
                    maxarea = max(maxarea, currentarea)
                    
        return maxarea
                    
        
        
