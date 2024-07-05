Iterative
Bottom up (Tabulation) - constant space

class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n

        prev = 0
        cur = 1

        for i in range(2, n+1):
            tmp = prev
            prev = cur
            cur= cur + tmp
        
        return cur


S: O(1)
T: O(n)
