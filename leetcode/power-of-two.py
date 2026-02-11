# From https://leetcode.com/problems/power-of-two/description/

import math


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        if n <= 0:
            return False

        value = int(math.log(n, 2))
        return 2**value == n


solution = Solution()
print(solution.isPowerOfTwo(536870912))  # Expected output: True
print(solution.isPowerOfTwo(16))  # Expected output: True
print(solution.isPowerOfTwo(3))  # Expected output: False
print(solution.isPowerOfTwo(4))  # Expected output: True
print(solution.isPowerOfTwo(5))  # Expected output: False
print(solution.isPowerOfTwo(6))  # Expected output: False
print(solution.isPowerOfTwo(7))  # Expected output: False
print(solution.isPowerOfTwo(8))  # Expected output: True
print(solution.isPowerOfTwo(9))  # Expected output: False
