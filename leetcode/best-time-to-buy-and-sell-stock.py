"""

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        for i  in range(0,len(prices)):
            for j in range(i+1, len(prices)):
                if prices[j] < prices[i]:
                    continue
                profit = prices[j] - prices[i]
                if profit > max_profit:
                    max_profit = profit

        return max_profit

solution = Solution()

print(solution.maxProfit([7,1,5,3,6,4]))    #5
print(solution.maxProfit([7,6,4,3,1]))     #0
"""


## Pending
## excluding then this one, other solutions are finished and tested
