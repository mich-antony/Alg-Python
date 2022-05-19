"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        newoldmap = {}
        
        def dfs(node):
            
            if node not in newoldmap:                
                newnode = Node(node.val)
                newoldmap[node] = newnode
                for nei in node.neighbors:
                    newnode.neighbors.append(dfs(nei))
                
                return newnode
            
            else:
                return newoldmap[node]    
                
        return dfs(node)
