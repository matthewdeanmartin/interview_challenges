from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # returns maximum profit
        profit = 0

        # This works, but isn't performant enough.
        # Probably should extract inner loop to function so I can safely break
        # and save a few if-block evaluations
        for i in range(0, len(prices)):
            for j in range(0, len(prices)):
                buy = prices[i]
                sell = prices[j]
                if sell == 0:
                    pass
                elif i == j:
                    # can't sell on same day
                    pass
                elif j < i:
                    # can't sell before buying
                    pass
                elif sell > buy and sell - buy > profit:
                    profit = sell - buy
        return profit



