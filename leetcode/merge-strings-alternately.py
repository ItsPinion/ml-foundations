# From https://leetcode.com/problems/merge-strings-alternately

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        length1 = len(word1)
        length2 = len(word2)
        output = ""
        min_length = min(length1, length2)
        
        for i in range(min_length):
            output += word1[i]
            output += word2[i]
            
        if length1 > length2:
            output += word1[min_length:]
        if length1 < length2:
            output += word2[min_length:]
            
        print()    
        return output
    
    
solution = Solution()

print(solution.mergeAlternately(word1 = "abc", word2 = "pqr"))
print(solution.mergeAlternately(word1 = "ab", word2 = "pqrs"))
print(solution.mergeAlternately(word1 = "abcd", word2 = "pq"))