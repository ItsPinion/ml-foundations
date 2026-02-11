# From https://leetcode.com/problems/move-zeroes/


class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = nums.count(0)

        for _ in range(count):
            nums.remove(0)
            nums.append(0)


solution = Solution()
nums = [0, 1, 0, 3, 12]
solution.moveZeroes(nums)
print(nums)  # Expected output: [1, 3, 12, 0
