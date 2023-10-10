from typing import List
prices1 = [7,6,10,3,1]



class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0

        if not prices:
            return 0

        for i in range (1,len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i]-prices[i-1]
        return profit

solution_instance = Solution()
x = solution_instance.maxProfit(prices1)
print(x)