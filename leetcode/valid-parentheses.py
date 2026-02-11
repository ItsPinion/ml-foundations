class Solution:
    def isValid(self, s: str) -> bool:
        stack: list[str] = []

        dictionary = {")": "(", "}": "{", "]": "["}

        for c in s:
            if c in dictionary:
                if len(stack) == 0:
                    return False

                if stack.pop() != dictionary[c]:
                    return False
            else:
                stack.append(c)

        return len(stack) == 0


solution = Solution()
print(solution.isValid("()"))  # Expected output: True
print(solution.isValid("()[]{}"))  # Expected output: True
print(solution.isValid("(]"))  # Expected output: False
print(solution.isValid("([)]"))  # Expected output: False
print(solution.isValid("{[]}"))  # Expected output: True
