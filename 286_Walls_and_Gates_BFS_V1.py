from typing import (
    List,
)

class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """
    def walls_and_gates(self, rooms: List[List[int]]):
        # write your code here

        rows = len(rooms)
        cols = len(rooms[0])

        emptycount = 0
        q = collections.deque()

        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 2147483647:
                    emptycount += 1
                elif rooms[r][c] == 0:
                    q.append((r,c))
                    
        while q and emptycount > 0:
            qlen = len(q)
            r, c = q.popleft()
            directions = [[0, -1],[-1,0],[0,1],[1,0]]
            for dr, dc in directions:
                nr = r+dr
                nc = c+dc

                if (nr <0 or nr ==rows or nc <0 or nc == cols or
                rooms[nr][nc] == -1 or rooms[nr][nc] == 0):
                    continue

                if rooms[r][c] ==0 and rooms[nr][nc] == 2147483647:
                    rooms[nr][nc] = 1
                    emptycount -= 1
                elif rooms[r][c] >0 and rooms[nr][nc] == 2147483647:
                    rooms[nr][nc] = rooms[r][c]+ 1
                    emptycount -= 1
                
                q.append((nr,nc))
        return rooms
