# Idea: DP over steps. dp[j] = cheapest cost to reach step j.
# From step i you can jump 1-3 steps, paying costs[j] + (j-i)^2,
# so dp[j] = costs[j] + min(dp[j-k] + k^2) for k in 1..3.
from typing import List


class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        dp = [0] * (n + 1)
        for j in range(1, n + 1):
            dp[j] = costs[j - 1] + min(
                dp[j - k] + k * k for k in (1, 2, 3) if j - k >= 0
            )
        return dp[n]
