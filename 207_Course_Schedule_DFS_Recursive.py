class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        
        precourseMap = {}
        visited = set()
        
        def dfs(currentcrs):

            if currentcrs in visited:
                return False
            
            if currentcrs not in precourseMap or precourseMap[currentcrs] == []:
                return True
            
            visited.add(currentcrs)
            for precrs in precourseMap[currentcrs]:
                if not dfs(precrs):
                    return False
            precourseMap[currentcrs] = []
            visited.remove(currentcrs)
            return True
            
        for c1, c2 in prerequisites:
            if c1 not in precourseMap:
                precourseMap[c1] = [c2]
            else:
                precourseMap[c1].append(c2)
        
        for k in precourseMap.keys():
            if not dfs(k):
                return False
        return True
        
        
        
