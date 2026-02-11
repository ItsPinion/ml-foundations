# From https://leetcode.com/problems/climbing-stairs

from functools import lru_cache


class Solution:
    @lru_cache(None)
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        return self.climbStairs(n - 1) + self.climbStairs(n - 2)


solution = Solution()
print(solution.climbStairs(2))  # 2
print(solution.climbStairs(3))  # 3
print(solution.climbStairs(38))  # 3XX
