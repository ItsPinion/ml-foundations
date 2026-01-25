#From https://leetcode.com/problems/fizz-buzz

class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        output:list[str] = []
        for i in range(1,n+1):
            if i % 15 == 0:
                output.append("FizzBuzz")
            elif i % 3 == 0:
                output.append("Fizz")
            elif i % 5 == 0:
                output.append("Buzz")
            else:
                output.append(str(i))
                
        return output
    
    
solution = Solution()

print(solution.fizzBuzz(3))
print(solution.fizzBuzz(5))
print(solution.fizzBuzz(15))