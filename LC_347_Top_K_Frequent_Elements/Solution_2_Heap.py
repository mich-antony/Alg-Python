class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        ele_counter = {}

        max_heap = []

        for num in nums:
            ele_counter[num] = ele_counter.get(num, 0) + 1
        
        for num, freq in ele_counter.items():
            heapq.heappush(max_heap, (-freq, num))
        
        for _ in range(k):
            res.append(heapq.heappop(max_heap)[1])
        
        return res
