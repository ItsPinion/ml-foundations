class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return (False)
        else:
            check = True
            for char in s:
                if (t.find(char) +1):
                    t = t.replace(char,"",1)
                else:
                    check = False
                    break

            return (check)