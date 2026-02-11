# from https://leetcode.com/problems/majority-element/


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        half_length = len(nums) / 2
        for num in set(nums):
            if nums.count(num) > half_length:
                return num

        return 0


solution = Solution()
print(solution.majorityElement([3, 2, 3]))
print(solution.majorityElement([2, 2, 1, 1, 1, 2, 2]))
print(solution.majorityElement([6, 5, 5]))
