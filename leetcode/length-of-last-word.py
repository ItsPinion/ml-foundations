# From https://leetcode.com/problems/length-of-last-word/


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        sting_arr = s.split()

        return len(sting_arr[-1])


solution = Solution()
print(solution.lengthOfLastWord("Hello World"))  # Expected output: 5
print(solution.lengthOfLastWord("   fly me   to   the moon  "))  # Expected output: 4
print(solution.lengthOfLastWord("luffy is still joyboy"))  # Expected output: 6
