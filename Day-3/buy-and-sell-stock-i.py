class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # basically Kadane's algorithm
        # TC: O(n) SC: O(1)

        currentMinimum, maxProfit = float('inf'), 0

        for price in prices:
            currentMinimum = min(currentMinimum, price)
            maxProfit = max(maxProfit, price - currentMinimum)
        
        return maxProfit
