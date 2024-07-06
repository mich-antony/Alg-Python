class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        num_count = {}
        count_freq = [[] for i in range(len(nums) +1)]

        for num in nums:
            num_count[num] = num_count.get(num, 0) + 1
        
        for num, cnt in num_count.items():
            count_freq[cnt].append(num)

        for i in range(len(count_freq)-1, 0, -1):
            for n in count_freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
