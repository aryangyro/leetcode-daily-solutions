# 3789. Minimum Cost to Acquire Required Items (Daily Challenge, Medium)
# Idea: buy x "both" items. They cover x of each need, and the rest is bought
# separately. The cost is linear in x between 0, min(need1, need2) and
# max(need1, need2), so checking those three values is enough.
class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        def cost(x):
            return x * costBoth + max(0, need1 - x) * cost1 + max(0, need2 - x) * cost2
        return min(cost(0), cost(min(need1, need2)), cost(max(need1, need2)))
