# Idea: one pass, track the lowest price seen so far and the best
# profit from selling at the current price after buying at that low.
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        low = prices[0]
        best = 0
        for p in prices[1:]:
            best = max(best, p - low)
            low = min(low, p)
        return best
