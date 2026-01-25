# From https://leetcode.com/problems/valid-palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
        alnum_str:str = ""
        
        for char in s.lower():
            if char.isalnum():
                alnum_str += char
        print(alnum_str)
        return alnum_str == alnum_str[::-1]