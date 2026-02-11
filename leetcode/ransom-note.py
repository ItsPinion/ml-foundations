# from https://leetcode.com/problems/ransom-note/


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        while len(ransomNote) > 0:
            char = ransomNote[0]
            if (magazine) and (char in magazine):
                ransomNote = ransomNote.replace(char, "", 1)
                magazine = magazine.replace(char, "", 1)
            else:
                return False

        return True


solution = Solution()
print(solution.canConstruct("a", "b"))
print(solution.canConstruct("aa", "ab"))
print(solution.canConstruct("aa", "aab"))
