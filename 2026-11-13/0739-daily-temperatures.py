# 739. Daily Temperatures (Medium)
# Idea: monotonic decreasing stack of indices. For each day, pop all earlier days
# that are colder than today — today is their first warmer day.
from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                j = stack.pop()
                ans[j] = i - j
            stack.append(i)
        return ans
