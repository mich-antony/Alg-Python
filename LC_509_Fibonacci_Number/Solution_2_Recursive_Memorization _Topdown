Recursive with Memorization
Topdown

class Solution:
    def fib(self, n: int) -> int:
        mem = {0:0, 1:1}

        def recfib(n: int) -> int: 
            if n in mem:
                return mem[n]

            mem[n] = recfib(n-1) + recfib(n-2)
            return mem[n]

        return recfib(n)

S: O(n)
T: O(n)
