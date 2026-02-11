class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        nums.sort()

        length = len(nums)

        for i in range(0, length, 2):
            current = nums[i]

            if (i == length - 1) or (current != nums[i + 1]):
                return current

        return 0


solution = Solution()
print(solution.singleNumber([2, 2, 1]))  # Expected output: 1
print(solution.singleNumber([4, 1, 2, 1, 2]))  # Expected output: 4
print(solution.singleNumber([1]))  # Expected output: 1
