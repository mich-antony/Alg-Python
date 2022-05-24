class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = {i: float("inf") for i in range(n)}
        prices[src] = 0
        
        
        for i in range(k+1):
            
            tmpprices = prices.copy()
            
            for s, dest, cost in flights:
                if prices[s] == float("inf"):
                    continue
                
                if prices[s] + cost < tmpprices[dest]:  
                    tmpprices[dest] = prices[s] + cost            
            
            prices = tmpprices
        
        return -1 if prices[dst]== float("inf") else prices[dst]
                
