# from https://leetcode.com/problems/isomorphic-strings


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(set(s)) != len(set(t)):
            return False

        isomorphic: dict[str, str] = {}

        for i in range(len(s)):
            charS = s[i]
            charT = t[i]
            replacement: str | None = isomorphic.get(charS)

            if replacement:
                if replacement != charT:
                    return False
            else:
                isomorphic[charS] = charT

        return True


solution = Solution()
print(solution.isIsomorphic("egg", "add"))
print(solution.isIsomorphic("foo", "bar"))
print(solution.isIsomorphic("paper", "title"))
print(solution.isIsomorphic("bbbaaaba", "aaabbbba"))
