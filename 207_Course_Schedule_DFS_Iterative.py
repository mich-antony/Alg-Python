class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        incomingcrs = collections.defaultdict(set)
        outgoingcrs = collections.defaultdict(set)
        
        for crs, depcrs in prerequisites:
            incomingcrs[crs].add(depcrs)
            outgoingcrs[depcrs].add(crs)
            
        cantake = []
        for i in range(numCourses):
            if len(incomingcrs[i]) == 0:
                cantake.append(i)
        
        taken = 0
        while len(cantake) > 0:
            
            crs = cantake.pop()
            taken += 1
            
            for nextcrs in outgoingcrs[crs]:
                incomingcrs[nextcrs].remove(crs)
                if len(incomingcrs[nextcrs]) == 0:
                    cantake.append(nextcrs)
        
        return taken == numCourses
