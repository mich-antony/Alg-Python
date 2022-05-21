class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        
        rows = len(heights)
        cols = len(heights[0])
        
        pvisited = set()
        avisited = set()
        
        def dfs(r, c, visited, prevheightval):
            if ((r,c) in visited or r < 0 or c < 0 or r == rows or c == cols or 
            heights[r][c] < prevheightval):
                return
            
            visited.add((r,c))
            
            dfs(r, c+1, visited, heights[r][c])
            dfs(r+1, c, visited, heights[r][c])
            dfs(r, c-1, visited, heights[r][c])
            dfs(r-1, c, visited, heights[r][c])
        
        for c in range(cols):
            dfs(0, c, pvisited, heights[0][c])
            dfs(rows -1, c, avisited, heights[rows-1][c])
            
        for r in range(rows):
            dfs(r, 0, pvisited, heights[r][0])
            dfs(r, cols-1, avisited, heights[r][cols-1])
        
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pvisited and (r,c) in avisited:
                    res.append([r,c])
                    
        return res
        
        
