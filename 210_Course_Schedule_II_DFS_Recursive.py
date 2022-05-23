class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        precourse = {}
        
        for i in range(numCourses):
            precourse[i] = []
        
        for crs, depcrs in prerequisites:            
            precourse[crs].append(depcrs)
        
        output = []
        visited = set()
        #outputmarked = set()
        def dfs(crs):
            
            if crs in visited:
                return False
            
            if crs not in precourse or precourse[crs] == []:
                if crs not in output:
                    output.append(crs)
                return True
            
            visited.add(crs)
            for depcrs in precourse[crs]:
                if dfs(depcrs) == False:
                    return False
            output.append(crs)
            precourse[crs] = []
            #outputmarked.add(crs)
            visited.remove(crs)            
            
            return True
        
        for crs in range(numCourses):
            if dfs(crs) == False:
                return []
            
        return output
