class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def valid_tree(self, n, edges):
        adjmap = {i: [] for i in range(n)}

        for node, nextnode in edges:
            adjmap[node].append(nextnode)
            adjmap[nextnode].append(node)

        visited = set()
        def dfs(curnode, prevnode):
            if curnode in visited:
                return False
            
            visited.add(curnode)

            for nextnode in adjmap[curnode]:
                if nextnode == prevnode:
                    continue
                if not dfs(nextnode, curnode):
                    return False
            return True

        return dfs(0, -1) and len(visited) == n
