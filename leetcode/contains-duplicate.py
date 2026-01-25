# From https://leetcode.com/problems/contains-duplicate

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        num_set = set(nums)
        
        return len(num_set) < len(nums) 