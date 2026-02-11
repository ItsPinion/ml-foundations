# from https://leetcode.com/problems/add-digits


class Solution:
    def addDigits(self, num: int) -> int:

        if num < 10:
            return num

        string = str(num)

        sum = 0

        for c in string:
            sum += int(c)

        return self.addDigits(sum)


solution = Solution()
print(solution.addDigits(38))  # Expected output: 2
print(solution.addDigits(0))  # Expected output: 0
print(solution.addDigits(9))  # Expected output: 9
print(solution.addDigits(123456789))  # Expected output: 9
