class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid:
            return 0
        
        island = 0
        isvisited = set()
        
        rows = len(grid)
        cols = len(grid[0])
        
        def bfs(r, c):
            
            
            q = collections.deque()
            q.append((r,c))
            
            while q:
                
                cr, cc= q.popleft()
                directions = [[0,-1], [-1, 0], [0, 1], [1, 0]]                
                for dr, dc in directions:
                    r = cr + dr
                    c = cc + dc                   
                    if (r in range(rows) and c in range(cols) and grid[r][c] == "1" and ((r,c) not in isvisited)):
                        isvisited.add((r,c))
                        q.append((r,c))
                        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in isvisited:
                    bfs(r, c)
                    island +=1
        
        return island
