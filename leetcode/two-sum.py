# From https://leetcode.com/problems/two-sum

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]|None:
        nums_set = set(nums)
        
        for i, num in enumerate(nums):
            complement = target - num
            
            if complement in nums_set :
                j = nums.index(complement)
                if i != j: return [i, j]
            
    
solution = Solution()

print(solution.twoSum([2,7,11,15], 9))  # Output: [0, 1]   
print(solution.twoSum([3,2,4], 6))  # Output: [1, 2]   
print(solution.twoSum([3,3], 6))  # Output: [1, 0]   