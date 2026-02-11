class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        nums_set = set(nums)

        u = set(range(len(nums_set) + 1))

        return tuple(u - nums_set)[0]


soluion = Solution()
print(soluion.missingNumber([3, 0, 1]))  # Expected output: 2
print(soluion.missingNumber([0, 1]))  # Expected output: 2
print(soluion.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))  # Expected output: 8
