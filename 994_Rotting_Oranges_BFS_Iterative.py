class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        rows = len(grid)
        cols = len(grid[0])
        
        time=0
        fresh=0
        
        q = collections.deque()
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r,c))
        
        while q and fresh > 0:
            
            qlen = len(q)
            
            for i in range(qlen):
            
                r, c = q.popleft()

                directions = [[0,-1],[-1,0],[1,0],[0,1]]

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if nr < 0 or nr == rows or nc<0 or nc==cols or grid[nr][nc] != 1:
                        continue

                    grid[nr][nc] = 2
                    fresh -=1
                    q.append((nr,nc))
            time +=1
            
        return time if fresh == 0 else -1
